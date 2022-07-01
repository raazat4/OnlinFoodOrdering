from django.urls import path
from order import views

urlpatterns = [
   path('menu', views.menu, name='menu'),
   path('order', views.order, name='order'),   
]