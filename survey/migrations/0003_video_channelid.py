# Generated by Django 2.1.3 on 2018-12-23 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20181208_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='channelId',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Channel ID'),
        ),
    ]