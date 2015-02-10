from django.db import models

# Create your models here.

class servicelist(models.Model):
    name = models.CharField(max_length=200)
    address = models.URLField(max_length=200)
    port = models.IntegerField()
    version = models.CharField(max_length=200)
    
    