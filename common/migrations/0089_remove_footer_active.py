# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 17:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0088_osfpage_footer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='active',
        ),
    ]