from django.shortcuts import render
import folium


def map(request):
    initialMap = folium.Map(location=[-34.6460675,-58.5268284], zoom_start=11)
    context = {'map':initialMap._repr_html_()}

    return render(request, 'map.html', context)
