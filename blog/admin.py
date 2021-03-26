from django.contrib import admin

# Register your models here.
from .models import Post, Comment, About,Galerie, Projet

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(About)
admin.site.register(Galerie)
admin.site.register(Projet)
#admin.site.register(Status)
