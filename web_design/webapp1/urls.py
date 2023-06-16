from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path("photo_retouch/", views.photo_retouch, name="photo_retouch"),
    path("video_generation/", views.video_generation, name="video_generation"),
    path("Education_feedback/", views.Education_feedback, name="Education_feedback"),
    path("Code_generation/", views.Code_generation, name="Code_generation"),
    path("Audio_generation/", views.Audio_generation, name="Audio_generation"),
    path("welcome/", views.welcome, name="welcome"),
]
