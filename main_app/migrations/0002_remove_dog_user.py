# Generated by Django 3.2.8 on 2021-11-06 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='user',
        ),
    ]
