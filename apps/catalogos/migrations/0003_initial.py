# Generated by Django 3.2 on 2025-07-02 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0001_initial'),
        ('catalogos', '0002_workarea_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='workarea',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_workarea_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workarea',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_workarea_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workarea',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_workarea_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='position',
            name='company',
            field=models.ForeignKey(help_text='Empresa/tenant al que pertenece este registro', on_delete=django.db.models.deletion.PROTECT, to='empresa.company'),
        ),
        migrations.AddField(
            model_name='position',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_position_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='position',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_position_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='position',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_position_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(help_text='Empresa/tenant al que pertenece este registro', on_delete=django.db.models.deletion.PROTECT, to='empresa.company'),
        ),
        migrations.AddField(
            model_name='branch',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_branch_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='branch',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_branch_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='branch',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_branch_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
