# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 16:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0077_auto_20161004_1716'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePage',
            new_name='OSFPage',
        ),
    ]