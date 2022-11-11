from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

monthly_challenges = {
    "january": "Eat no junk food for the entire month!",
    "february": "Walk for at least 20 miles every day!",
    "march": "We should exercise everyday :(",
    "april": "We should exercise more",
    "may": "Walk for at least 20 miles every day!",
    "june": "Walk for at least 20 miles every day!",
    "july": "We should exercise more",
    "august": "We should exercise more",
    "september": "We should exercise more",
    "october": "We should exercise more",
    "november": "We should exercise more",
    "december": "We should exercise more"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("monthly_challenge", args=[redirect_month])
    
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")        