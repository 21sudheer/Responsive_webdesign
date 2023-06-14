from django.urls import path
from . import views

urlpatterns = [
    path("chat_view_function/", views.chat_view_function, name="chat_view_function"),
    path("", views.chat1, name="chat1"),
    path("search/", views.search, name="search"),
    path("updates", views.updates, name="updates"),
    path("faq/", views.faq, name="faq"),
    path("upgrade/", views.upgrade, name="upgrade"),
    path("upfad/", views.upfad, name="upfad"),
    path("demo/", views.demo, name="demo"),
    path("new/", views.new, name="new"),
    path("subscription/", views.subscription, name="subscription"),
    path("photo_retouching/", views.photo_retouching, name="photo_retouching"),
    path("talking_avatar/", views.talking_avatar, name="talking_avatar"),
    path("hello/", views.hello, name="hello"),
]
