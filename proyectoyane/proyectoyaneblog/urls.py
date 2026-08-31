from django.urls import path

from proyectoyaneblog import views

urlpatterns = [
    path('', views.blog, name="Blog"),
    # TODO Crear URL de detalles del Post
    # TODO Crear URL para filtrar Posts por Categoria
]
