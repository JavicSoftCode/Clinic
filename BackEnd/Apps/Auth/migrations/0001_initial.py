# Generated by Django 5.1.2 on 2024-10-11 01:38

import BackEnd.Apps.Auth.Utils.utils
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Menú')),
                ('icon', models.CharField(max_length=50, unique=True, verbose_name='Icono del Menú')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('dni', models.CharField(max_length=10, unique=True, validators=[BackEnd.Apps.Auth.Utils.utils.Validators.validate_dni], verbose_name='DNI')),
                ('cell', models.CharField(max_length=15, unique=True, validators=[BackEnd.Apps.Auth.Utils.utils.Validators.validate_and_format_cell_number], verbose_name='Celular')),
                ('address', models.CharField(max_length=255, validators=[BackEnd.Apps.Auth.Utils.utils.Validators.validate_address], verbose_name='Dirección')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/images/', verbose_name='Imagen')),
                ('birth_day', models.DateField(validators=[BackEnd.Apps.Auth.Utils.utils.Validators.validate_birth_date], verbose_name='Fecha Nacimiento')),
                ('first_name', models.CharField(max_length=30, validators=[BackEnd.Apps.Auth.Utils.utils.Validators.validate_full_name], verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=30, validators=[BackEnd.Apps.Auth.Utils.utils.Validators.validate_full_name], verbose_name='Apellido')),
                ('username', models.CharField(max_length=20, unique=True, validators=[BackEnd.Apps.Auth.Utils.utils.Validators.validate_username], verbose_name='Usuario')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[BackEnd.Apps.Auth.Utils.utils.Validators.validate_email], verbose_name='Correo Electrónico')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Último inicio de sesión')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de registro')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, unique=True, verbose_name='Url')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Módulo')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Icono para el Módulo')),
                ('is_active', models.BooleanField(default=True, verbose_name='Es activo')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modules', to='Auth.menu', verbose_name='Menú para el Módulo')),
                ('permissions', models.ManyToManyField(blank=True, to='auth.permission', verbose_name='Permisos')),
            ],
            options={
                'verbose_name': 'Modulo',
                'verbose_name_plural': 'Modulos',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Super Usuario',
                'verbose_name_plural': 'Super Usuarios',
            },
            bases=('Auth.customuser',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario Normal',
                'verbose_name_plural': 'Usuarios Normales',
            },
            bases=('Auth.customuser',),
        ),
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario Administrador',
                'verbose_name_plural': 'Usuarios Administradores',
            },
            bases=('Auth.customuser',),
        ),
        migrations.CreateModel(
            name='GroupModulePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='group_module_permissions', to='auth.group', verbose_name='Grupo')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_module_permissions', to='auth.permission', verbose_name='Permiso')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='group_module_permissions', to='Auth.module', verbose_name='Modulo')),
            ],
            options={
                'verbose_name': 'Grupo Modulo Permiso',
                'verbose_name_plural': 'Grupos Modulos Permisos',
                'ordering': ('group',),
                'unique_together': {('group', 'module', 'permission')},
            },
        ),
    ]
