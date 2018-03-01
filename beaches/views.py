# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Beach

# Create your views here.

def index(request):
	template = loader.get_template('beaches/index.html')
	return HttpResponse(template.render())

def search(request):
	template = loader.get_template('beaches/search.html')
	return HttpResponse(template.render())