# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armorstats',
            name='charisma',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='armorstats',
            name='constitution',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='armorstats',
            name='defense',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='armorstats',
            name='dexterity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='armorstats',
            name='luck',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='armorstats',
            name='perception',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='armorstats',
            name='strength',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='armorstats',
            name='willpower',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='armorstats',
            name='wisdom',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
