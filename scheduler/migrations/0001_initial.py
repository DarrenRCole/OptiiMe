# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-06 02:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=5)),
                ('end_time', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Professor_Unavailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=1)),
                ('start_time', models.CharField(max_length=5)),
                ('end_time', models.CharField(max_length=5)),
                ('preference_level', models.IntegerField(default=0)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Professor')),
            ],
        ),
        migrations.AddField(
            model_name='offering',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Section'),
        ),
    ]
