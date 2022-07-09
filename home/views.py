from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):
    """View for home page"""

    return render(request, "home/index.html")
