# Generated by Django 2.2.24 on 2023-05-17 20:47

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20230517_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='RU'),
        ),
    ]
