# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default=3),
            preserve_default=False,
        ),
    ]