# Generated by Django 4.0.1 on 2022-07-28 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_rename_first_name_profile_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]