from django.contrib import admin

from proyectoyaneblog.models import Post, PostCategory


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'created', 'updated')


class PostCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'created', 'updated')


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
