from .models import Product
from django.shortcuts import render

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def index(request):
    productcount = Product.objects.count()
    return render(request, 'index.html', {'productcount': productcount})

def info(request):
    productcount = Product.objects.count()
    return render(request, 'info.html', {'productcount': productcount})
