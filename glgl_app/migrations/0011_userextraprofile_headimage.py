# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glgl_app', '0010_comment_cdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextraprofile',
            name='headimage',
            field=models.ImageField(default='default/default.jpg', upload_to='headimage'),
        ),
    ]