# from django.db import migrations


# def forwards(apps, schema_editor):
#     if schema_editor.connection.alias != "postgres_db":
#         return
#     # Your migration code goes here


# class Migration(migrations.Migration):
#     dependencies = [
#         # Dependencies to other migrations
#     ]

#     operations = [
#         migrations.RunPython(forwards, hints={"target_db": "postgres_db"}),
#     ]
    
# from django.core.management.commands.migrate import Command as CoreMigrateCommand
# # from myapp.db import create_constraints


# class Command(CoreMigrateCommand):
#     def handle(self, *args, **options):
#         # Do normal migrate
#         super().handle(*args, **options)

#         # Then our custom extras
#         # create_constraints()    