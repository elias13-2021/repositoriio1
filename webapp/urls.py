from django.contrib import admin
from django.urls import path

from django import views
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path("login/", login_request, name="login"),
	path("logout/", logout_request, name= "logout"),
    path('verClientes', verClientes, name='verClientes'),
    path('agregarCliente', agregarCliente),
    path('editarCliente/<int:DNI>', editarCliente),
    path('detalleCliente/<int:DNI>', detalleCliente),
    path('agregarInstructor', agregarInstructor),
    path('verInstructores', verInstructores, name="instructores"),
    path('editarInstructor/<int:DNIinstructor>', editarInstructor),
    path('agregarModalidad', agregarModalidad),
    path('verModalidades', verModalidades, name="verModalidades"),
    path('editarModalidad/<int:codmodalidad>', editarModalidad),
    path('agregarDia', agregarDia),
    path('verDias', verDias, name="verDias"),
    path('eliminarDia/<int:coddia>', eliminarDia),
    path('verActividades', verActividad, name='actividad'),
    path('agregarActividad', agregarActividad),
    path('verRegistros', verRegistros, name='registros'),
    path('agregarRegistro', agregarRegistro),
    path('editarRegistro/<int:codregistro>', editarRegistro),
    path('listadoRegistroTM1', listadoRegistroTM1),
]