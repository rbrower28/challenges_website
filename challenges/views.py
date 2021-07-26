from django import http
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
# from django.template.loader import render_to_string

challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
    }

# Create your views here.

def index(request):

    list_items = ""
    months = list(challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })


def challenge_by_number(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    try:
        challenge_text = challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "challenge_text": challenge_text
        })
    except:
        # response_data = render_to_string("404.html")
        raise Http404
