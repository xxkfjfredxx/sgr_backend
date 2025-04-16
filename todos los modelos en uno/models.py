from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRole(models.Model):  # "Tabla de Roles de Usuario"
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    permissions = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_roles'  # "Tabla en base de datos: Roles de Usuario"

    def __str__(self):
        return self.name


class User(AbstractUser):  # "Tabla de Usuarios"
    role = models.ForeignKey(UserRole, on_delete=models.RESTRICT)  # "Rol del usuario"

    class Meta:
        db_table = 'users'  # "Tabla en base de datos: Usuarios"


class Branch(models.Model):  # "Tabla de Sucursales"
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField(blank=True, null=True)  # "Dirección"
    city = models.CharField(max_length=100, blank=True, null=True)  # "Ciudad"
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'branches'  # "Tabla en base de datos: Sucursales"

    def __str__(self):
        return self.name


class Position(models.Model):  # "Tabla de Cargos"
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)  # "Descripción del cargo"
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'positions'  # "Tabla en base de datos: Cargos"

    def __str__(self):
        return self.name


class WorkArea(models.Model):  # "Tabla de Áreas de Trabajo"
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'work_areas'  # "Tabla en base de datos: Áreas de Trabajo"

    def __str__(self):
        return self.name


class DocumentType(models.Model):  # "Tabla de Tipos de Documento"
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'document_types'  # "Tabla en base de datos: Tipos de Documento"

    def __str__(self):
        return self.name


class Employee(models.Model):  # "Tabla de Trabajadores"
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)  # "Usuario relacionado"
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


class EmploymentLink(models.Model):  # "Tabla de Vinculaciones Laborales"
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)  # "Trabajador relacionado"
    link_type = models.CharField(max_length=50)  # "Tipo de vinculación"
    contract_type = models.CharField(max_length=50, blank=True, null=True)  # "Tipo de contrato"
    resignation_reason = models.CharField(max_length=100, blank=True, null=True)  # "Motivo de retiro"
    position = models.ForeignKey('Position', on_delete=models.RESTRICT)  # "Cargo"
    area = models.ForeignKey('WorkArea', on_delete=models.RESTRICT)  # "Área de trabajo"
    branch = models.ForeignKey('Branch', on_delete=models.RESTRICT)  # "Sucursal"
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # "Salario"
    start_date = models.DateField()  # "Fecha de ingreso"
    end_date = models.DateField(blank=True, null=True)  # "Fecha de retiro"
    shift = models.CharField(max_length=50, blank=True, null=True)  # "Turno"
    status = models.CharField(max_length=50, default='ACTIVE')  # "Estado de la vinculación"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employment_links'  # "Tabla en base de datos: Vinculaciones Laborales"


class PersonalDocument(models.Model):  # "Tabla de Documentos Personales"
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)  # "Trabajador relacionado"
    document_type = models.ForeignKey('DocumentType', on_delete=models.RESTRICT)  # "Tipo de documento"
    file_name = models.CharField(max_length=255)  # "Nombre del archivo"
    file_path = models.CharField(max_length=255)  # "Ruta del archivo"
    observations = models.TextField(blank=True, null=True)  # "Observaciones del documento"
    uploaded_by = models.ForeignKey('User', on_delete=models.RESTRICT)  # "Usuario que subió el documento"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'personal_documents'  # "Tabla en base de datos: Documentos Personales"


class WorkHistory(models.Model):  # "Tabla de Historial Laboral"
    employment_link = models.ForeignKey('EmploymentLink', on_delete=models.CASCADE)  # "Vinculación laboral relacionada"
    field_modified = models.CharField(max_length=50)  # "Campo modificado"
    old_value = models.TextField(blank=True, null=True)  # "Valor anterior"
    new_value = models.TextField()  # "Valor nuevo"
    change_date = models.DateTimeField(auto_now_add=True)  # "Fecha de cambio"
    changed_by = models.ForeignKey('User', on_delete=models.RESTRICT)  # "Usuario que realizó el cambio"

    class Meta:
        db_table = 'work_history'  # "Tabla en base de datos: Historial Laboral"


class SystemAudit(models.Model):  # "Tabla de Auditoría del Sistema"
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)  # "Usuario relacionado"
    action = models.CharField(max_length=100)  # "Acción realizada"
    affected_table = models.CharField(max_length=100, blank=True, null=True)  # "Tabla afectada"
    record_id = models.IntegerField(blank=True, null=True)  # "ID del registro afectado"
    old_data = models.JSONField(blank=True, null=True)  # "Datos anteriores"
    new_data = models.JSONField(blank=True, null=True)  # "Datos nuevos"
    ip_origin = models.CharField(max_length=50, blank=True, null=True)  # "IP de origen"
    user_agent = models.TextField(blank=True, null=True)  # "User Agent del navegador"
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'system_audit'  # "Tabla en base de datos: Auditoría del Sistema"