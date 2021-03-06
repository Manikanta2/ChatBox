# Generated by Django 2.1.7 on 2019-02-18 19:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_auto_20190218_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbox',
            name='group_ID',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_ID',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
