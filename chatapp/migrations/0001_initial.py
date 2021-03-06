# Generated by Django 2.1.7 on 2019-02-12 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBox',
            fields=[
                ('group_name', models.CharField(max_length=200)),
                ('group_description', models.TextField(default='Required', max_length=420)),
                ('group_ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Connected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.ChatBox')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message_tag', models.CharField(max_length=100)),
                ('message_text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('to_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.ChatBox')),
            ],
        ),
        migrations.AddField(
            model_name='connected',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.Message'),
        ),
        migrations.AddField(
            model_name='connected',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
