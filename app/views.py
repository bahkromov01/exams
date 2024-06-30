from django.shortcuts import render

from app.models import Category, Product


# Create your views here.


def shop_index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'app/home.html', context)


def products_list(request, product_id):
    category = Product.objects.get(id=product_id)
    context = {
        'category': category ,
    }
    return render(request, 'app/detail.html', context)