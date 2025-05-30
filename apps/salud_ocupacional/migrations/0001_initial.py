# Generated by Django 5.1.6 on 2025-05-11 20:11

import apps.salud_ocupacional.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("empresa", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MedicalExam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "exam_phase",
                    models.CharField(
                        choices=[
                            ("Ingreso", "Ingreso"),
                            ("Periódico", "Periódico"),
                            ("Retiro", "Retiro"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "sub_type",
                    models.CharField(
                        choices=[
                            ("Audiometría", "Audiometría"),
                            ("Espirometría", "Espirometría"),
                            ("Visión", "Visión"),
                            ("Laboratorio", "Laboratorio"),
                            ("Presión arterial", "Presión arterial"),
                            ("Otro", "Otro"),
                        ],
                        default="Otro",
                        max_length=50,
                    ),
                ),
                (
                    "risk_level",
                    models.CharField(
                        choices=[
                            ("I", "Bajo"),
                            ("II", "Medio"),
                            ("III", "Alto"),
                            ("IV", "Crítico"),
                        ],
                        default="II",
                        help_text="Nivel de riesgo SST del puesto",
                        max_length=5,
                    ),
                ),
                ("date", models.DateField()),
                ("entity", models.CharField(max_length=100)),
                ("aptitude", models.CharField(max_length=100)),
                ("recommendations", models.TextField(blank=True)),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=apps.salud_ocupacional.models.document_upload_path,
                    ),
                ),
                (
                    "metrics",
                    models.JSONField(
                        blank=True,
                        help_text="Resultados específicos (p.ej. {'dB':25,'next_due':'2025-10-01'})",
                        null=True,
                    ),
                ),
                (
                    "next_due",
                    models.DateField(
                        blank=True,
                        help_text="Fecha calculada para próximo examen",
                        null=True,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="empresa.company",
                    ),
                ),
            ],
            options={
                "verbose_name": "Examen Médico",
                "verbose_name_plural": "Exámenes Médicos",
                "ordering": ["-date"],
            },
        ),
    ]
