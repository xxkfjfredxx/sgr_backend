# Generated by Django 3.2 on 2025-07-18 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('objectives', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sstobjective',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_sstobjective_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sstobjective',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_sstobjective_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sstobjective',
            name='responsible',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='objectives', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sstobjective',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_sstobjective_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sstgoal',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_sstgoal_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sstgoal',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_sstgoal_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sstgoal',
            name='objective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='objectives.sstobjective'),
        ),
        migrations.AddField(
            model_name='sstgoal',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_sstgoal_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
