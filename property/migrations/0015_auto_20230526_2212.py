# Generated by Django 2.2.24 on 2023-05-26 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20230524_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]
