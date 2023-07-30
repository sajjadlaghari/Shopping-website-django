from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns =[
    path('',views.home),
    path('shop/',views.shop),
    path('product_detailed/<int:id>',views.product_detailed),
    path('add-to-cart',views.add_to_cart)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)