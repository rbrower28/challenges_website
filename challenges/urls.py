from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # /challenges/
    path("<int:month>", views.challenge_by_number), # /challenges/1
    path("<str:month>", views.monthly_challenge, name="month-challenge") # /challenges/january
]