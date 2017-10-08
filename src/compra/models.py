# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from producto.models import Producto
from distribuidor.models import Distribuidor

# Create your models here.
class Compra(models.Model):
	codigoCompra = models.CharField(max_length=50, primary_key=True,)
	idProducto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
	nitProveedor = models.ForeignKey(Distribuidor, null=True, blank=True, on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	valorCompra = models.IntegerField()
	#fecha = models.DateTimeField()#(auto_now_add=True, auto_now=False)
