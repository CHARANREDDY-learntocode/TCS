# Generated by Django 3.1.1 on 2021-01-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20210127_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
