# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glgl_app', '0012_remove_userextraprofile_headimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextraprofile',
            name='headImage',
            field=models.ImageField(default='default/default.jpg', upload_to='headImages'),
        ),
    ]
