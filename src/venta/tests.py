# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from venta.models import Venta
from datetime import datetime, date, time, timedelta
import calendar

formato = "%d-%m-%y %H:%M %S"
hoy = datetime.today()

cadena2 = hoy.strftime(formato)

# Create your tests here.
class VentaTest(TestCase):
	def setUp(self):
		Venta.objects.create(codigoVenta='3', fechaVenta='2017-10-01', cantidad=4, valorVenta=5)


	def test_codigo_venta(self):  
		codigo = Venta.objects.get(codigoVenta='3')
		self.assertEqual(codigo.codigoVenta, '3')


	def test_fecha_venta(self):
		fecha = Venta.objects.get(fechaVenta='2017-10-01')
		self.assertEqual(fecha.fechaVenta, '2017,10, 1')
		