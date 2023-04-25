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

def oil_painting(request):
    products = Product.objects.filter(categories='Oil-Painting')
    return render(request, 'Oil-Painting.html', {'products': products})

def Watercolors(request):
    products = Product.objects.filter(categories='Watercolors')
    return render(request, 'Watercolors.html', {'products': products})

def Dry_Crayons(request):
    products = Product.objects.filter(categories='Dry-Crayons')
    return render(request, 'Dry-Crayons.html', {'products': products})

def Oil_Crayons(request):
    products = Product.objects.filter(categories='Oil-Crayons')
    return render(request, 'Oil-Crayons.html', {'products': products})

def handler404(request, exception):
    return render(request, '404.html', status=404)