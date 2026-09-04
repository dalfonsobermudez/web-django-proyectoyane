from django.urls import path

from proyectoyaneshop import views

urlpatterns = [
    path("", views.shop, name="Shop"),
    path(
        "category/<slug:category_slug>/",
        views.category_products,
        name="ProductsByCategory",
    ),
    path("<str:product_slug>/", views.product_details, name="ProductDetails"),
]
