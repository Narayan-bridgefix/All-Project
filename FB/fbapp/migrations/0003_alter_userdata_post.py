# Generated by Django 5.1.1 on 2024-09-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbapp', '0002_userdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='post',
            field=models.ImageField(upload_to='fbapp/images/'),
        ),
    ]