from django.db import models
#for database we use models

#for python stuff views.py which is connected to url.py and templates

# Create your models here.

#pyhton to SQL django kar dega after migration
# python manage.py makemigration

class list(models.Model):

	item= models.CharField(max_length=200)
	completed=models.BooleanField(default=False)

	def __str__ (self):
		return self.item+" | "+ str(self.completed) 

