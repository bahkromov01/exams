from django.shortcuts import render

from app.models import Category, Product


# Create your views here.


def shop_index(request):
    return render(request, 'app/home.html')


def products_list(request, category_id):
    category = Category.objects.get(id=category_id)
    products = category.products.all()
    context = {
        'products': products,
    }
    return render(request, 'app/detail.html', context)