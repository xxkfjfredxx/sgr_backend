# Generated by Django 3.2 on 2025-07-18 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('capacitaciones', '0001_initial'),
        ('empleados', '0002_employeedocument_company'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsessionattendance',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_trainingsessionattendance_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainingsessionattendance',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_trainingsessionattendance_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainingsessionattendance',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.employee'),
        ),
        migrations.AddField(
            model_name='trainingsessionattendance',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='capacitaciones.trainingsession'),
        ),
        migrations.AddField(
            model_name='trainingsessionattendance',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_trainingsessionattendance_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainingsession',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.company'),
        ),
        migrations.AddField(
            model_name='trainingsession',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_trainingsession_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainingsession',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_trainingsession_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainingsession',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_trainingsession_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='certification',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_certification_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='certification',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_certification_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='certification',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certifications', to='capacitaciones.trainingsessionattendance'),
        ),
        migrations.AddField(
            model_name='certification',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_certification_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='trainingsessionattendance',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('session', 'employee'), name='unique_attendance_active'),
        ),
    ]
