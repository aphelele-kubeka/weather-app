# Generated by Django 3.2.4 on 2021-06-23 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20210623_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='note',
            name='modified_at',
        ),
    ]
