from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import Post

# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/starting_page.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all_posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    post_by_slug = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post_detail.html", {
        "post": post_by_slug,
        "tags": post_by_slug.tags.all()
    })