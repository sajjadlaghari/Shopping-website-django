from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Admin.models import Slider
from Admin.models import Product
from Admin.models import Cart

def home(request):

    sliders = Slider.objects.all()
    products = Product.objects.all().order_by('-created_at')

    # Check if the user is authenticated before accessing the cart
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
        cart_item_count = carts.count()
        print(cart_item_count)
    else:
        # If the user is not logged in, set carts and cart_item_count to None or 0
        carts = None
        cart_item_count = 0

    # Rest of your view logic goes here
    # ...

    return render(request, 'index.html', {
        'sliders': sliders,
        'products': products,
        'carts': carts,
        'cart_item_count': cart_item_count,
    })


def product_detailed(request,id):

    product = Product.objects.get(pk = id)
    # Check if the user is authenticated before accessing the cart
    if request.user.is_authenticated:
        cart_item_count = Cart.objects.filter(user=request.user).count()
        carts = Cart.objects.filter(user=request.user)
    else:
        # If the user is not logged in, set carts and cart_item_count to None or 0
        cart_item_count = 0
        carts = None

    return render(request, 'product-detail.html', {
        'carts': carts,
        'cart_item_count': cart_item_count,
        'product': product,
    })


@login_required
def add_to_cart(request):
    
    product_id = request.POST.get('id')
    quantity = int(request.POST.get('quantity'))
    price = float(request.POST.get('price'))

    product = Product.objects.get(pk=product_id)

    # Try to get the cart for the current user and product
    try:
        cart = Cart.objects.get(user=request.user, product=product)
    except Cart.DoesNotExist:
        cart = None

    if cart:
        cart.quantity += quantity
        cart.price += price * quantity
        cart.save()
    else:
        cart = Cart(user=request.user, product=product, quantity=quantity, price=price * quantity)
        cart.save()

    return render(request, 'product-detail.html', {'product': product})

@login_required
def view_cart(request):
    cart_item_count = Cart.objects.filter(user=request.user).count()
    carts = Cart.objects.filter(user = request.user)
    return render(request,'shoping-cart.html',{'carts':carts,'cart_item_count':cart_item_count})




def shop(request):
    return render(request,'shops.html')