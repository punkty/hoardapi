# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 05:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('armor_class', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Light', 'Light armor'), ('Medium', 'Medium armor'), ('Heavy', 'Heavy armor')], max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('stealth', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('magical', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArmorStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('charisma', models.IntegerField(blank=True, default=0)),
                ('constitution', models.IntegerField(blank=True, default=0)),
                ('defense', models.IntegerField(blank=True, default=0)),
                ('dexterity', models.IntegerField(blank=True, default=0)),
                ('luck', models.IntegerField(blank=True, default=0)),
                ('perception', models.IntegerField(blank=True, default=0)),
                ('strength', models.IntegerField(blank=True, default=0)),
                ('willpower', models.IntegerField(blank=True, default=0)),
                ('wisdom', models.IntegerField(blank=True, default=0)),
                ('armor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='resources.Armor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Bio', 'Biological'), ('Mech', 'Mechanical'), ('Summon', 'Summoned')], max_length=100)),
                ('speed', models.CharField(max_length=50)),
                ('max_burden', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=100)),
                ('health', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Potion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=100)),
                ('effect', models.CharField(max_length=200)),
                ('side_effect', models.CharField(blank=True, default='None', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trinket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('magical', models.BooleanField(default=False)),
                ('effects', models.CharField(blank=True, default='-', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('damage', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Simple M', 'Simple Melee'), ('Simple R', 'Simple Ranged'), ('Martial M', 'Martial Melee'), ('Martial R', 'Martial Ranged')], max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('stealth', models.CharField(blank=True, default='-', max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('magical', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeaponStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('charisma', models.IntegerField(blank=True, default=0)),
                ('constitution', models.IntegerField(blank=True, default=0)),
                ('defense', models.IntegerField(blank=True, default=0)),
                ('dexterity', models.IntegerField(blank=True, default=0)),
                ('luck', models.IntegerField(blank=True, default=0)),
                ('perception', models.IntegerField(blank=True, default=0)),
                ('strength', models.IntegerField(blank=True, default=0)),
                ('willpower', models.IntegerField(blank=True, default=0)),
                ('wisdom', models.IntegerField(blank=True, default=0)),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='resources.Weapon')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
