# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-24 14:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Found',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=256, null=True)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Lost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('clothes_color', models.CharField(blank=True, max_length=120, null=True)),
                ('complexion', models.CharField(blank=True, choices=[('dark', 'Dark'), ('light', 'Light Skin'), ('chocolate', 'Chocolate')], max_length=120)),
                ('child_pic', models.ImageField(upload_to='HackOkPlease/pic_folder/')),
                ('contact', models.CharField(max_length=256, null=True)),
                ('found', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
