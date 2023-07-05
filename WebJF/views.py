from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "WebJF/home.html")

def vizzano(request):

    return render(request, "WebJF/vizzano.html")

def modare(request):

    return render(request, "WebJF/modare.html")

def actvitta(request):

    return render(request, "WebJF/actvitta.html")

def brsport(request):

    return render(request, "WebJF/brsport.html")

