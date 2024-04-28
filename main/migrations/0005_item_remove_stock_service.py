# Generated by Django 5.0.3 on 2024-04-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_service_service_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100)),
                ('item_cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('item_charge', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='stock',
            name='service',
        ),
    ]
