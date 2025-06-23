from django.shortcuts import render
from django.http import HttpResponse


def january(request):
    return HttpResponse("Dont forget to make a new year's resolution")


def february(request):
    return HttpResponse("Valentines day is coming  make sure you buy the necessary thing in the grocery store in the sale")

# Create your views here.
