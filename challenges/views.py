from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Eat no junk food for the entire month!")

def february(request):
    return HttpResponse("Walk for at least 20 miles every day!")
