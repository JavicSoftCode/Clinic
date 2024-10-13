from crum import get_current_request
from django.contrib.auth.models import Group, Permission, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.forms.models import model_to_dict
from django.utils.translation import gettext_lazy as _
from BackEnd.Apps.Auth.Utils.utils import Validators
from django.utils import timezone


class Menu(models.Model):
  """Modelo que representa un menú con un nombre y un icono."""
  name = models.CharField(_('Nombre del Menú'), max_length=100, unique=True)
  icon = models.CharField(_('Icono del Menú'), max_length=50, unique=True)

  def __str__(self):
    return self.name

  def get_model_to_dict(self):
    """Convierte el objeto Menu en un diccionario."""
    return model_to_dict(self)

  def get_icon(self):
    """Devuelve el icono del menú o un icono predeterminado."""
    return self.icon or 'bi bi-calendar-x-fill'

  def has_related_objects(self):
    """Verifica si existen módulos relacionados con este menú."""
    return self.modules.exists()  # Usando el related_name

  class Meta:
    verbose_name = 'Menu'
    verbose_name_plural = 'Menus'
    ordering = ['name']


class Module(models.Model):
  """Modelo que representa un módulo dentro de un menú."""
  url = models.CharField(_('Url'), max_length=100, unique=True)
  name = models.CharField(_('Nombre del Módulo'), max_length=100, unique=True)
  menu = models.ForeignKey(Menu, on_delete=models.PROTECT, verbose_name='Menú para el Módulo', related_name='modules')
  description = models.CharField(_('Descripción'), max_length=200, null=True, blank=True)
  icon = models.CharField(_('Icono para el Módulo'), max_length=100, null=True, blank=True, unique=True)
  is_active = models.BooleanField(verbose_name='Es activo', default=True)
  permissions = models.ManyToManyField(verbose_name='Permisos', to=Permission, blank=True)

  def __str__(self):
    return '{} [{}]'.format(self.name, self.url)

  def get_model_to_dict(self):
    """Convierte el objeto Module en un diccionario."""
    return model_to_dict(self)

  def has_related_objects(self):
    """Verifica si existen permisos relacionados con este módulo."""
    return GroupModulePermission.objects.filter(module=self).exists()

  def get_icon(self):
    """Devuelve el icono del módulo o un icono predeterminado."""
    return self.icon or 'bi bi-x-octagon'

  class Meta:
    verbose_name = 'Modulo'
    verbose_name_plural = 'Modulos'
    ordering = ('name',)


class GroupModulePermission(models.Model):
  """Modelo que representa los permisos asociados a un grupo y un módulo."""
  group = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Grupo',
                            related_name='group_module_permissions')
  module = models.ForeignKey(Module, on_delete=models.PROTECT, verbose_name='Modulo',
                             related_name='group_module_permissions')
  permission = models.ForeignKey(Permission, on_delete=models.CASCADE, verbose_name='Permiso', related_name='group_module_permissions')

  class Meta:
    unique_together = ('group', 'module', 'permission')
    verbose_name = 'Grupo Modulo Permiso'
    verbose_name_plural = 'Grupos Modulos Permisos'
    ordering = ('group',)

  def __str__(self):
    return f"{self.group.name} - {self.module.name} - {self.permission.codename}"

  @staticmethod
  def get_group_module_permission_active_list(group_id):
    return GroupModulePermission.objects.select_related(
      'module',
      'module__menu'
    ).filter(
      group_id=group_id,
      module__is_active=True
    )


class CustomUserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError(_('El campo de correo electrónico es obligatorio'))
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    superuser = SuperUser(email=email, **extra_fields)
    superuser.set_password(password)
    superuser.save(using=self._db)
    return superuser

  def create_useradmin(self, email, password=None, **extra_fields):
    if not self.model.objects.filter(is_superuser=True).exists():
      raise ValueError(_('Solo un superusuario puede crear un UserAdmin'))

    extra_fields.setdefault('is_staff', True)
    user_admin = UserAdmin(email=email, **extra_fields)
    user_admin.set_password(password)
    user_admin.save(using=self._db)
    self.assign_permissions_and_groups(user_admin, extra_fields)

    return user_admin


