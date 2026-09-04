from django.urls import path

from proyectoyaneblog import views

urlpatterns = [
    path("", views.blog, name="Blog"),
    path(
        "category/<slug:category_slug>/",
        views.category_posts,
        name="PostsByCategory",
    ),
    path("<slug:post_slug>/", views.post_detail, name="PostDetail"),
]
