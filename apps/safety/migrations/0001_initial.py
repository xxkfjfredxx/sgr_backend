# Generated by Django 3.2 on 2025-07-18 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccinationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacuna', models.CharField(max_length=100, verbose_name='Vacuna')),
                ('fecha', models.DateField(verbose_name='Fecha de aplicación')),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha de vencimiento')),
                ('soporte', models.FileField(blank=True, null=True, upload_to='vaccination_records/', verbose_name='Soporte (PDF/foto)')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinations', to='empleados.employee')),
            ],
            options={
                'db_table': 'vaccination_records',
            },
        ),
        migrations.CreateModel(
            name='SignageInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_senal', models.CharField(max_length=100, verbose_name='Tipo de señal')),
                ('ubicacion_plano', models.JSONField(verbose_name='Ubicación (geoJSON)')),
                ('photo', models.FileField(blank=True, null=True, upload_to='signage_inventory/', verbose_name='Evidencia (foto)')),
                ('installed_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de verificación')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signage_inventory', to='empresa.company')),
            ],
            options={
                'db_table': 'signage_inventory',
                'ordering': ['-installed_at'],
            },
        ),
    ]
