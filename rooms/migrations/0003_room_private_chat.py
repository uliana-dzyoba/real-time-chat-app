# Generated by Django 4.1 on 2022-09-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_message_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='private_chat',
            field=models.BooleanField(default=False),
        ),
    ]
