from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from BackEnd.Apps.Doctors.Utils.utils import Validators


class Clinic(models.Model):
  ruc = models.CharField(_('Clinica Ruc'), unique=True, max_length=13, validators=[Validators.validate_ruc])
  name = models.CharField(_('Nombre de la Clinica'), unique=True, max_length=100)

  class Meta:
    verbose_name = "Clínica"
    verbose_name_plural = "Clínicas"
    ordering = ['name']

  @classmethod
  def exists(cls, ruc):
    ruc_exists = cls.objects.filter(ruc=ruc).exists()
    if ruc_exists:
      raise ValidationError(
        _('El RUC ingresado coincide con otro RUC existente. Por favor, ingrese un RUC diferente.')
      )
    return False  # Si no existe, retornamos False

  def full_name(self):
    return f"Nombre de la Clínica {self.name}"

  def full_name_and_ruc(self):
    return f"RUC {self.ruc} - Clinica {self.name}"

  def __str__(self):
    return f"{self.name}"


class Profession(models.Model):
  description = models.CharField(_('Profesión'), unique=True, max_length=100)

  class Meta:
    verbose_name = 'Profesión'
    verbose_name_plural = 'Profesiones'
    ordering = ['description']

  def full_description(self):
    return f"Profesión del Doctor {self.description}"

  def __str__(self):
    return f"{self.description}"


class Doctor(models.Model):
  SEX_CHOICES = (("M", 'Masculino'), ("F", 'Femenino'))
  profession = models.ManyToManyField(Profession, verbose_name='Profesión')
  clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="clinicas", verbose_name='Clínica')
  sex = models.CharField(_('Elegir Sexo'), default="M", max_length=1, choices=SEX_CHOICES)
  dni = models.CharField(_('Cédula'), unique=True, max_length=10, validators=[Validators.validate_dni])
  first_name = models.CharField(_('Nombres'), max_length=50, validators=[Validators.validate_full_name])
  last_name = models.CharField(_('Apellidos'), max_length=50, validators=[Validators.validate_full_name])
  address = models.CharField(_('Ubicación'), max_length=100, validators=[Validators.validate_address])
  birth_date = models.DateField(verbose_name='Fecha Nacimiento', validators=[Validators.validate_birth_date])
  is_active = models.BooleanField(_('Activo o Inactivo ?'), default=True)

  class Meta:
    verbose_name = 'Doctor'
    verbose_name_plural = 'Doctores'
    ordering = ['last_name', 'first_name']

  @classmethod
  def exists(cls, dni):
    dni_exists = cls.objects.filter(dni=dni).exists()
    if dni_exists:
      raise ValidationError(
        _('La cédula ingresada coincide con otro DNI existente. Por favor, ingrese un DNI diferente.')
      )
    return False  # Si no existe, retornamos False

  def full_name(self):
    return f'Doctor {self.first_name} {self.last_name}'

  def __str__(self):
    return f'{self.first_name} {self.last_name}'


class License(models.Model):
  doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
  license_number = models.CharField(_('Licencia Medica Del Doctor'), unique=True, max_length=8,
                                    validators=[Validators.validate_license_number])
  issued_date = models.DateField(_('Expiración de la Licencia Medica del Doctor'),
                                 validators=[Validators.validate_expiration_license])

  class Meta:
    verbose_name = 'Licencia'
    verbose_name_plural = 'Licencias'
    ordering = ['doctor', 'license_number']

  @classmethod
  def exists(cls, license_number):
    license_number_exists = cls.objects.filter(license_number=license_number).exists()
    if license_number_exists:
      raise ValidationError(
        _("El número de licencia ingresado coincide con otro número de licencia existente. Por favor, ingrese un número diferente.")
      )
    return False  # Si no existe, retornamos False

  def full_license(self):
    return f'Licencia Médica {self.license_number} del Doctor {self.doctor.first_name} {self.doctor.last_name}'

  def __str__(self):
    return f'{self.license_number}'
