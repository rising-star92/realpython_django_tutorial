# dwitter/urls.py

from django.urls import path
from .views import show_dino

app_name = "dwitter"

urlpatterns = [
    path("show_dino/<str:name>/", show_dino),
]