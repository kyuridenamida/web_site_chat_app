# Generated by Django 3.0.1 on 2019-12-18 13:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20191217_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lobby',
            old_name='name',
            new_name='lobby_name',
        ),
        migrations.AddField(
            model_name='message',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.User'),
        ),
    ]
