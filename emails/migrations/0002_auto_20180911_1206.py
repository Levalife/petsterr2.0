# Generated by Django 2.0.6 on 2018-09-11 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emails',
            new_name='Email',
        ),
    ]