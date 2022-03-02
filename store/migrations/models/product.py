from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(default=0,max_length=30)
    description = models.CharField(max_length=200, default='')
    image= models.ImageField(upload_to='products/')