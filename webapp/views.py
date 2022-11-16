from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django_tables2 import RequestConfig

from .filters import RegistroFilter
from .forms import *
from .models import *

# Create your views here.
from .tables import RegistrosTable

TEMPLATES_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Has iniciado sesión como {username}.")
                return redirect('index')
            else:
                messages.error(request, "Usuario o contraseña erróneos.")
        else:
            messages.error(request, "Usuario o contraseña erróneos.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect('login')


def index(request):
    return render(request, "index.html")

@login_required
def verClientes(request):
    busqueda = request.GET.get("buscar")
    cliente = Registros_cliente.objects.all()

    if busqueda:
        cliente = Registros_cliente.objects.filter(
            Q(DNI__icontains = busqueda) |
            Q(nombre__icontains = busqueda) |
            Q(apellido__icontains = busqueda) |
            Q(telefono__icontains = busqueda) |
            Q(email__icontains = busqueda)
        ).distinct()

    datos = {'clientes': cliente}
    return render(request, "crudClientes/verClientes.html", datos)

@login_required
def agregarCliente(request):
    if request.method == 'POST':
        formaCliente = ClienteForm(request.POST)
        if formaCliente.is_valid():
            formaCliente.save()
            return redirect('verClientes')
    else:
        formaCliente = ClienteForm()

    return render(request, 'crudClientes/agregarCliente.html', {'formaCliente': formaCliente})

@login_required
def editarCliente(request, DNI):
    cliente = get_object_or_404(Registros_cliente, pk=DNI)
    if request.method == 'POST':
        formaCliente = ClienteForm(request.POST, instance=cliente)
        if formaCliente.is_valid():
            formaCliente.save()
            return redirect('verClientes')
    else:
        formaCliente = ClienteForm(instance=cliente)

    return render(request, 'crudClientes/editarCliente.html', {'formaCliente': formaCliente})

def detalleCliente(request, DNI):
    #cliente = Registros_cliente.objects.get(pk=DNI)
    cliente = get_object_or_404(Registros_cliente, pk=DNI)
    return render(request, 'crudClientes/detalleCliente.html', {'cliente': cliente})

@login_required
def agregarInstructor(request):
    if request.method == 'POST':
        formaInstructor = InstructorForm(request.POST)
        if formaInstructor.is_valid():
            formaInstructor.save()
            return redirect('instructores')
    else:
        formaInstructor = InstructorForm()

    return render(request, 'crudInstructor/agregarInstructor.html', {'formaInstructor': formaInstructor})


@login_required
def verInstructores(request):
    no_instructores = Registros_instructor.objects.count()
    instructores = Registros_instructor.objects.all()
    return render(request, 'crudInstructor/verInstructores.html', {'no_instructores': no_instructores, 'instructores': instructores})


@login_required
def editarInstructor(request, DNIinstructor):
    instructor = get_object_or_404(Registros_instructor, pk=DNIinstructor)
    if request.method == 'POST':
        formaInstructor = InstructorForm(request.POST, instance=instructor)
        if formaInstructor.is_valid():
            formaInstructor.save()
            return redirect('instructores')
    else:
        formaInstructor = InstructorForm(instance=instructor)

    return render(request, 'crudInstructor/editarInstructor.html', {'formaInstructor': formaInstructor})

"""def detalleRegistro(request, codregistro):
    registro = Registros_registro.objects.get(pk=codregistro)
    registro = get_object_or_404(Registros_registro, pk=codregistro)
    return render(request, 'detalleRegistro.html', {'registro': registro})"""


@login_required
def agregarModalidad(request):
    if request.method == 'POST':
        formaModalidad = ModalidadForm(request.POST)
        if formaModalidad.is_valid():
            formaModalidad.save()
            return redirect('verModalidades')
    else:
        formaModalidad = ModalidadForm()

    return render(request, 'crudModalidad/agregarModalidad.html', {'formaModalidad': formaModalidad})


@login_required
def verModalidades(request):
    modalidades = Registros_modalidad.objects.all()
    return render(request, 'crudModalidad/verModalidades.html', {'modalidades': modalidades})


@login_required
def editarModalidad(request, codmodalidad):
    modalidad = get_object_or_404(Registros_modalidad, pk=codmodalidad)
    if request.method == 'POST':
        formaModalidad = ModalidadForm(request.POST, instance=modalidad)
        if formaModalidad.is_valid():
            formaModalidad.save()
            return redirect('verModalidades')
    else:
        formaModalidad= ModalidadForm(instance=modalidad)

    return render(request, 'crudModalidad/editarModalidad.html', {'formaModalidad': formaModalidad})


@login_required
def agregarDia(request):
    if request.method == 'POST':
        formaDia = DiaForm(request.POST)
        if formaDia.is_valid():
            formaDia.save()
            return redirect('verDias')
    else:
        formaDia = DiaForm()

    return render(request, 'crudDias/agregarDia.html', {'formaDia': formaDia})


@login_required
def verDias(request):
    dias = Resgistros_dia.objects.all()
    return render(request, 'crudDias/verDias.html', {'dias':dias})

@login_required
def eliminarDia(request, coddia):
    dias = get_object_or_404(Resgistros_dia, pk=coddia)
    if dias:
        dias.delete()
    return  redirect('crudDias/verDias.html')


@login_required
def verActividad(request):
    no_actividad = Registros_actividad.objects.count()
    actividades = Registros_actividad.objects.all()
    return render(request, 'crudActividad/verActividades.html', {'no_actividad': no_actividad, 'actividades': actividades})


@login_required
def agregarActividad(request):
    if request.method == 'POST':
        formaActividad = ActividadForm(request.POST)
        if formaActividad.is_valid():
            formaActividad.save()
            return redirect('actividad')
    else:
        formaActividad = ActividadForm()

    return render(request, 'crudActividad/agregarActividad.html', {'formaActividad': formaActividad})


#@login_required
#def verRegistros(request):
#    busqueda = request.GET.get("buscar")
#    registro = Registros_registro.objects.all()
#
#    if busqueda:
#        registro = Registros_registro.objects.filter(
#            Q(codregistro__icontains = busqueda) |
#            Q(DNI__icontains = busqueda) |
#            Q(codactividad__icontains = busqueda) |
#            Q(fecha__icontains = busqueda)
#        ).distinct()
#
#    datos = {'registros': registro}
#    return render(request, "crudRegistros/verRegistros.html", datos)

@login_required
def verRegistros(request):
    #no_clientes = Registros_cliente.objects.count()
    registros = Registros_registro.objects.all()
    filterset_class = RegistroFilter(request.GET, registros)
    table = RegistrosTable(filterset_class.qs)
    RequestConfig(request).configure(table)
    return render(request=request, template_name='crudRegistros/verRegistros.html', context={"clientes":registros, "table":table, "filterset_class":filterset_class})


@login_required
def agregarRegistro(request):
    if request.method == 'POST':
        formaRegistro = RegistroForm(request.POST)
        if formaRegistro.is_valid():
            formaRegistro.save()
            return redirect('registros')
    else:
        formaRegistro = RegistroForm()

    return render(request, 'crudRegistros/agregarRegistro.html', {'formaRegistro': formaRegistro})

@login_required
def editarRegistro(request, codregistro):
    registro = get_object_or_404(Registros_registro, pk=codregistro)
    if request.method == 'POST':
        formaRegistro = RegistroForm(request.POST, instance=registro)
        if formaRegistro.is_valid():
            formaRegistro.save()
            return redirect('registros')
    else:
        formaRegistro = RegistroForm(instance=registro)

    return render(request, 'crudRegistros/editarRegistro.html', {'formaRegistro': formaRegistro})

#Listado
@login_required
def listadoRegistroTM1(request):
    listadotm1 = Registros_registro.objects.filter(codactividad__horaentrada__contains='07:00')
    #listadotm1 = Registros_registro.objects.select_related('DNI', 'codactividad')
    #listadotm1 = Registros_registro.objects.filter(codactividad_id__contains='07:00')
    #listadotm1 = Registros_registro.objects.filter(DNI_id=39633413)
    #listadotm1 = Registros_registro.objects.raw('SELECT * FROM Registros_registro')

    return render(request, 'listados/listadoRegistroTM1.html', {'listadotm1': listadotm1})