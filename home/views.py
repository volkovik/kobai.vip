from django.http import HttpRequest
from django.shortcuts import render

from home.models import Link, Post


def index(request: HttpRequest):
    """Home page view"""
    links = Link.objects.all()
    posts = Post.objects.all()

    return render(request, "home/index.html", {"links": links, "posts": posts})
