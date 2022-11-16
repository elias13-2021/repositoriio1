import django_filters
from django.forms.widgets import TextInput
from .models import *
from django.db.models import Q

#class RegistroFilter(django_filters.FilterSet):
#
#	busqueda = django_filters.CharFilter(lookup_expr='icontains', method='buscar',label="")
#
#	class Meta:
#		model = Registros_registro
#		fields = ['busqueda']
#
#	def buscar(self, queryset, name, value):
#		return queryset.filter(Q(codregistro__icontains=value) | Q(DNI__icontains=value))


class RegistroFilter(django_filters.FilterSet):

	busqueda = django_filters.CharFilter(lookup_expr='icontains', method='buscar',label="")

	class Meta:
		model = Registros_registro
		fields = ['busqueda']

	def buscar(self, queryset, name, value):
		return queryset.filter(Q(codregistro__icontains=value) | Q(DNI__icontains=value))