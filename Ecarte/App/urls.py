from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from Ecarte.settings import MEDIA_ROOT, STATICFILES_DIRS

urlpatterns = [
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('account',views.account, name = 'userAccount'),
    path('collection/<str:category>',views.collection,name='collection'),
    path('productdetails/<int:pk>',views.prdetails.as_view(),name='product-details')

]