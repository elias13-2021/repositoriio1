from django.forms import ModelForm, EmailInput

from .models import *
#Registros_cliente, Registros_instructor, Registros_modalidad, Resgistros_dia, \
#Registros_actividad, Registros_registro


class ClienteForm(ModelForm):
    class Meta:
        model = Registros_cliente
        fields = '__all__'
        widgets = {
                'email': EmailInput(attrs={'type': 'email'})
            }

class InstructorForm(ModelForm):
    class Meta:
        model = Registros_instructor
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }

class ModalidadForm(ModelForm):
    class Meta:
        model = Registros_modalidad
        fields = '__all__'

class DiaForm(ModelForm):
    class Meta:
        model = Resgistros_dia
        fields = '__all__'

class ActividadForm(ModelForm):
    class Meta:
        model = Registros_actividad
        fields = '__all__'

class RegistroForm(ModelForm):
    class Meta:
        model = Registros_registro
        fields = '__all__'
