from django.urls import path

from proyectoyaneblog import views

urlpatterns = [
    path('', views.blog, name="Blog"),
]
