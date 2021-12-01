from unicodedata import name
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path,include

from App.forms import loginForm
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from Ecarte.settings import MEDIA_ROOT, STATICFILES_DIRS

urlpatterns = [
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path("account/", views.userArea, name="Account"),
    path("customerAddress/",views.address.as_view(),name = 'custaddress'),
    path("account/changepassword",views.set_newPass.as_view(),name = 'custChangePass'),
    path('account/register',views.account.as_view(), name = 'userAccount'),
    path('collection/<str:category>',views.collection,name='collection'),
    path('productdetails/<int:pk>',views.prdetails.as_view(),name='product-details'),
    path("account/orders",views.Cust_orders, name="customerOrders"),
    path('account/login',auth_views.LoginView.as_view(
        template_name = 'app/LogForm.html',authentication_form=loginForm
    ),name = "account-login"),
    path('account/logout',auth_views.LogoutView.as_view(
        template_name = "app/home.html"
    ),name="account-logout"),

]