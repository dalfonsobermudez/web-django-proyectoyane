from django.urls import path

from proyectoyanecontact import views

urlpatterns = [
    path('', views.contact, name="Contact"),
]
