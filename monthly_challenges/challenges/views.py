from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("this works!!")

# Create your views here.
