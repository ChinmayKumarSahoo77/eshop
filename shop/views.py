from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product
from django.contrib import messages

# Create your views here.
def show_items(request):
    items = Product.objects.all().order_by('title')
    
    search_val = request.GET.get('search')
    if search_val != "" or search_val is not None:
        items = items.filter(title__icontains = search_val)

    paginator = Paginator(items, 4)
    page_num = request.GET.get('page')
    item_object = paginator.get_page(page_num)
    return render(request, 'shop/index.html', {"items":item_object})


def detail_view(request, id: int):
    item_obj = Product.objects.get(id = id)
    
    messages.success(request, f"Item details with id {id} fetched successfully.")
    return render(request, 'shop/details.html', {'item_obj':item_obj})