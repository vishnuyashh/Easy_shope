from django.shortcuts import render ,redirect
from seller.models import *
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']
       if Customer.objects.filter(username=username,password=password).exists():
        return redirect('customer:index')
       else:

         return render(request,'login.html',{'msg':'invalid'})
    return render(request,'login.html')

def register(request):
   
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']
       email=request.POST['email']
       cust=Customer(username=username,password=password,email=email)
       cust.save()
       return redirect('customer:login')
    return render(request,'register.html')

def masterpage(request):
    return render(request,'masterpage.html')

def men(request):
    return render(request,'men.html')

def women(request):
    return render(request,'women.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

