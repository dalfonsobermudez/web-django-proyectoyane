from django.shortcuts import render

from proyectoyaneshop.models import Product


# Create your views here.
def shop(request):
    products = Product.objects.all()
    return render(
        request,
        "proyectoyaneshop/shop.html",
        {"products": products},
    )
