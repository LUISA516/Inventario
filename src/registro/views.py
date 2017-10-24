# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from.forms import RegistroForm

# Create your views here.

def index(request):
	form = RegistroForm()
	context = {
		'form': form,
	}
	return render(request, 'inicio/index.html', context)	