from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def say_hello(request, name=None):
    return HttpResponse(f"Hello {name}")
