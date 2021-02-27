from django.db import models

# Create your models here.


class contact(object):
	"""docstring for contact"""
	name = models.CharField(max_lenght = 200)
	email = models.EmailField()
	subject = name = models.CharField(max_lenght = 200)
	message = models.TextField()
	
	def __str__():
		return contact.name		