from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.index, name="index"),
]