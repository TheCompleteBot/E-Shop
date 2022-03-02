from django.contrib import admin
from .models import Product,Category,Customer,Vendor
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','category','price','vendor']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','password']
class AdminVendor(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'password']

admin.site.register(Product, AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Vendor,AdminVendor)

