from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import authenticate,  logout
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import *
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
def products_cart(request):
    return render(request,'admin/products-cart.html')

@login_required
def products(request):
    return render(request,'admin/products.html')


@login_required
def slider(request):

    sliders = Slider.objects.all()

    return render(request,'admin/slider.html',{'sliders':sliders})

@login_required
def add_slider(request):
    
    if request.method == "POST":
        title = request.POST.get('title')            
        description = request.POST.get('description')

        upload = request.FILES.get('slider_image')
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)            
       
        obj = Slider.objects.create(title = title, description = description, image = file_url)
            
        file_items = Slider.objects.all()

        for item in file_items:
            # Removing the leading forward slash from the "media" folder
            file_name = item.image.name.lstrip("/")
            item.image.name = file_name
            item.save()   
        messages.warning(request,'Your account created successfully')
        return redirect('/admin/sliders')
    
    else:
        return render(request,'admin/add-slider.html')





@login_required
def add_products(request):

    if request.method == "POST":
        title = request.POST.get('title')            
        price = request.POST.get('price')            
        location = request.POST.get('location')            
        description = request.POST.get('description')

        upload = request.FILES.get('featured_image')
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        featured_image = fss.url(file)            
       
        obj = Product.objects.create(title = title, description = description, image = file_url)
            
        file_items = Slider.objects.all()

        for item in file_items:
            # Removing the leading forward slash from the "media" folder
            file_name = item.image.name.lstrip("/")
            item.image.name = file_name
            item.save()   
        messages.warning(request,'Your account created successfully')
    
    else:
            
        return render(request,'admin/add-product.html')

@login_required
def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')            
     

        upload = request.FILES.get('image')
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)            
       
        obj = Category.objects.create(name = name, image = file_url)
            
        file_items = Category.objects.all()

        for item in file_items:
            # Removing the leading forward slash from the "media" folder
            file_name = item.image.name.lstrip("/")
            item.image.name = file_name
            item.save()   
        messages.warning(request,'Category created successfully')
        return redirect('/admin/categories')
    
    else:
        return render(request,'admin/add-category.html')

@login_required
def categories(request):

    categories = Category.objects.all()

    return render(request,'admin/categories.html',{'categories':categories})

@login_required
def edit_category(request,id):

    category =Category.objects.get(pk = id)

    return render(request,'admin/edit-category.html',{'category':category})

@login_required
def update_category(request):
    if request.method == "POST":
        id = request.POST.get('id')            


        category = Category.objects.get(id=id)

        if request.method == "POST":
           name = request.POST.get('name')
           upload = request.FILES.get('image')

        if upload:
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
            category.image = file_url


        # If no new image is selected, keep the existing image

        category.name = name
        category.save()

        file_items = Category.objects.all()

        for item in file_items:
            # Removing the leading forward slash from the "media" folder
            file_name = item.image.name.lstrip("/")
            item.image.name = file_name
            item.save()   
        messages.success(request,'Category Updated successfully')
        return redirect('/admin/categories')
    

@login_required
def delete_category(request,id):
    Category.objects.filter(id=id).delete()

    messages.warning(request,'Category Deleted successfully')
    return redirect('/admin/categories')
    



@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/admin/login")