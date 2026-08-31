from django.contrib import admin

from .models import Product, ProductCategory


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'created', 'updated')


class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'created', 'updated')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
