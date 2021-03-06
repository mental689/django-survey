# Generated by Django 2.1.2 on 2018-12-08 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responses', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='response',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='survey.Video', verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='video',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='vid',
            field=models.CharField(blank=True, max_length=50, unique=True, verbose_name='Video ID'),
        ),
    ]
