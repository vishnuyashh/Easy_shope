from django.shortcuts import render ,redirect
from seller.models import *
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
       email=request.POST['email']
       password=request.POST['password']
       try:
         cust=Customer.objects.get(email=email,password=password)
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

def masterpage1(request):
    return render(request,'masterpage1.html')

def men(request):
   if 'customer' in request.session:
    cat=Category.objects.get(name='men')
    pdt=Product.objects.filter(category=cat)
    return render(request,'men.html',{'products':pdt})
   else:
      return redirect('customer:login')

def women(request):
   if 'customer' in request.session:
    cat=Category.objects.get(name='women')
    pdt=Product.objects.filter(category=cat)
    return render(request,'women.html',{'products':pdt})
   else:
      return redirect('customer:login')
    

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def cart(request):
   cart_items=Cart.objects.all()
   total_price=sum(item.product.price*item.quantity for item in cart_items)
   total_price_per_item=[]
   grand_total=0
   for item in cart_items:
      item_total=item.product.price*item.quantity
      total_price_per_item.append({'item':item,'total':'item_total'})
      grand_total+=item_total    
   return render(request,'cart.html',{'cart_items':cart_items,'grand_total':grand_total,'total_price':total_price})

def add_to_cart(request,product_id):
   if request.method=='POST':
      product=Product.objects.get(id=product_id)
      cart_item,created=Cart.objects.get_or_create(product=product)
      if not created:
         cart_item.quantity+=1
         cart_item.save()
   return redirect('customer:cart')

def remove_from_cart(request,product_id):
   product=Product.objects.get(id=product_id)
   cart_item=Cart.objects.get(product=product)
   cart_item.delete()
   return redirect('customer:cart')


def payment(request):
   return render(request,'payment.html')

def wishlist(request):
   wishlist_item=Wishlist.objects.all()
   return render(request,'wishlist.html',{'wishlist_item':wishlist_item})


def add_to_wishlist(request,products_id):
   if request.method=='POST':
      pdt=Product.objects.get(id=products_id)
      wishlist,created=Wishlist.objects.get_or_create(products=pdt)
      wishlist.save()
      
     
      return redirect('customer:wishlist')
   

def remove_from_wishlist(request,products_id):
   product=Product.objects.get(id=products_id)
   wishlist_item=Wishlist.objects.get(products=product)
   wishlist_item.delete()
   return redirect('customer:wishlist')

def profile(request):
   if 'customer' in request.session:
    cust_id=request.session.get('customer') 
    cust=Customer.objects.get(id=cust_id)
        
    return render(request,'profile.html',{'customer':cust})

