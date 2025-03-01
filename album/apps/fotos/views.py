from django.shortcuts import render
from django.conf import settings
from .models import Mifoto
# Create your views here.

def fotos(request):
    mis_fotos = Mifoto.objects.all()
    return render(request, "page/fotos.html",{"fotos":mis_fotos, "MEDIA_URL": settings.MEDIA_URL})
