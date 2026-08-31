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


def product_details(request, product_slug: str):
    product = Product.objects.get(slug=product_slug)
    return render(
        request,
        "proyectoyaneshop/product_details.html",
        {"product": product},
    )
