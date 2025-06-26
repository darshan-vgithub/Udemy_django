from django.shortcuts import render
from django.http import HttpResponse

def january(request):
    return HttpResponse("January: Start fresh! Set clear goals and begin the year with positive energy.")

def february(request):
    return HttpResponse("February: Show love, not just to others but also to yourself. Self-care is important.")

def monthly_challenge(request,month):
    challenge_text=None
    if month=="january":
        challenge_text="Start fresh! Set clear goals and begin the year with positive energy."
    elif month=="february":
        challenge_text="Show love, not just to others but also to yourself. Self-care is important."
    return HttpResponse(f"the month is {month} \n and the challenge is {challenge_text}")    

# Create your views here.
