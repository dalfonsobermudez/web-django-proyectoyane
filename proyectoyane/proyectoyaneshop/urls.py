from django.urls import path

from proyectoyaneshop import views

urlpatterns = [
    path('', views.shop, name="Shop"),
    path('<str:product_slug>/', views.product_details, name="ProductDetails"),

]
