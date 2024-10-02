# Generated by Django 5.1.1 on 2024-09-23 05:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('like', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Like_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fbapp.user')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fbapp.post_image')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fbapp.user')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fbapp.post_image')),
            ],
        ),
    ]
