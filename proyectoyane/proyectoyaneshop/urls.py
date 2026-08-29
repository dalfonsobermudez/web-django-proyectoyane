from django.urls import path
from proyectoyaneshop import views

urlpatterns = [
    path('', views.shop, name="Shop"),
]
