from __future__ import unicode_literals

from django.db import models

# Create your models here.
class details(models.Model):
    name = models.CharField(max_length=20)
    age  = models.IntegerField()
    runs = models.IntegerField()
    centuries = models.IntegerField()
    country = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)+' '+str(self.age)+' '+str(self.runs)+' '+str(self.centuries)+' '+str(self.country)
