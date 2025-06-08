from django.shortcuts import render

from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, 'shop/product_detail.html', {'product': product})