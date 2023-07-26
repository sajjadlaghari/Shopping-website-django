from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import authenticate,  logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    return render(request,'admin/index.html')

def login(request):
    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = authenticate(username=email, password=password)

        if user_obj:
            django_login(request, user_obj)  # Use login() to log in the user
            return redirect('/admin')

        messages.warning(request,'Invalid credentials')
        return HttpResponseRedirect(request.path_info)

    return render(request,'admin/login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')            
        last_name = request.POST.get('lname')            
        email = request.POST.get('email')           
        password = request.POST.get('password')  
        user_obj = User.objects.filter(email=email).exists()

            
        if user_obj:
            messages.warning(request,'Email already Taken')
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(first_name = first_name, last_name = last_name, email = email, username = email)
        user_obj.set_password(password)
        user_obj.save()     
            
        messages.warning(request,'Your account created successfully')
        return redirect('/admin/login')
    else:

        return render(request,'admin/register.html')
@login_required
def products(request):
    return render(request,'admin/products.html')

@login_required
def add_products(request):
    return render(request,'admin/add-product.html')

@login_required
def add_category(request):
    return render(request,'admin/add-category.html')



@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/admin/login")