# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.ImageField(upload_to='images/', null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE,)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text

class About(models.Model):
    experience_year = models.IntegerField(default = 0)
    project_finish = models.IntegerField(default = 0)
    project_appending = models.IntegerField(default = 0)
    project_not_start = models.IntegerField(default = 0)

class Galerie(models.Model):
    title = models.CharField(max_length=100)
    photo= models.ImageField(upload_to='images/', null=True)
    def __str__(self):
        return self.title

class Projet(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    photo= models.ImageField(upload_to='images/', null=True)
    description = models.TextField()
    status = models.ForeignKey('blog.Status', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Status(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
