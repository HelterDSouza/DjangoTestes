from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from task1.models import Post

# Create your views here.


def home(request):
    all_posts = Post.objects.all()
    context = {}
    context["posts"] = all_posts
    return render(request, "task1/index.html", context)


def post_single(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {}
    context["post"] = post
    return render(request, "task1/detail.html", context)
