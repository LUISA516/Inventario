# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
	idProducto = models.CharField(max_length=50, primary_key=True)
	nombre = models.CharField(max_length=50)
	precioProducto = models.IntegerField()

	
