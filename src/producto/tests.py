# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from producto.models import Producto

# Create your tests here.
class ProductoTest(TestCase):
	def setUp(self):
		Producto.objects.create(idProducto='1', nombre='bota', precioVenta=12)
		

	def test_id_producto(self):
		idProducto = Producto.objects.get(idProducto='1')
		self.assertEqual(idProducto.idProducto,'1')

	def test_nombre(self):
		nombre = Producto.objects.get(nombre='bota')
		self.assertEqual(nombre.nombre, 'bota')
		

	def test_precio_venta(self):
		precio = Producto.objects.get(precioVenta=12)
		self.assertEqual(precio.precioVenta, 12)
		