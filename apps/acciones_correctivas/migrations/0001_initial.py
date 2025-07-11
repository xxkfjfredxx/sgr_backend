# Generated by Django 3.2 on 2025-07-11 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('due_date', models.DateField(db_index=True)),
                ('completed', models.BooleanField(db_index=True, default=False)),
                ('evidence', models.FileField(blank=True, null=True, upload_to='improvement_evidence/')),
                ('comments', models.TextField(blank=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-due_date'],
            },
        ),
        migrations.CreateModel(
            name='ImprovementPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('open', 'Abierto'), ('in_progress', 'En Progreso'), ('closed', 'Cerrado')], default='open', max_length=20)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='RiskAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('evidence', models.FileField(blank=True, null=True, upload_to='risk_actions_evidence/')),
                ('comments', models.TextField(blank=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
