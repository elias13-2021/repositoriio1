from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Registros_cliente)
admin.site.register(Registros_instructor)
admin.site.register(Registros_modalidad)
admin.site.register(Resgistros_dia)
admin.site.register(Registros_actividad)
admin.site.register(Registros_cliente_actividad)
admin.site.register(Registros_registro)
