
from django.db.models import Max, Min
from django.shortcuts import render, get_object_or_404, redirect

from django.db import models
from app.models import Product


def about_page(request):
    return render(request, 'about/about.html')