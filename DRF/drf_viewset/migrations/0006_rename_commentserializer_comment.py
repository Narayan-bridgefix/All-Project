# Generated by Django 5.1.1 on 2024-09-30 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drf_viewset', '0005_commentserializer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentSerializer',
            new_name='Comment',
        ),
    ]