# Generated by Django 5.1.2 on 2024-10-23 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ref',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.student')),
            ],
        ),
    ]
