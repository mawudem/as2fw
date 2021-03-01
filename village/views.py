from django.http import HttpResponse,  Http404
from django.shortcuts import render, redirect
from django.template import loader

from blog.models import About, Galerie, Projet


"""docstring for Welcome"""
def  index(request):
    #getting the templates
    # selectionner la derniere mise a jour d'about
    about = About.objects.order_by('id')
    for a in about:
    	pass
    # selectionner les photo à metre dans la galerie
    photo = Galerie.objects.order_by('id')

    # selectionnen les projets
    projet = Projet.objects.order_by('id') #.filter(Status_title = "En cours...")
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'about':a, 'photo':photo, 'projet': projet}))

def  Histoire(request):
    #getting the templates
    template = loader.get_template('histoire.html')
    return HttpResponse(template.render())


def  Atout(request):
    #getting the templates
    template = loader.get_template('atout.html')
    return HttpResponse(template.render())


def  Don(request):
    #getting the templates
    template = loader.get_template('don.html')
    return HttpResponse(template.render())

def  Inscription(request):
    #getting the templates
    template = loader.get_template('inscription.html')
    return HttpResponse(template.render())


def  Vision(request):
    #getting the templates
    template = loader.get_template('vision.html')
    return HttpResponse(template.render())


    