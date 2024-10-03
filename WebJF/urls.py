from django.urls import path

from WebJF import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.home, name="Home"),
    path('vizzano',views.vizzano, name="Vizzano"),
    path('modare',views.modare, name="Modare"),
    path('actvitta',views.actvitta, name="Actvitta"),
    path('brsport',views.brsport, name="Brsport"),
    path('encuentranos',views.encuentranos, name="Encuentranos"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)