# Generated by Django 2.1.7 on 2019-02-18 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_auto_20190218_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connected',
            name='user',
        ),
    ]
