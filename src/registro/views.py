# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from.forms import RegistroForm
from.models import Registro

# Create your views here.

def index(request):
	form = RegistroForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get("Codigo")
		obj = Registro.objects.create(id_registro=abc)
		abcd = form_data.get("Cantidad")
		objd = Registro.objects.create(cantidad_registro=abcd)
	context = {
		'form': form,
	}
	return render(request, 'inicio/index.html', context)	