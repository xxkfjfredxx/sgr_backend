# Generated by Django 3.2 on 2025-07-11 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contratistas', '0001_initial'),
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contract_type', models.CharField(choices=[('Laboral', 'Laboral'), ('Servicios', 'Servicios'), ('Aprendizaje', 'Aprendizaje'), ('Temporal', 'Temporal'), ('Otro', 'Otro')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('renewal_count', models.IntegerField(default=0)),
                ('contract_file', models.FileField(blank=True, null=True, upload_to='contracts/')),
                ('status', models.CharField(choices=[('VIGENTE', 'Vigente'), ('TERMINADO', 'Terminado'), ('LIQUIDADO', 'Liquidado'), ('SUSPENDIDO', 'Suspendido')], default='VIGENTE', max_length=50)),
                ('notes', models.TextField(blank=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresa.company')),
                ('contractor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contratistas.contractorcompany')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
