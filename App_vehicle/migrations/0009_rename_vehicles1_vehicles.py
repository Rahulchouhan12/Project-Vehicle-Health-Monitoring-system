# Generated by Django 4.1.7 on 2023-05-12 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_vehicle', '0008_vehicles1_delete_vehicles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='vehicles1',
            new_name='vehicles',
        ),
    ]