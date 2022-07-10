from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpRequest

from home.models import Link


def index(request: HttpRequest):
    """View for home page"""
    links = Link.objects.all()

    return render(request, "home/index.html", {"links": links})
