from django.shortcuts import render
from django.http.response import JsonResponse
import json

from .models import Product


def index_page(request):
    return render(request, 'index.html')


# def


def get_products(request):
    products = list(Product.objects.all().values())
    for p in products:
        p['params'] = p['params'].split(',')
    return JsonResponse(products, safe=False)