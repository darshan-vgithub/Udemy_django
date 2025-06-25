from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound


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

def monthly_challenges_by_name(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_text = f"Month: {month}\nChallenge: {challenge_text}"
        return HttpResponse(response_text)
    except:
        return HttpResponseNotFound("This month is not supported")


def monthly_challenges_by_numbers(request,month):
    return HttpResponse(month)
# Create your views here.
