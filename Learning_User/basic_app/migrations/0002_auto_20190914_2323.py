# Generated by Django 2.2.1 on 2019-09-14 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile',
            new_name='profile_pic',
        ),
    ]
