# Generated by Django 3.0 on 2019-12-17 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='user_id',
            new_name='user_ids',
        ),
    ]
