from django.shortcuts import render
from django import views
from TshirtApp.models import Catagory,Tshirts,Orders



def home(request):
    tshirts=Tshirts.objects.all()
    return render(request,'home.html')



