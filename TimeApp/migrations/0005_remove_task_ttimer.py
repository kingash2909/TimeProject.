# Generated by Django 3.0.6 on 2020-09-09 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeApp', '0004_auto_20200909_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='ttimer',
        ),
    ]
