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

    products = Product.objects.all().order_by('-created_at')[:4]
    return render(request,'admin/index.html',{'products':products})

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
    products = Product.objects.all().order_by('-created_at')

    return render(request,'admin/products-cart.html',{'products':products})


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
        messages.success(request,'Slider created successfully')
        return redirect('/admin/sliders')
    
    else:
        return render(request,'admin/add-slider.html')

@login_required
def edit_slider(request,id):

    slider = Slider.objects.get(pk = id)

    return render(request,'admin/edit-slider.html',{'slider':slider})

@login_required
def update_slider(request):
    if request.method == "POST":
        id = request.POST.get('id')     
       
        slider = Slider.objects.get(id=id)

        if request.method == "POST":
            title = request.POST.get('title')            
            status = request.POST.get('status')
            description = request.POST.get('description')
            upload = request.FILES.get('slider_image')       

        if upload:
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
            slider.image = file_url

        if status:
            slider.status = status

        # If no new image is selected, keep the existing image

        slider.title = title
        slider.description = description
        slider.save()

        file_items = Slider.objects.all()

        for item in file_items:
            # Removing the leading forward slash from the "media" folder
            file_name = item.image.name.lstrip("/")
            item.image.name = file_name
            item.save()   
        messages.success(request,'Slider Updated successfully')
        return redirect('/admin/sliders')
    

@login_required
def delete_slider(request,id):
    Slider.objects.filter(id=id).delete()

    messages.success(request,'Slider Deleted successfully')
    return redirect('/admin/sliders')
    


# Product Routes

@login_required
def products(request):
    products = Product.objects.all().order_by('-created_at')

    return render(request,'admin/products.html',{'products':products})

@login_required
def add_products(request):

    if request.method == "POST":
        title = request.POST.get('title')            
        price = request.POST.get('price')            
        category_id = request.POST.get('category')            
        location = request.POST.get('location')            
        description = request.POST.get('description')

        upload = request.FILES.get('featured_image')
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        featured_image = fss.url(file)   

        current_user = request.user

        category =  Category.objects.get(id = category_id)
              
       
        obj = Product.objects.create(user = current_user , category = category,name = title, description = description, location = location, price=price, fearured_image = featured_image)
            

        file_items = Product.objects.all()

        for item in file_items:
            # Removing the leading forward slash from the "media" folder
            file_name = item.fearured_image.name.lstrip("/")
            item.fearured_image.name = file_name
            item.save()   

        
        product = Product.objects.get(id=obj.id)

        images = request.FILES.getlist('images')

        for image in images:
           fss = FileSystemStorage()
           file = fss.save(image.name, image)
           attch = fss.url(file)

           productImage = ProductImage()

           productImage.product = product
           productImage.image = attch

           productImage.save()

        file_items = ProductImage.objects.all()

        for item in file_items:
            # Removing the leading forward slash from the "media" folder
            file_name = item.image.name.lstrip("/")
            item.image.name = file_name
            item.save()
        messages.success(request,'Product created successfully')
        products = Product.objects.all().order_by('-created_at')
        return render(request,'admin/products.html',{'products':products})
    
    else:
        categories = Category.objects.all()
        return render(request,'admin/add-product.html',{'categories':categories})


@login_required
def edit_product(request,id):
    product = Product.objects.get(pk = id)
    categories = Category.objects.all()

    return render(request,'admin/edit-product.html',{'product':product,'categories':categories})




def update_product(request):
     
     if request.method == "POST":
        id = request.POST.get('id')     
        product = Product.objects.get(id=id)

        title = request.POST.get('title')            
        price = request.POST.get('price')            
        category_id = request.POST.get('category')            
        location = request.POST.get('location')            
        description = request.POST.get('description')

        upload = request.FILES.get('featured_image')
        
        current_user = request.user

        category =  Category.objects.get(id = category_id)

        if upload:
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            featured_image = fss.url(file)  
            product.fearured_image = featured_image


        product.user = current_user
        product.category = category
        product.name = title
        product.description = description
        product.location = location
        product.price = price
       
        product.save()

        file_items = Product.objects.all()

        for item in file_items:
            # Removing the leading forward slash from the "media" folder
            file_name = item.fearured_image.name.lstrip("/")
            item.fearured_image.name = file_name
            item.save()   

        
        product = Product.objects.get(id=product.id)

        images = request.FILES.getlist('images')

        if images:
            for image in images:
                fss = FileSystemStorage()
                file = fss.save(image.name, image)
                attch = fss.url(file)

                productImage = ProductImage()

                productImage.product = product
                productImage.image = attch

                productImage.save()

                file_items = ProductImage.objects.all()

            for item in file_items:
                # Removing the leading forward slash from the "media" folder
                file_name = item.image.name.lstrip("/")
                item.image.name = file_name
                item.save()
        messages.success(request,'Product Updated successfully')
        return redirect('/admin/products')



@login_required
def delete_products(request,id):
    Product.objects.filter(id=id).delete()

    messages.success(request,'Product Deleted successfully')
    return redirect('/admin/products')
   



#  category views


@login_required
def categories(request):

    categories = Category.objects.all()

    return render(request,'admin/categories.html',{'categories':categories})

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
        messages.success(request,'Category created successfully')
        return redirect('/admin/categories')
    
    else:
        return render(request,'admin/add-category.html')


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
    

#  category views Ended Here

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/admin/login")