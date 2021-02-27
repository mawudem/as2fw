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

def  post(request):
    #getting the templates
    template = loader.get_template('single.html')
    return HttpResponse(template.render())