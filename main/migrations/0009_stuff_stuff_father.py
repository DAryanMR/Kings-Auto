# Generated by Django 5.0.3 on 2024-04-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_stuff_join_date_stuff_stuff_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='stuff_father',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
