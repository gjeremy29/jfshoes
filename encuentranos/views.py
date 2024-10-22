from django.shortcuts import render
import folium

# Create your views here.

def home(request):

    initialMap = folium.Map(location=[-3.2592278,-79.9597467], zoom_start=9)
    

    context = {'map':initialMap._repr_html_()}
    return render(request, 'encuentranos/encuentranos.html')
