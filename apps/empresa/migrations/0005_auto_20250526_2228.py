# Generated by Django 3.2 on 2025-05-27 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0004_auto_20250525_2153"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={
                "ordering": ["name"],
                "verbose_name": "Empresa",
                "verbose_name_plural": "Empresas",
            },
        ),
        migrations.AlterModelTable(
            name="company",
            table="companies",
        ),
    ]
