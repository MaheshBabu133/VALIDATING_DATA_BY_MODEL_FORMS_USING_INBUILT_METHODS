# Generated by Django 4.1.7 on 2023-04-27 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_webpage_accessrecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrecord',
            old_name='data',
            new_name='date',
        ),
    ]
