from datetime import timezone, datetime
from difflib import context_diff
from itertools import product

from django.contrib.messages.context_processors import messages
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages

from app.models import Category, Product, Comment, Order
from django.db import models
from .forms import CommentForm, OrderForm


# Create your views here.


def shop_index(request, category_slug=None):
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(Q(name__icontains=search))
    else:
        categories = Category.objects.all()
        products = Product.objects.all()
        if category_slug:
            products = products.filter(category__slug=category_slug)
            pass

    context = {
        'products': products,
        'categories': categories,
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


def products_detail(request, slug):
    products = Product.objects.get(slug=slug)
    product = get_object_or_404(Product, slug=slug)
    context = {
        'products': products,
        'product': product
    }
    return render(request, 'app/detail.html', context)


# def product_list(request, slug):
#     product = Product.objects.get(slug=slug)
#     context = {'products': product}
#     return render(request, 'app/detail.html', context)

def add_comment(request, slug):
    order = get_object_or_404(Order, slug=slug)
    comments = Comment.objects.filter(order=order)
    new_comment = None

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.order = order
            new_comment.save()
            return redirect('products_detail', slug=slug)
    else:

        form = CommentForm()
        context = {
            'form': form,
            'order': order,
            'comments': comments,
            'new_comment': new_comment
        }
    return render(request,'app/detail.html', context)