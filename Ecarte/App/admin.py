from typing import List
from django.contrib import admin

from App.models import Customer, Product, laptops, phones, shirts,Cart


# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','Fname','Lname','Address','State']
    
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','Title','Category','MRP','SellPrice']

@admin.register(shirts)
class shirtsModelAdmin(admin.ModelAdmin):
    list_display = ['id','Item','Brand','Color']

@admin.register(phones)
class phonesModelAdmin(admin.ModelAdmin):
    list_display = ['id','Item','Brand','color','Ram','Storage']

@admin.register(laptops)
class laptopsMOdelAdmin(admin.ModelAdmin):
    list_display = ['id','Item','Brand','Ram','Storage','Storage_type']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','customer','cart_item','qty']