from django.shortcuts import render

# Create your views here.
def menu(request):
   return render(request, 'order/menu.html')

def order(request):
   return render(request, 'order/order.html')