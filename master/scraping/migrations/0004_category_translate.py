# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_auto_20170519_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='translate',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
