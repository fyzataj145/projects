from django.shortcuts import render
from cartApp.models import Product
# Create your views here.
def funcHome(request):
    elist=Product.objects.all()
    return render(request,'html/home.html',{'elist':elist})
def funcElectronic(request):
    elist=Product.objects.all()
    return render(request,'html/electronic.html',{'elist':elist})
def funcFashion(request):
     elist=Product.objects.all()
     return render(request,'html/fashion.html',{'elist':elist})
def funcGroceries(request):
     elist=Product.objects.all()
     return render(request,'html/groceries.html',{'elist':elist})