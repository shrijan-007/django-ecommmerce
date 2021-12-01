# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse,request
from App import models
from App.models import Product, phones, shirts,Customer
from django.views import View
from . import forms
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
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



# def account(request):
#     fm = forms.userRegistrationForm()
#     return render(request,'app/registration.html',{'form':fm})

def userArea(request):
    if request.user.is_authenticated:
        customer_ = Customer.objects.filter(user = request.user.id)
        return render(request,'app/Account.html',{"customer":customer_})
    else:
        return HttpResponse('<h1>NOT Authorized</h1>')

def Cust_orders(request):
    return render(request,'app/userOrders.html')

class set_newPass(View):
    def get(self,request):
        fm = forms.changeUserPass(user=request.user)
        return render(request,'app/changePass.html',{'form':fm})
    def post(self,request):
        fm = forms.changeUserPass(user = request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request,'Your password is changed succefully !')
            return render(request,'app/changePass.html',{'form':fm})
        else:
            messages.warning(request,'something went wrong')
            return render(request,'app/changePass.html',{'form':fm})
class account(View):
    def get(self,request):
        fm = forms.userRegistrationForm()
        return render(request,'app/registration.html',{'form':fm})
    def post(self,request):
        fm =forms.userRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request,'app/home.html')
        else:
            return render(request,'app/registration.html',{'form':fm})

class address(View):
    def get(self,request):
        customer_ = Customer.objects.filter(user = request.user.id)
        fm = forms.customers_Adress()
        return render(request,'app/address.html',{'form':fm,"customer":customer_})
    def post(self,request):
        customer_ = Customer.objects.filter(user = request.user.id)
        fm = forms.customers_Adress(request.POST)
        if fm.is_valid():
            fname = fm.cleaned_data['fname']
            lname = fm.cleaned_data['lname']
            addr = fm.cleaned_data['address']
            phno = fm.cleaned_data['phoneNo']
            state = fm.cleaned_data['state']
            pincode = fm.cleaned_data['pincode']
            Customer.objects.create(user = User.objects.filter(id = request.user.id).get(),Fname = fname,Lname = lname,PhoneNo = phno,Address = addr,State = state,Pincode = pincode)
            messages.success(request,'Address saved Successfully')
            fm = forms.customers_Adress()
            return render(request,'app/address.html',{'form':fm,"customer":customer_})
        else:
            return render(request,'app/address.html',{'form':fm,"customer":customer_})


class prdetails(View):
    def get(self,request,pk):
        requested_product = Product.objects.filter(id = pk).get()
        if requested_product.Category == "smartphone":
            item = phones.objects.filter(Item = pk).get()
            product_model = item.Item_model
            colors = phones.objects.filter(Item_model = product_model).filter(Ram = item.Ram).filter(Storage = item.Storage).distinct()
            return render(request,'app/product-page.html',{'item':item,'colors':colors})
        if requested_product.Category == "shirt":
            item = shirts.objects.filter(Item = pk).get()
            return render(request,'app/product-page.html',{'item':item,'title':'ss'})