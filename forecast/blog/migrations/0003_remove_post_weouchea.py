# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 23:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_weouchea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='weouchea',
        ),
    ]
