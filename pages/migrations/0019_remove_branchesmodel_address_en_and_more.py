# Generated by Django 5.1 on 2024-11-07 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_rename_address_branchesmodel_address_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branchesmodel',
            name='address_en',
        ),
        migrations.RemoveField(
            model_name='branchesmodel',
            name='address_ru',
        ),
    ]
