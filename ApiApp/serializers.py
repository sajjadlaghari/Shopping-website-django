from rest_framework import serializers
from Admin.models import Slider
from Admin.models import Product
from Admin.models import ProductImage
from Admin.models import Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Include the CategorySerializer for the category field
    images = ProductImageSerializer(many=True)
    user = UserSerializer()  # Include the UserSerializer for user data

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'location', 'price', 'fearured_image', 'status', 'created_at','updated_at','user','category','images')




