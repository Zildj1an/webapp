from django.db import models

# Create your models here.
class Regis(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __unicode__(self): #Python 2
		return self.email

	def __str__(self): #python 3
		return self.email