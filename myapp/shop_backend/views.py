from .models import Product
from django.shortcuts import render
from django.db.models import Q

def product_list(request):
    search_query = request.GET.get('search','')
    
    if search_query:
        products = Product.objects.filter(name__icontains=search_query)
    else:
        products = Product.objects.all()

    return render(request, 'product_list.html', {'products': products})

def index(request):
    productcount = Product.objects.count()
    return render(request, 'index.html', {'productcount': productcount})

def info(request):
    productcount = Product.objects.count()
    return render(request, 'info.html', {'productcount': productcount})
def product_details(request, product_id):


    product = Product.objects.filter(id=product_id).first()
    return render(request, 'product_details.html', {'product': product})
