# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 08:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glgl_app', '0014_remove_userextraprofile_headimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='money',
            new_name='like',
        ),
    ]
