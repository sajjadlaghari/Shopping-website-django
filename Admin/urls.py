from django.urls import path

from . import views

urlpatterns =[
    path('',views.index),
    path('login',views.login),
    path('register',views.register),
    path('products',views.products),
    path('add-product',views.add_products),
    path('add-category',views.add_category),
    path('logout',views.custom_logout),
    # path('shop/',views.shop)
]