# Generated by Django 3.2 on 2025-07-02 22:23

from django.db import migrations, models
import django.db.models.deletion
import django_multitenant.models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_initial'),
        ('historial', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='workhistory',
            managers=[
                ('objects', django_multitenant.models.TenantManager()),
            ],
        ),
        migrations.AddField(
            model_name='workhistory',
            name='company',
            field=models.ForeignKey(default=1, help_text='Empresa/tenant al que pertenece este registro', on_delete=django.db.models.deletion.PROTECT, to='empresa.company'),
            preserve_default=False,
        ),
    ]
