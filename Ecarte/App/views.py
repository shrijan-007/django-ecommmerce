from django.shortcuts import render
from django.http import HttpResponse,request
from App import models
from App.models import Product, phones, shirts
from django.views import View
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def cart(request):
    return render(request, 'app/cart.html')


def collection(request,category):
    items = Product.objects.filter(Category = category).all()
    return render(request,'app/pr-collection.html',{'items':items,'title':category})

def phone_collection(request):

    items =Product.objects.all().filter(Category = "smartphone")
    return render(request,'app/pr-collection.html',{'items':items,'title':'Smartphone'})



def account(request):
    return HttpResponse("<h2 style = 'text-align:center; padding:12px 8px;'>Accounts</h2>")


class prdetails(View):
    def get(self,request,pk):
        requested_product = Product.objects.filter(id = pk).get()
        if requested_product.Category == "smartphone":
            item = phones.objects.filter(Item = pk).get()
            product_model = item.Item_model
            colors = phones.objects.filter(Item_model = product_model).filter(Ram = item.Ram).filter(Storage = item.Storage).distinct()
            return render(request,'app/product-page.html',{'item':item,'colors':colors})
        if requested_product.Category == "MFashion":
            item = shirts.objects.filter(Item = pk).get()
            return render(request,'app/product-page.html',{'item':item,'title':'ss'})