from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request, 'core/index.html')

def UserLogin(request):
   return render(request, 'accounts/login.html')