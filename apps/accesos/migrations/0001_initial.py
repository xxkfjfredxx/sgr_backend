# Generated by Django 3.2 on 2025-07-18 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('access_type', models.CharField(choices=[('ingreso', 'Ingreso'), ('egreso', 'Egreso')], max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('method', models.CharField(blank=True, help_text='manual, biometría, QR…', max_length=30)),
                ('remarks', models.CharField(blank=True, max_length=200)),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'access_logs',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='RiskAcceptanceForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('task_description', models.TextField()),
                ('risk_description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('signature', models.ImageField(blank=True, null=True, upload_to='signatures/')),
                ('accepted', models.BooleanField(default=True)),
                ('ip_address', models.CharField(blank=True, max_length=45, null=True)),
                ('user_agent', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'risk_acceptance_forms',
                'ordering': ['-date'],
            },
        ),
    ]
