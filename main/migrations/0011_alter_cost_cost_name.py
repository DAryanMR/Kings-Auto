# Generated by Django 5.0.3 on 2024-04-26 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_stuff_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='cost_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
