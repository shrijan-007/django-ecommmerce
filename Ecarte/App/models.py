from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils.regex_helper import Choice
States_choice = [
    ("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry")
]
laptops_brand = [
    ('hp','hp'),
    ('dell','dell'),
    ('apple','apple')
]
product_Categories = [
    ('smartphone','smartphone'),
    ('MFashion','MFashion'),
    ('shirt','shirt'),
    ('FFashion','FFashion'),
    ('Laptops','Laptops'),
    ('Headphones','Headphones'),
    ('Shoes','Shoes'),
    ('TV','TV'),
    ('electronics','electronics')
]

color_choices = [
    ('red','red'),
    ('white','white'),
    ('black','black'),
    ('gray','gray'),
    ('blue','blue'),
    ('purple','purple'),
    ('green','green')
]

mobile_brands = [
    ('MI','mi'),
    ('IP','iphone'),
    ('OP','one plus'),
    ('SAM','samsung'),
]

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    PhoneNo = models.PositiveIntegerField()
    Address = models.CharField(max_length=50)
    State = models.CharField(choices=States_choice, max_length=255)
    Pincode = models.CharField(max_length=10)

class Product(models.Model):
    Title = models.CharField(max_length=40)
    Category = models.CharField(
        choices=product_Categories,max_length=15
    )
    MRP = models.FloatField()
    SellPrice = models.FloatField()
    product_image = models.ImageField(upload_to = 'allproducts')
    product_image01 = models.ImageField(upload_to = 'allproducts')
    product_image02 = models.ImageField(upload_to = 'allproducts')
    description = models.TextField()
    offer = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)

class shirts(models.Model):
    Item = models.ForeignKey(Product,on_delete=models.CASCADE)
    Brand = models.CharField(choices=[('AlS','allen solly'),('PE','peter england'),('PA','park avenue'),('LP','louis philepe'),],max_length=3)
    Color = models.CharField(choices=color_choices, max_length=20)
    

class phones(models.Model):
    Item = models.ForeignKey(Product,on_delete=models.CASCADE)
    Brand = models.CharField(choices = mobile_brands,max_length=5)
    Item_model = models.CharField(max_length=12,null=True)
    color = models.CharField(choices = color_choices ,max_length=20)
    Ram = models.IntegerField()
    Storage = models.CharField(choices=[('32 GB','32 GB'),('64GB','64 GB'),('128 GB','128 GB'),('256 GB','256 GB'),('512 GB','512 GB'),('1 TB','1 TB')],max_length=6)

class laptops(models.Model):
    Item = models.ForeignKey(Product,on_delete=models.CASCADE)
    Ram = models.IntegerField()
    Brand = models.CharField(choices=laptops_brand,max_length=12)
    Storage = models.CharField(choices=[('128 GB','128 GB'),('256 GB','256 GB'),('512 GB','512 GB'),('1 TB','1 TB')],max_length=6)
    Storage_type = models.CharField(choices=[('SSD','SSD'),('HDD','HDD')], max_length=3)