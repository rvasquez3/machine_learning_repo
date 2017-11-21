# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alg_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DataTypeTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ml_app.DataType')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TaskAlg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ml_app.Algorithm')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ml_app.Task')),
            ],
        ),
        migrations.AddField(
            model_name='datatypetask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ml_app.Task'),
        ),
    ]
