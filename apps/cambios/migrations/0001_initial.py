# Generated by Django 3.2 on 2025-07-02 21:29

from django.db import migrations, models
import django_multitenant.mixins
import django_multitenant.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('evaluation_comments', models.TextField()),
                ('risk_level', models.CharField(max_length=50)),
                ('approved', models.BooleanField(default=False)),
                ('evaluated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-evaluated_at'],
            },
        ),
        migrations.CreateModel(
            name='ChangeImplementation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('implementation_date', models.DateField()),
                ('verification_comments', models.TextField(blank=True)),
                ('verification_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-implementation_date'],
            },
        ),
        migrations.CreateModel(
            name='ChangeRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pendiente'), ('approved', 'Aprobado'), ('rejected', 'Rechazado')], db_index=True, default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
            managers=[
                ('objects', django_multitenant.models.TenantManager()),
            ],
        ),
    ]
