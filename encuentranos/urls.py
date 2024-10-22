from django.urls import path

from . import views

urlpatterns = [
    path('',views.encuentranos, name="Encuentranos"),
]