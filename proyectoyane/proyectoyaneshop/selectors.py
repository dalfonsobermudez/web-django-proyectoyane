from proyectoyaneshop.models import Product, ProductCategory


def get_active_products():
    return Product.objects.filter(is_active=True).select_related("category")


def get_active_product(product_slug: str):
    return get_active_products().filter(slug=product_slug, is_active=True)


def get_active_products_by_category(category: ProductCategory):
    return get_active_products().filter(category=category)
