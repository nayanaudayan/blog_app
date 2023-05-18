from datetime import date
from pyexpat import model
from django.db import models

class Product(models.Model):
    p_title = models.CharField(max_length=40,default="")
    p_num = models.CharField(max_length=30)
    p_description = models.TextField()
    p_author = models.CharField(max_length=300)
