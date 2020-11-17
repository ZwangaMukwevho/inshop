from django.shortcuts import render
from .models import shop

# Create your views here.
def home(request):
    shops = shop.objects
    return render(request, 'landingpage/home.html',{'shops':shops})