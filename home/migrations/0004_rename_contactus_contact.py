# Generated by Django 4.0.3 on 2022-03-20 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_contact_contactus'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contactus',
            new_name='Contact',
        ),
    ]