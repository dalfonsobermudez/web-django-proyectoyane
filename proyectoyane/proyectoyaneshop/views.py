from django.shortcuts import render, get_object_or_404

from proyectoyaneshop.models import Product, ProductCategory


# Create your views here.
def shop(request):
    # Mostrar solo productos activos
    products = Product.objects.filter(is_active=True)
    # Lista de categorias para el menú superior
    categories = ProductCategory.objects.all()
    return render(
        request,
        "proyectoyaneshop/shop.html",
        {"products": products, "categories": categories},
    )


def product_details(request, product_slug: str):
    product = get_object_or_404(Product, slug=product_slug)
    categories = ProductCategory.objects.all()
    return render(
        request,
        "proyectoyaneshop/product_details.html",
        {"product": product, "categories": categories},
    )


def category_products(request, category_slug: str):
    # Obtener la categoría por slug o devolver 404
    category = get_object_or_404(ProductCategory, slug=category_slug)
    # Productos activos de la categoría
    products = Product.objects.filter(category=category, is_active=True)
    # También pasar la lista completa de categorías para el menú
    categories = ProductCategory.objects.all()
    return render(
        request,
        "proyectoyaneshop/category_products.html",
        {"products": products, "category": category, "categories": categories},
    )
