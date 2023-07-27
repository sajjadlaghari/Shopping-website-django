from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('',views.index),
    path('login',views.login),
    path('register',views.register),
    path('products-cart',views.products_cart),
    path('products',views.products),
    path('add-product',views.add_products),
    path('logout',views.custom_logout),

    path('categories',views.categories),
    path('add-category',views.add_category),
    path('edit-category/<int:id>', views.edit_category),
    path('update-category', views.update_category),
    path('delete-category/<int:id>', views.delete_category),


    # path('sliders',views.slider),
    # path('add-slider',views.add_slider),

    # path('shop/',views.shop)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)