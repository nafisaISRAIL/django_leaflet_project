# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_category_translate'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
    ]