from django.db import models
from datetime import date


class Registros_cliente(models.Model):
    DNI = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    fechadealta = models.DateField(default=date.today)
    observacion = models.CharField(max_length=200)#cambiar por estado
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'Registros_cliente: {self.DNI} {self.nombre} {self.apellido} {self.telefono} {self.email} {self.fechadealta} {self.observacion} {self.estado}'

class Registros_instructor(models.Model):
    DNIinstructor = models.CharField(max_length=8, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    matricula = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)
    fechadealta = models.DateField(default=date.today)
    email = models.CharField(max_length=150)


    def __str__(self):
        return f'Registros_instructor: {self.DNIinstructor} {self.nombre} {self.apellido} {self.telefono} {self.matricula} {self.estado} {self.fechadealta} {self.email}'

class Registros_modalidad(models.Model):
    codmodalidad = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=20, unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'Registros_modalidad: {self.codmodalidad} {self.nombre} {self.estado}'

class Resgistros_dia(models.Model):
    coddia = models.AutoField(primary_key=True, auto_created=True)
    #codclienteactividad = models.ForeignKey(Registros_cliente_actividad, on_delete=models.SET_NULL, null=True) (eliminar)
    descripcion = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return f'Registros_dia: {self.coddia} {self.descripcion}'

class Registros_actividad(models.Model):
    codactividad = models.AutoField(primary_key=True, auto_created=True)
    DNIinstructor =models.ForeignKey(Registros_instructor, on_delete=models.SET_NULL, null=True)
    codmodalidad = models.ForeignKey(Registros_modalidad, on_delete=models.SET_NULL, null=True)
    coddia = models.ForeignKey(Resgistros_dia, on_delete=models.SET_NULL, null=True)
    horaentrada = models.TimeField()
    horasalida = models.TimeField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'Registro_actividad: {self.codactividad} {self.DNIinstructor} {self.codmodalidad} {self.coddia} {self.horaentrada} {self.horasalida} {self.estado}'

class Registros_registro(models.Model):
    codregistro = models.AutoField(primary_key=True, auto_created=True)
    DNI = models.ForeignKey(Registros_cliente, on_delete=models.SET_NULL, null=True)
    codactividad = models.ForeignKey(Registros_actividad, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(default=date.today)

    def __str__(self):
        return f'Registros_registro: {self.codregistro} {self.DNI} {self.codactividad} {self.fecha}'


class Registros_cliente_actividad(models.Model):
    codclienteactividad = models.AutoField(primary_key=True, auto_created=True)
    DNI = models.ForeignKey(Registros_cliente, on_delete=models.SET_NULL, null=True)
    codactividad = models.ForeignKey(Registros_actividad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Registros_cliente_actividad: {self.codclienteactividad} {self.DNI} {self.codactividad}'
