# Generated by Django 5.1 on 2024-10-27 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_branchesmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchesmodel',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
