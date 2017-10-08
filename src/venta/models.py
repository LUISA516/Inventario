# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from producto.models import Producto
from datetime import datetime, date, time, timedelta
import calendar



# Create your models here.
formato = "%d-%m-%y %H:%M %S"
hoy = datetime.today()

cadena2 = hoy.strftime(formato)

class Venta(models.Model):
	codigoVenta = models.CharField(max_length=50, primary_key=True,)
	idProducto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
	fechaVenta = models.DateField()
	cantidad = models.IntegerField()
	valorVenta = models.IntegerField()