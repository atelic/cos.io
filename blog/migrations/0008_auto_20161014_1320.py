# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 13:20
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20161013_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='additional',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='body',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock()), ('code_block', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('python', 'python'), ('css', 'css'), ('sql', 'sql'), ('javascript', 'javascript'), ('clike', 'clike'), ('markup', 'markup'), ('java', 'java')], default='python')), ('codes', wagtail.wagtailcore.blocks.TextBlock()))))), blank=True, null=True),
        ),
    ]
