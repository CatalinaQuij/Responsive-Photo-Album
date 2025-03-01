from django.urls import path
from . import views


urlpatterns = [
    path('visor', views.fotos, name="fotos")
]
