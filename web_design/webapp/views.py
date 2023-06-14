from django.shortcuts import render, HttpResponse


# Create your views here.
def chat_view_function(request):
    return render(request, "dashboard.html")


def chat1(request):
    return render(request, "chat1.html")


def search(request):
    return render(request, "search.html")


def updates(request):
    return render(request, "updates&FAQ.html")


def faq(request):
    return render(request, "FAQ.html")


def upgrade(request):
    return render(request, "upgrade.html")


def upfad(request):
    return render(request, "updfaq.html")


def demo(request):
    return render(request, "toggle.html")


def new(request):
    return render(request, "new.html")


def subscription(request):
    return render(request, "sub.html")


def photo_retouching(request):
    return render(request, "photo_retouching.html")


def talking_avatar(request):
    return render(request, "talking_avatar.html")


def hello(request):
    return render(request, "hello.html")
