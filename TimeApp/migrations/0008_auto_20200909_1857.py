# Generated by Django 3.0.6 on 2020-09-09 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeApp', '0007_auto_20200909_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tend',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='tname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='tprojects',
            new_name='projects',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='tstart',
            new_name='start',
        ),
    ]
