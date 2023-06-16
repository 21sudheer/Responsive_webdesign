from django.shortcuts import render

# Create your views here.


def mainpage(request):
    return render(request, "mainpage.html")


def photo_retouch(request):
    return render(request, "photo_retouch.html")


def video_generation(request):
    return render(request, "video_generation.html")


def Education_feedback(request):
    return render(request, "Education_feedback.html")


def Code_generation(request):
    return render(request, "Code_generation.html")


def Audio_generation(request):
    return render(request, "Audio_generation.html")


def welcome(request):
    return render(request, "welcome.html")
