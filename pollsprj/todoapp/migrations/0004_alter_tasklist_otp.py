# Generated by Django 5.1.1 on 2024-09-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_tasklist_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='otp',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
