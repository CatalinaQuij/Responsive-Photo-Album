from django.shortcuts import render
from django.conf import settings


def inicio(request):
    return render(request,"pages/index.html",{"MEDIA_URL": settings.MEDIA_URL})
