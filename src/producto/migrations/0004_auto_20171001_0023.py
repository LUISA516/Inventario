# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 00:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_auto_20170928_0428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='id',
            new_name='idProducto',
        ),
    ]