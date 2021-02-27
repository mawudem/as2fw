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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),  # Home page
    #++++++++++++++++++++++++++++++++++++++++++++++++
    #                       blog                    #
    #++++++++++++++++++++++++++++++++++++++++++++++++
    path('post/', views.PostListView.as_view(), name='index'),  # la page de detaille d'un blog
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]	

if settings.DEBUG:   
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


