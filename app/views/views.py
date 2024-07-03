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
from app.forms import CommentForm, OrderForm


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
    product = Product.objects.get(slug=slug)
    related_product = Product.objects.filter(slug=slug)
    comments = Comment.objects.filter(product__slug=slug)
    comment_form = CommentForm()
    order_form = OrderForm()
    new_comment = None
    new_order = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        order_form = OrderForm(data=request.POST)
        if comment_form.is_valid() and order_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()

        elif order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.product = product
            new_order.save()
            messages.add_message(
                request, messages.SUCCESS,'Product added successfully!')

    return render(request, 'app/detail.html',
                  {'product': product,
                           'new_comment': new_comment,
                           'order_form': order_form, 'comment_form': comment_form,
                           'new_order': new_order,
                           'comments': comments,
                           'related_product': related_product})
