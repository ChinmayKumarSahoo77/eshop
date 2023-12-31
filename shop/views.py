from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Order
from django.contrib import messages


# Create your views here.
def show_items(request):
    items = Product.objects.all().order_by("title")

    # Search functionality
    search_val = request.GET.get("search")

    if search_val != "" and search_val is not None:
        items = items.filter(title__icontains=search_val)

    # Pagination functionality
    paginator = Paginator(items, 4)
    page_num = request.GET.get("page")
    item_object = paginator.get_page(page_num)
    return render(request, "shop/index.html", {"items": item_object})


def detail_view(request, id: int):
    item_obj = Product.objects.get(id=id)

    messages.success(request, f"Item details with id {id} fetched successfully.")
    return render(request, "shop/detail.html", {"item_obj": item_obj})


def checkout(request):
    if request.method == "POST":
        items = request.POST.get("items", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zipcode = request.POST.get("zipcode", "")
        total = request.POST.get("total", "")
        
        order = Order(
            items=items,
            name=name,
            email=email,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            total=total,
        )
        order.save()

    return render(request, "shop/checkout.html")
