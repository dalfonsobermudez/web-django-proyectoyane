from urllib.parse import quote

from django.conf import settings
from django.shortcuts import get_object_or_404, render

from proyectoyaneshop.models import ProductCategory
from proyectoyaneshop.selectors import (
    get_active_product,
    get_active_products,
    get_active_products_by_category,
)


# Create your views here.
def shop(request):
    products = get_active_products()
    # Lista de categorias para el menú superior
    categories = ProductCategory.objects.all()
    return render(
        request,
        "proyectoyaneshop/shop.html",
        {"products": products, "categories": categories},
    )


def product_details(request, product_slug: str):
    product = get_object_or_404(get_active_product(product_slug))
    categories = ProductCategory.objects.all()
    whatsapp_url = ""
    if settings.WHATSAPP_NUMBER:
        message = f"Hola, quisiera consultar por el producto {product.name}."
        whatsapp_url = (
            f"https://wa.me/{settings.WHATSAPP_NUMBER}?text={quote(message)}"
        )
    return render(
        request,
        "proyectoyaneshop/product_details.html",
        {
            "product": product,
            "categories": categories,
            "whatsapp_url": whatsapp_url,
        },
    )


def category_products(request, category_slug: str):
    # Obtener la categoría por slug o devolver 404
    category = get_object_or_404(ProductCategory, slug=category_slug)
    # Productos activos de la categoría
    products = get_active_products_by_category(category)
    # También pasar la lista completa de categorías para el menú
    categories = ProductCategory.objects.all()
    return render(
        request,
        "proyectoyaneshop/category_products.html",
        {"products": products, "category": category, "categories": categories},
    )
