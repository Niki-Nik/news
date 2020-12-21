from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "main/index.html")


def about(request):
    return HttpResponse("Страница про нас")
