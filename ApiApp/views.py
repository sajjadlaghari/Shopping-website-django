from rest_framework.decorators import api_view
from rest_framework.response import Response
from Admin.models import Slider
from Admin.models import Product
from Admin.models import Cart
from .serializers import SliderSerializer
from .serializers import ProductSerializer
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import authenticate,  logout
from .serializers import UserSerializer
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

@api_view(['GET'])
def product_detailed(request,id):

    product = Product.objects.get(pk = id)
    serializer = ProductSerializer(product)
    return Response({'status':200, 'data':serializer.data})

@api_view(['POST'])
def login(request):
  

    email = request.data.get('username')
    password = request.data.get('password')

    user_obj = authenticate(email=email, password=password)

    if user_obj:

        django_login(request, user_obj)

    # Authenticate user using Django's built-in authentication
    user = authenticate(request=request, username=email, password=password)


    if user:
        user_serializer = UserSerializer(user)
        user_data = user_serializer.data
        # If user is authenticated, generate tokens
      
        return Response({
            'data': user_data,
            'status': 200,
        })
    else:
        return Response({
            
            'status': 300,
        })