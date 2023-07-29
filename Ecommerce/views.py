from django.shortcuts import render
from Admin.models import Slider
from Admin.models import Product

def home(request):

    sliders = Slider.objects.all()

    products = Product.objects.all().order_by('-created_at')
    return render(request,'index.html',{'sliders':sliders,'products':products})



def product_detailed(request,id):

    product = Product.objects.get(pk = id)
    return render(request,'product-detail.html',{'product':product})


def shop(request):
    return render(request,'shops.html')