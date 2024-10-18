# Generated by Django 5.1.1 on 2024-10-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgre_app', '0006_remove_postgres_data_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='postgres_data',
            name='age',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='postgres_employee',
            name='age',
            field=models.IntegerField(default=10),
        ),
    ]