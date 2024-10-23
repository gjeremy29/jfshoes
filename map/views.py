from django.shortcuts import render
from .models import Location
import folium
from folium.plugins import FastMarkerCluster

def map(request):
    locations = Location.objects.all()
    initialMap = folium.Map(location=[-2.1919108,-79.8854934], zoom_start=7)
    # Creamos el Clustering de los marcadores
    #latitudes = [location.lat for location in locations]
    #longitudes = [location.lng for location in locations]
    #popups = [location.name for location in locations]

    #print(latitudes)
    #print(longitudes)
    #print(list(zip(latitudes, longitudes, popups)))

    #FastMarkerCluster(data=list(zip(latitudes, longitudes, popups))).add_to(initialMap)

    #Creamos los marcadores
    for location in locations:
        coordinates = (location.lat, location.lng)
        folium.Marker(coordinates, popup='Sucursal ' + location.name).add_to(initialMap)

    context = {'map':initialMap._repr_html_(), 'locations':locations}

    return render(request, 'map/map.html', context)
