from datetime import timezone, datetime
from difflib import context_diff
from itertools import product

from django.contrib.auth.decorators import login_required
from django.contrib.messages.context_processors import messages
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages

from app.models import Category, Product, Comment, Order
from django.db import models
from app.forms import CommentModelForm, OrderModelForm

@login_required(login_url='http://127.0.0.1:8000/admin/login/?next=/admin/')

# Create your views here.


def shop_index(request, category_slug=None):
    categories = Category.objects.all()
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(Q(name__icontains=search))
    else:
        products = Product.objects.all()
    if category_slug:
        products = products.filter(category__slug=category_slug)
    filter_expensive = request.GET.get('expensive')
    filter_cheap = request.GET.get('cheap')
    if filter_expensive:
        products = products.order_by('-price')[:3]
    elif filter_cheap:
        products = products.order_by('price')[:3]
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'app/home.html', context)


def category_index(request, category_slug=None):
    categories = Category.objects.all()
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
        context = {
            'categories': categories,
            'products': products
        }
        return render(request, 'app/home.html', context)


def products_detail(request, product_slug):
    products = Product.objects.get(slug=product_slug)
    product = get_object_or_404(Product, slug=product_slug)
    comments = product.comments.filter(is_possible=True)
    context = {
        'products': products,
        'product': product,
        'comments': comments
    }
    return render(request, 'app/detail.html', context)




def add_comment(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.product = product
            comment.save()
            print('Save Done ! ')
            return redirect('products_detail', product_slug)
    else:
        form = CommentModelForm(request.GET)
        print('Get method running')

    return render(request, 'app/detail.html', {'form': form, 'product': product})


def add_order(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            messages.success(request, 'Your order is saved !')
            return redirect('products_detail', product_slug)
        else:
            form = OrderModelForm(request.POST)

        return render(request, 'app/detail.html', {'form': form, 'product': product})


