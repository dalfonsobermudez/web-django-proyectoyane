from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class PostCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CategoriaPost"
        verbose_name_plural = "CategoriasPost"

    def save(self, *args, **kwargs):
        # Si el slug no ha sido ingresado manualmente,
        # se genera a partir del nombre
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

        def __str__(self) -> str:
            return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blogs/", null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def save(self, *args, **kwargs):
        # Si el slug no ha sido ingresado manualmente,
        # se genera a partir del nombre
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
