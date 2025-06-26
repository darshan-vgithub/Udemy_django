from django.shortcuts import render
from django.http import HttpResponse

def january(request):
    return HttpResponse("January: Start fresh! Set clear goals and begin the year with positive energy.")

def february(request):
    return HttpResponse("February: Show love, not just to others but also to yourself. Self-care is important.")

# Create your views here.
