from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Admin.models import Slider
from Admin.models import Product
from Admin.models import Cart

def home(request):

    sliders = Slider.objects.all()

    products = Product.objects.all().order_by('-created_at')
    return render(request,'index.html',{'sliders':sliders,'products':products})



def product_detailed(request,id):

    product = Product.objects.get(pk = id)
    return render(request,'product-detail.html',{'product':product})

@login_required
def add_to_cart(request):
    
    product = Product.objects.get(pk = request.POST.get('id'))
    cart = Cart.objects.get(product = request.POST.get('id'))
    if cart:

        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        price = float(price)
        quantity = int(quantity)

        price = price * quantity

        cart.quantity += quantity
        cart.price += price

        cart.save()

    else:

        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        price = float(price)
        quantity = int(quantity)

        price = price * quantity

        current_user = request.user
        cart = Cart()

        cart.product = product
        cart.user = current_user
        cart.quantity = quantity
        cart.price = price
        cart.save()

    product = Product.objects.get(pk = request.POST.get('id'))

    return render(request,'product-detail.html',{'product':product})



def shop(request):
    return render(request,'shops.html')