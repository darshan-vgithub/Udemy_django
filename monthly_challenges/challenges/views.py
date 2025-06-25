from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound


# def january(request):
#     return HttpResponse("Dont forget to make a new year's resolution")


# def february(request):
#     return HttpResponse("Valentines day is coming  make sure you buy the necessary thing in the grocery store in the sale")


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "January: Start fresh! Set clear goals and begin the year with positive energy."
    elif month == "february":
        challenge_text = "February: Show love, not just to others but also to yourself. Self-care is important."
    elif month == "march":
        challenge_text = "March: Spring into action! Take steps towards your personal and professional goals."
    elif month == "april":
        challenge_text = "April: Embrace change as nature blooms. It’s time to start something new and exciting."
    elif month == "may":
        challenge_text = "May: Stay consistent. Small efforts every day lead to big results in the future."
    elif month == "june":
        challenge_text = "June: Mid-year check! Reflect on your resolutions and realign your goals."
    elif month == "july":
        challenge_text = "July: Enjoy the warmth of life, celebrate your progress, and recharge for the second half of the year."
    elif month == "august":
        challenge_text = "August: Push your boundaries. Take on a challenge you’ve been avoiding."
    elif month == "september":
        challenge_text = "September: Learn something new this month—skills, hobbies, or knowledge."
    elif month == "october":
        challenge_text = "October: Stay strong and keep moving forward, even if things get spooky or uncertain!"
    elif month == "november":
        challenge_text = "November: Be grateful for what you have. Practicing gratitude changes perspective."
    elif month == "december":
        challenge_text = "December: Reflect, rest, and recharge. Prepare yourself for a new beginning next year."
    else:
        challenge_text = HttpResponseNotFound("Invalid month! Please enter a valid month name.")
    
    return HttpResponse(challenge_text)
# Create your views here.