class CustomUser(AbstractBaseUser, PermissionsMixin):
  gender = models.CharField(verbose_name='Sexo', max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino')), default='M')
  dni = models.CharField(_('DNI'), max_length=10, unique=True, validators=[Validators.validate_dni])
  cell = models.CharField(_('Celular'), max_length=15, unique=True, validators=[Validators.validate_and_format_cell_number])
  address = models.CharField(_('Dirección'), max_length=255, validators=[Validators.validate_address])
  image = models.ImageField(_('Imagen'), upload_to='users/images/', blank=True, null=True)  # pip install Pillow
  birth_day = models.DateField(_('Fecha Nacimiento'), validators=[Validators.validate_birth_date])
  first_name = models.CharField(_('Nombre'), max_length=30, validators=[Validators.validate_full_name])
  last_name = models.CharField(_('Apellido'), max_length=30, validators=[Validators.validate_full_name])
  username = models.CharField(_('Usuario'), max_length=20, unique=True, validators=[Validators.validate_username])
  email = models.EmailField(_('Correo Electrónico'), unique=True, validators=[Validators.validate_email])
  is_superuser = models.BooleanField(_('Super Usuario'), default=False)
  is_staff = models.BooleanField(_('Admin'), default=False)
  is_active = models.BooleanField(_('Activo'), default=True)
  last_login = models.DateTimeField(_('Último inicio de sesión'), blank=True, null=True)
  date_joined = models.DateTimeField(_('Fecha de registro'), default=timezone.now)

  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['dni', 'cell', 'birth_day', 'first_name', 'last_name', 'username']

  class Meta:
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'
    ordering = ['first_name', 'last_name']

  def clean(self):
    super().clean()
    self.cell = Validators.validate_and_format_cell_number(self.cell)

  def has_perm(self, perm, obj=None):
    """Comprueba si el usuario tiene un permiso específico."""
    if self.is_superuser:
      return True
    return super().has_perm(perm, obj)

  def __str__(self):
    return f"{self.email}"

  @property
  def get_full_name(self):
    return f"{self.first_name} {self.last_name}"

  def get_groups(self):
    return self.groups.all()

  def get_short_name(self):
    return self.username

  def get_group_session(self):
    request = get_current_request()
    return Group.objects.get(pk=request.session.get('group_id'))

  def set_group_session(self):
    request = get_current_request()

    if 'group' not in request.session:
      groups = self.groups.all().order_by('id')
      if groups.exists():
        request.session['group'] = groups.first()
        request.session['group_id'] = request.session['group'].id


class SuperUser(CustomUser):
  class Meta:
    verbose_name = 'Super Usuario'
    verbose_name_plural = 'Super Usuarios'

  def assign_group(self, group):
    self.groups.add(group)
    self.save()

  def remove_group(self, group):
    self.groups.remove(group)
    self.save()

  def assign_permission(self, permission):
    self.user_permissions.add(permission)
    self.save()

  def remove_permission(self, permission):
    self.user_permissions.remove(permission)
    self.save()


class UserAdmin(CustomUser):
  class Meta:
    verbose_name = 'Usuario Administrador'
    verbose_name_plural = 'Usuarios Administradores'

  def has_permission_on_module(self, module_name, permission_code):
    module = Module.objects.get(name=module_name)
    return GroupModulePermission.objects.filter(
      group__in=self.groups.all(),
      module=module,
      permission__codename=permission_code
    ).exists()


class User(CustomUser):
  class Meta:
    verbose_name = 'Usuario Normal'
    verbose_name_plural = 'Usuarios Normales'
