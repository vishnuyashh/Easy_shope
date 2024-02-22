from django.shortcuts import render ,redirect
from  seller.models import*
# Create your views here.
def s_index(request):
    return render(request,'seller/s_index.html')

def s_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if Seller.objects.filter(username=username,password=password).exists():
            return redirect('seller:s_index')
        else:
            return render(request,'s_login.html',{'msg':'invalid'})
    return render(request,'seller/s_login.html')

def s_register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        seller=Seller(username=username,password=password,email=email)
        seller.save()
    
    return render(request,'seller/s_register.html') 

def s_masterpage(request):
    
    return render(request,'seller/s_masterpage.html')

def addpdt(request):  
    cat=Category.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        quantity=request.POST['quantity']
        price=request.POST['price']
        image=request.FILES['image']
        
        category_id=request.POST.get('cat')
        category=Category.objects.get(id=category_id)
        pdt=Product(name=name,description=description,quantity=quantity,price=price,image=image,category=category)
        pdt.save()
    return render(request,'seller/addpdt.html',{'cat':cat})


def dashboard(request):
    pdt=Product.objects.all()
    return render(request,'seller/dashboard.html',{'product':pdt})

def remove(request,category_id):
    Product.objects.get(id=category_id).delete()
    return redirect('seller:dashboard')

def product_update(request,pid):
    cat=Category.objects.all()
    product=Product.objects.get(id=pid)
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        quantity=request.POST['quantity']
        price=request.POST['price']
        image=request.FILES['image']
        product.name=name
        product.description=description
        product.quantity=quantity
        product.price=price
        product.image=image

        product.save()
        return redirect('seller:dashboard')
    return render(request,'seller/product_update.html',{'i':product,
                                                        'cat':cat})
    





     
