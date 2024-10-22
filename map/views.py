# map/views.py

from django.shortcuts import render

def map(request):
    # Logic for your map view goes here
    return render(request, 'map.html')
