# Generated by Django 3.2 on 2025-07-02 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0002_initial'),
        ('indicadores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicatorresult',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_indicatorresult_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='indicatorresult',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_indicatorresult_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='indicatorresult',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='indicadores.indicator'),
        ),
        migrations.AddField(
            model_name='indicatorresult',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_indicatorresult_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='indicator',
            name='company',
            field=models.ForeignKey(help_text='Empresa/tenant al que pertenece este registro', on_delete=django.db.models.deletion.PROTECT, to='empresa.company'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_indicator_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='indicator',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_indicator_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='indicator',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_indicator_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='indicatorresult',
            unique_together={('indicator', 'period')},
        ),
    ]
