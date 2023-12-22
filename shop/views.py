from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
# Create your views here.
def show_items(request):
    items = Product.objects.all()

    paginator = Paginator(items, 4)
    page_num = request.GET.get('page')
    item_object = paginator.get_page(page_num)
    return render(request, 'shop/index.html', {"items":item_object})