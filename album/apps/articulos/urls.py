from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_noticias, name="lista_noticias"),  # /noticias/
    path("<int:noticia_id>/", views.detalle_noticia, name="detalle_noticia"),  # /noticias/<id>/
]
