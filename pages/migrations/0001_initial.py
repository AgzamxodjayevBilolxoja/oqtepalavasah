# Generated by Django 5.1 on 2024-10-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uz', models.CharField(max_length=150)),
                ('ru', models.CharField(max_length=150)),
                ('en', models.CharField(max_length=150)),
            ],
        ),
    ]
