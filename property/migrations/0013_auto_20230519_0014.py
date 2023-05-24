# Generated by Django 2.2.24 on 2023-05-18 21:14

from django.db import migrations


def fill_class_owner_from_class_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
            owner = Owner.objects.get_or_create(
                owner=flat.owner,
                owners_phonenumber=flat.owners_phonenumber,
                owner_pure_phone=flat.owner_pure_phone,
                flat=flat,
            )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner'),
    ]

    operations = [
        migrations.RunPython(fill_class_owner_from_class_flat)
    ]
