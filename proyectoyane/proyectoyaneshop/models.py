from django.db import models
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    details = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def save(self, *args, **kwargs):
        # Si el slug no ha sido ingresado manualmente,
        # se genera a partir del nombre
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
