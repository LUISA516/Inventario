# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='cantidadRegistro',
            new_name='cantidad_registro',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='fechaRegistro',
            new_name='fecha_registro',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='idRegistro',
            new_name='id_registro',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='nombreRegistro',
            new_name='nombre_registro',
        ),
    ]