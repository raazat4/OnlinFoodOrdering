from django.urls import path
from accounts import views

urlpatterns = [
   path('login', views.UserLogin, name='UserLogin'),
   path('login', views.UserLogin, name='UserLogin'),
   
]