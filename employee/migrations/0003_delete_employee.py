# Generated by Django 3.1.1 on 2021-01-27 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('employee', '0002_auto_20210127_1629'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
