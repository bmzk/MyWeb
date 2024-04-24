from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("city", views.display_city, name="citypage"),
]