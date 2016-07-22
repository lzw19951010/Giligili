# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 16:28
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
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NContent', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserExtraProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UNickName', models.CharField(max_length=20)),
                ('UDescription', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VTitle', models.CharField(max_length=50)),
                ('VUploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glgl_app.UserExtraProfile')),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='NUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glgl_app.UserExtraProfile'),
        ),
    ]
