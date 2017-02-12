# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('description', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('feature_image_link', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coala_admin.Blog')),
            ],
        ),
    ]