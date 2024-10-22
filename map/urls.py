# map/urls.py

from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [
    path('', views.map, name="Map"),  # This line should match the function name in views.py
]
