from django.http import HttpResponse,  Http404
from django.shortcuts import render, redirect
from django.template import loader

"""docstring for Welcome"""
def  index(request):
    #getting the templates
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def  post(request):
    #getting the templates
    template = loader.get_template('single.html')
    return HttpResponse(template.render())