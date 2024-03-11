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
       try:
         cust=Customer.objects.get(username=username,password=password)
         request.session['customer']=cust.id
         return redirect('customer:index')
       except Customer.DoesNotExist:    
         return render(request,'login.html',{'msg':'invalid'})
    return render(request,'login.html')

def logout(request):
   if 'customer' in request.session:
      del request.session['customer']
      return redirect('customer:login')
   else:
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
    cat=Category.objects.get(name='men')
    pdt=Product.objects.filter(category=cat)
    return render(request,'men.html',{'products':pdt})

def women(request):
    cat=Category.objects.get(name='women')
    pdt=Product.objects.filter(category=cat)
    return render(request,'women.html',{'products':pdt})
    

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def cart(request):
   return render(request,'cart.html')

def payment(request):
   return render(request,'payment.html')

