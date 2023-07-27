from django.shortcuts import render
from Admin.models import Slider
def home(request):

    sliders = Slider.objects.all()
    return render(request,'index.html',{'sliders':sliders})

def shop(request):
    return render(request,'shops.html')