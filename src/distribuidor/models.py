# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Distribuidor(models.Model):
	nitDistribuidor = models.CharField(max_length=50, primary_key=True,)
	nombreDistribuidor = models.CharField(max_length=50,blank=True, null=True)
	direccion = models.CharField(max_length=50,blank=True, null=True)
	telefono = models.CharField(max_length=50,blank=True, null=True)