from django.shortcuts import render
from .static_data import products

def product_list(request):
    context = {
        'products': products
    }
    return render(request, 'product/product_list.html', context)

def product_detail(request, product_id): 
    product = None
    for p in products:
        if p['id'] == product_id: 
            product = p
            break
    
    context = {
        'product': product
    }
    return render(request, 'product/product_detail.html', context)