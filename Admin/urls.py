from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('',views.index),
    path('login',views.login),
    path('register',views.register),
    path('products-cart',views.products_cart),
    path('logout',views.custom_logout),

    
    path('products',views.products),
    path('add-product',views.add_products),
    path('edit-product/<int:id>',views.edit_product),
    path('update-product',views.update_product),
    path('delete-product/<int:id>',views.delete_products),


    path('categories',views.categories),
    path('add-category',views.add_category),
    path('edit-category/<int:id>', views.edit_category),
    path('update-category', views.update_category),
    path('delete-category/<int:id>', views.delete_category),


    path('sliders',views.slider),
    path('add-slider',views.add_slider),

    path('edit-slider/<int:id>', views.edit_slider),
    path('update-slider', views.update_slider),
    path('delete-slider/<int:id>', views.delete_slider),

    # path('shop/',views.shop)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)