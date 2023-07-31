from rest_framework.decorators import api_view
from rest_framework.response import Response
from Admin.models import Slider
from Admin.models import Product
from Admin.models import Cart
from .serializers import SliderSerializer
from .serializers import ProductSerializer

@api_view(['GET'])
def sliders(request):

    sliders = Slider.objects.all()
    serializer = SliderSerializer(sliders, many=True)
    return Response({'status':200, 'data':serializer.data})

@api_view(['GET'])
def products(request):

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response({'status':200, 'data':serializer.data})
