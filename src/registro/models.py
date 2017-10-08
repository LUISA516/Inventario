# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime, date, time, timedelta
import calendar


# Create your models here.
class Registro(models.Model):
	idRegistro = models.CharField(max_length=50)
	nombreRegistro = models.CharField(max_length=50)
	cantidadRegistro = models.IntegerField()
	fechaRegistro = models.DateField()