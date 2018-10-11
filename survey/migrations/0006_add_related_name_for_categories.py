# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 14:52


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_rename_question_related_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='survey',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='categories', to='survey.Survey'
            ),
        ),
    ]
