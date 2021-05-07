"""village URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from blog import views
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),  # Home page
    path('don/', Don),  # Home page
    path('inscription/', Inscription),  # Home page
    #++++++++++++++++++++++++++++++++++++++++++++++++
    #                       blog                    #
    #++++++++++++++++++++++++++++++++++++++++++++++++
    path('post/', views.PostListView.as_view(), name='post_list'),  # la page de detaille d'un blog
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]	

if settings.DEBUG:   
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# me rappeler de chercher le role de la ligne la quand je serai connecte
