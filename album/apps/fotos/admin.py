from django.contrib import admin

# Register your models here.
from .models import Mifoto #instanciar la clase que definimos en el modelo

admin.site.register(Mifoto)
