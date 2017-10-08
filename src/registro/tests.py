# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from registro.models import Registro


# Create your tests here.
class RegistroTest(TestCase):
	def setUp(self):
		Registro.objects.create(idRegistro='1', nombreRegistro='montera', cantidadRegistro=2, fechaRegistro='2017-10-1')

	def test_registro_id(self):
		registro = Registro.objects.get(idRegistro='1')
		self.assertEqual(registro.idRegistro, '1')

	def test_nombre_registro(self):
			nombre = Registro.objects.get(nombreRegistro='montera')
			self.assertEqual(nombre.nombreRegistro, 'montera')	

	def test_cantidad_registro(self):
		cantidad = Registro.objects.get(cantidadRegistro=2)
		self.assertEqual(cantidad.cantidadRegistro, 2)

	def test_fecha_registro(self):
		fecha = Registro.objects.get(fechaRegistro='2017-10-1')
		self.assertEqual(fecha.fechaRegistro,'2017-10-1')
		print fechaRegistro

			