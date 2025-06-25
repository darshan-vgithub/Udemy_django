from django.urls import path
from . import views
urlpatterns=[
    # path("january",views.january),
    # path("february",views.february)
    path("<int:month>",views.monthly_challenges_by_numbers,name="month-challenge_numbers"), # this <int:month> will tell django to convert the following parameter to int
    path("<str:month>",views.monthly_challenges,name="month-challenge"), # this <str:month> will tell django to expect a string and also convert it to a string
]