# Generated by Django 5.0.3 on 2024-04-06 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('car_name', models.CharField(max_length=100)),
                ('car_color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('cost_id', models.AutoField(primary_key=True, serialize=False)),
                ('cost_date', models.DateField()),
                ('cost_name', models.CharField(max_length=100)),
                ('cost_amount', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Jobcard',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.CharField(default=None, max_length=100, null=True)),
                ('customer_name', models.CharField(default=None, max_length=100, null=True)),
                ('customer_address', models.CharField(default=None, max_length=100, null=True)),
                ('customer_phone', models.CharField(default=None, max_length=100, null=True)),
                ('chassis', models.CharField(default=None, max_length=100, null=True)),
                ('vehicle', models.CharField(default=None, max_length=100, null=True)),
                ('model_year', models.CharField(default=None, max_length=100, null=True)),
                ('model', models.CharField(default=None, max_length=100, null=True)),
                ('engine', models.CharField(default=None, max_length=100, null=True)),
                ('reg', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('sale_id', models.AutoField(primary_key=True, serialize=False)),
                ('memo_id', models.IntegerField(default=None, null=True)),
                ('sale_date', models.DateField()),
                ('customer_name', models.CharField(max_length=100)),
                ('car_name', models.CharField(max_length=100)),
                ('car_reg', models.CharField(max_length=20)),
                ('chassis_no', models.CharField(max_length=50)),
                ('qty', models.IntegerField(default=1)),
                ('sale_total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=100)),
                ('service_cost', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('service_charge', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('stuff_id', models.AutoField(primary_key=True, serialize=False)),
                ('stuff_name', models.CharField(max_length=100)),
                ('stuff_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duty_days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IssueDemandEngineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField(default=None, null=True)),
                ('engineer', models.CharField(default=None, max_length=100, null=True)),
                ('technician', models.CharField(default=None, max_length=100, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.jobcard')),
            ],
        ),
        migrations.CreateModel(
            name='IssueDemand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField(default=None, null=True)),
                ('material_description', models.CharField(default=None, max_length=100, null=True)),
                ('material_qty', models.CharField(default=None, max_length=100, null=True)),
                ('material_price', models.CharField(default=None, max_length=100, null=True)),
                ('req_description', models.CharField(default=None, max_length=100, null=True)),
                ('req_qty', models.CharField(default=None, max_length=100, null=True)),
                ('req_sign', models.CharField(default=None, max_length=100, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.jobcard')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField(default=None, null=True)),
                ('diagnosis_detail', models.CharField(default=None, max_length=100, null=True)),
                ('ref_by', models.CharField(default=None, max_length=100, null=True)),
                ('diagnosed_by', models.CharField(default=None, max_length=100, null=True)),
                ('driver_signature', models.CharField(default=None, max_length=100, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.jobcard')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField(default=None, null=True)),
                ('request', models.CharField(default=None, max_length=100, null=True)),
                ('category', models.CharField(default=None, max_length=100, null=True)),
                ('charge', models.CharField(default=None, max_length=100, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.jobcard')),
            ],
        ),
        migrations.CreateModel(
            name='Dues',
            fields=[
                ('due_id', models.AutoField(primary_key=True, serialize=False)),
                ('due_date', models.DateField(default=None)),
                ('due_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_received', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('memo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sale')),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.service'),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField(default=0)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.service')),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='stuff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.stuff'),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('salary_id', models.AutoField(primary_key=True, serialize=False)),
                ('salary_date', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('paid_status', models.BooleanField(default=False)),
                ('stuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.stuff')),
            ],
        ),
    ]
