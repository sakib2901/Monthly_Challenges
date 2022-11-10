from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenges(request, month):
    challenge_text = None
    if month == "January":
        challenge_text = "Eat no junk food for the entire month!"
    elif month == "February":
        challenge_text = "Walk for at least 20 miles every day!"
    elif month == "March":
        challenge_text = "We should exercise everyday :("
    else:
        return HttpResponseNotFound("This month is not supported")
    
    return HttpResponse (challenge_text)
        