from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse


monthly_challenges={
    "january":"Start fresh! Set clear goals and begin the year with positive energy.",
    "february":"Show love, not just to others but also to yourself. Self-care is important.",
    "march":"Spring into action! Take steps towards your personal and professional goals.",
    "april":"Embrace change as nature blooms. It’s time to start something new and exciting.",
    "may":"Stay consistent. Small efforts every day lead to big results in the future.",
    "june":"Be open to new ideas. Don’t be afraid to try something new.",
    "july":"Embrace the change. It’s time to start something new and exciting.",
    "august":"Embrace the change. It’s time to start something new and exciting.",
    "september":"Embrace the change. It’s time to start something new and exciting.",
    "october":"Embrace the change. It’s time to start something new and exciting.",
    "november":"Embrace the change. It’s time to start something new and exciting.",
    "december":"Embrace the change. It’s time to start something new and exciting.",
}
def january(request):
    return HttpResponse("January: Start fresh! Set clear goals and begin the year with positive energy.")

def february(request):
    return HttpResponse("February: Show love, not just to others but also to yourself. Self-care is important.")

def monthly_challenge_by_name(request,month):
    challenge_text=monthly_challenges[month]
    return HttpResponse(f"<h1>Month: {month}\nChallenge: {challenge_text}</h1>")

def monthly_challenge_by_number(request,month):
    months=list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    response_data=months[month-1]
    redirect_path=reverse("month-challenge",args=[response_data])

    return HttpResponseRedirect(redirect_path) 

# Create your views here.
