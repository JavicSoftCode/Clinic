# Generated by Django 5.1.2 on 2024-10-12 05:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stop', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('activo', 'Activo'), ('baja', 'De Baja')], default='activo', max_length=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
