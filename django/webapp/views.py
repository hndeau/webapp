from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def css_main(request):
    return render(request, "css/main.css")
