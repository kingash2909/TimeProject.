# Generated by Django 3.0.6 on 2020-09-09 04:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TimeApp', '0003_auto_20200909_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due',
        ),
        migrations.AddField(
            model_name='task',
            name='ttimer',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
