from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.



def dashboard(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'dashboard.html', context)

def about(request):
    return render(request, 'about.html')

def support(request):
    return render(request, 'support.html')

def product(request,product_id):
    product_ = get_object_or_404(Product, id=product_id)
    return render(request, 'product.html',{'product':product_})

def categories(request):
    categories = Product.CATEGORY
    return render(request, 'categories.html', {'categories': categories})

def category1(request):
    products = Product.objects.filter(categories='category1')
    return render(request, 'category1.html', {'products': products})

def category2(request):
    products = Product.objects.filter(categories='category2')
    return render(request, 'category2.html', {'products': products})

def category3(request):
    products = Product.objects.filter(categories='category3')
    return render(request, 'category3.html', {'products': products})

def category4(request):
    products = Product.objects.filter(categories='category4')
    return render(request, 'category4.html', {'products': products})