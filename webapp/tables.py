import django_tables2 as tables
from django_tables2 import TemplateColumn
from django_tables2.utils import A
from .models import *

class RegistrosTable(tables.Table):
    class Meta:
        model = Registros_registro
        template_name = "django_tables2/bootstrap4.html"
        attrs = {
            "class":"table table-light table-striped table-hover",
            """ Margin: Arriba | Derecha | Abajo | Izquierda """
            "style":"width:92%; margin:0 4% 0 4%;",
        }
        fields = ['codregistro', 'DNI', 'codactividad', 'fecha']
    acciones = TemplateColumn(template_name='botonesregistro.html', verbose_name="")
    acciones.orderable=False

class CashierTable(tables.Table):
    delete = tables.LinkColumn('main:delete_item', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    })


class ClienteTable(tables.Table):
    class Meta:
        model = Registros_cliente
        template_name = "django_tables2/bootstrap4.html"
        attrs = {
            "class":"table table-light table-striped table-hover",
            """ Margin: Arriba | Derecha | Abajo | Izquierda """
            "style":"width:100%; margin:0 4% 0 0%;",
        }
        fields = ['DNI', 'nombre', 'apellido', 'telefono', 'email']
    acciones = TemplateColumn(CashierTable,)
    acciones.orderable=False

class CashierTable(tables.Table):
    delete = tables.LinkColumn('main:delete_item', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    })
