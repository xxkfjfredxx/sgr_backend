from django.db import models
from django.conf import settings

class Employee(models.Model):  # "Tabla de Trabajadores"
    user = user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # ESTA ES LA CLAVE CORRECTA
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )  # "Usuario relacionado"  # "Usuario relacionado"
    document = models.CharField(max_length=20, unique=True)  # "Documento de identidad"
    first_name = models.CharField(max_length=100)  # "Nombres"
    last_name = models.CharField(max_length=100)  # "Apellidos"
    gender = models.CharField(max_length=10, blank=True, null=True)  # "Género"
    birth_date = models.DateField(blank=True, null=True)  # "Fecha de nacimiento"
    eps = models.CharField(max_length=100, blank=True, null=True)
    afp = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)  # "Escolaridad"
    marital_status = models.CharField(max_length=50, blank=True, null=True)  # "Estado civil"
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)  # "Contacto de emergencia"
    phone_contact = models.CharField(max_length=20, blank=True, null=True)  # "Teléfono de contacto"
    address = models.CharField(max_length=100, blank=True, null=True)  # "Dirección de residencia"
    ethnicity = models.CharField(max_length=50, blank=True, null=True)  # "Grupo étnico"
    socioeconomic_stratum = models.IntegerField(blank=True, null=True)  # "Estrato socioeconómico"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employees'  # "Tabla en base de datos: Trabajadores"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'