# Generated by Django 4.0.6 on 2022-12-06 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_rename__age_employees_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='avatar',
            field=models.ImageField(default=None, upload_to='images'),
        ),
        migrations.AddField(
            model_name='employees',
            name='cv',
            field=models.FileField(default=None, upload_to='files'),
        ),
    ]
