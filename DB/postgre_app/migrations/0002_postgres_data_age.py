# Generated by Django 5.1.1 on 2024-10-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgre_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postgres_data',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
