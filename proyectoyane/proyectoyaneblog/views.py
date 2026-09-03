from django.shortcuts import get_object_or_404, render

from proyectoyaneblog.models import Post, PostCategory


# Create your views here.
def blog(request):
    posts = Post.objects.select_related('author', 'category').order_by('-created')
    categories = PostCategory.objects.all()
    return render(
        request,
        'proyectoyaneblog/blog.html',
        {'posts': posts, 'categories': categories},
    )


def post_detail(request, post_slug: str):
    post = get_object_or_404(
        Post.objects.select_related('author', 'category'),
        slug=post_slug,
    )
    return render(
        request,
        'proyectoyaneblog/post_detail.html',
        {'post': post},
    )


def category_posts(request, category_slug: str):
    category = get_object_or_404(PostCategory, slug=category_slug)
    posts = Post.objects.filter(category=category).select_related('author', 'category').order_by('-created')
    categories = PostCategory.objects.all()
    return render(
        request,
        'proyectoyaneblog/category_posts.html',
        {'posts': posts, 'category': category, 'categories': categories},
    )
