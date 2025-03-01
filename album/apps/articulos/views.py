from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Noticia

def lista_noticias(request):
    noticias = Noticia.objects.filter(publicada=True).order_by('-fecha_publicacion')
    return render(request, "articulos/listado.html", {"noticias": noticias, "MEDIA_URL": settings.MEDIA_URL})

def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, "articulos/detalle.html", {"noticia": noticia, "MEDIA_URL": settings.MEDIA_URL})
