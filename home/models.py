
from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=110)
    phone = models.CharField(max_length=111)  
   