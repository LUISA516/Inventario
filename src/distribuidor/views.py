# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
def index(reguest):
	return HttpResponse('pagina de proveedor')
# Create your views here.

