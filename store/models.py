from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Vendor(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name

    def register(self):
        self.save()
    def getuser(email):
        return Vendor.objects.get(email=email)



class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(default=0,max_length=30)
    description = models.CharField(max_length=200, default='',null=True,blank=True)
    image= models.ImageField(upload_to='uploads/products/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=1)
    @staticmethod
    def GetAllProducts():
        return Product.objects.all()
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)
class Customer(models.Model):
    first_name =models.CharField(max_length=30)
    last_name =models.CharField(max_length=30)
    email =models.CharField(max_length=60)
    password =models.CharField(max_length=100)
    def register(self):
        self.save()
    def getuser(email):
        return Customer.objects.get(email=email)
