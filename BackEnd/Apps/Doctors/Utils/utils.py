# from datetime import datetime
#
# from django.core.exceptions import ValidationError
# from django.core.validators import MinLengthValidator
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _
#
#
# class Validators:
#   @staticmethod
#   def validate_full_name(value):
#     MinLengthValidator(3, _("El nombre o apellido debe tener al menos 3 caracteres."))(value)
#
#     words = value.split()
#     if len(words) < 2 or any(len(word) < 2 for word in words):
#       raise ValidationError(
#         _("Debe ingresar al menos dos nombres o apellidos, y cada uno debe tener al menos 2 caracteres.")
#       )
#
#   @staticmethod
#   def validate_birth_date(value):
#     if value >= timezone.now().date():
#       raise ValidationError(_("La fecha de nacimiento no puede ser en el futuro."))
#
#   @staticmethod
#   def validate_ruc(value):
#     ruc = str(value)
#
#     if not ruc.isdigit():
#       raise ValidationError('El RUC debe contener solo números.')
#
#     if len(ruc) != 13:
#       raise ValidationError('El RUC debe tener 13 dígitos.')
#
#     coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
#
#     total = 0
#
#     for i in range(9):
#       digito = int(ruc[i])
#
#       coeficiente = coeficientes[i]
#
#       producto = digito * coeficiente
#
#       if producto > 9:
#         producto -= 9
#
#       total += producto
#
#     digito_verificador = (total * 9) % 10
#
#     if digito_verificador != int(ruc[9]):
#       raise ValidationError('El RUC no es válido.')
#
#   @staticmethod
#   def validate_dni(value):
#     cedula = str(value)
#     if not cedula.isdigit():
#       raise ValidationError('La cédula debe contener solo números.')
#
#     longitud = len(cedula)
#     if longitud != 10:
#       raise ValidationError('Cantidad de dígitos incorrecta.')
#
#     coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
#     total = 0
#     for i in range(9):
#       digito = int(cedula[i])
#       coeficiente = coeficientes[i]
#       producto = digito * coeficiente
#       if producto > 9:
#         producto -= 9
#       total += producto
#
#     digito_verificador = (total * 9) % 10
#     if digito_verificador != int(cedula[9]):
#       raise ValidationError('La cédula no es válida.')
#
#   @staticmethod
#   def validate_license_number(value):
#     """
#     En caso de no usar el metodo de generar 8 digitos aleatorios PONER ESTE METODO
#     """
#     if not value.isdigit():
#       raise ValidationError(_("El número de licencia debe contener solo dígitos."))
#
#     if not (6 <= len(value) <= 8):
#       raise ValidationError(_("El número de licencia debe tener entre 6 y 8 dígitos."))
#
#   @staticmethod
#   def validate_expiration_license(value):
#     """
#     Esta función valida si la fecha de expiración proporcionada es válida.
#     La licencia debe expirar en el futuro, no en el pasado o presente.
#     """
#     if isinstance(value, datetime):
#       value = value.date()  # Convertir a fecha si es datetime
#
#     if value <= timezone.now().date():
#       raise ValidationError(_('La expiración de la Licencia Médica del Doctor debe ser a futuro.'))
#
#   @staticmethod
#   def validate_address(value):
#     # Validación de longitud mínima
#     if len(value.strip()) < 5:
#       raise ValidationError('La dirección debe tener al menos 5 caracteres.')
#
#     # Validación de caracteres permitidos (no números de más de 3 dígitos)
#     if not re.match(r'^[\w\s,.#-]+$', value):
#       raise ValidationError('La dirección contiene caracteres no permitidos.')
#
#     # Ejemplo de validación adicional para evitar direcciones vacías o solo espacios
#     if not value.strip():
#       raise ValidationError('La dirección no puede estar vacía o ser solo espacios en blanco.')


import re
from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Validators:
  @staticmethod
  def validate_full_name(value):
    value = value.strip()  # Eliminar espacios en blanco
    MinLengthValidator(3, _("El nombre o apellido debe tener al menos 3 caracteres."))(value)

    words = value.split()
    if len(words) < 2 or any(len(word) < 2 for word in words):
      raise ValidationError(
        _("Debe ingresar los dos nombres o apellidos, y cada uno debe tener al menos 2 caracteres.")
      )

  # me falta el formato
  @staticmethod
  def validate_birth_date(value):
    if value >= timezone.now().date():
      raise ValidationError(_("La fecha de nacimiento no puede ser en el futuro."))

  @staticmethod
  def validate_ruc(value, instance=None):
    ruc = str(value).strip()  # Eliminar espacios en blanco

    # Validar que el RUC contenga solo dígitos
    if not ruc.isdigit():
      raise ValidationError(_('El RUC debe contener solo números.'))

    # Validar que el RUC tenga exactamente 13 dígitos
    if len(ruc) != 13:
      raise ValidationError(_('El RUC debe tener 13 dígitos.'))

    # Calcular el dígito verificador
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0

    for i in range(9):
      digito = int(ruc[i])
      coeficiente = coeficientes[i]
      producto = digito * coeficiente

      if producto > 9:
        producto -= 9

      total += producto

    digito_verificador = (total * 9) % 10

    if digito_verificador != int(ruc[9]):
      raise ValidationError(_('El RUC no es válido.'))

  @staticmethod
  def validate_dni(value, instance=None):
    cedula = str(value).strip()  # Eliminar espacios en blanco

    # Validar que la cédula contenga solo dígitos
    if not cedula.isdigit():
      raise ValidationError(_('La cédula debe contener solo números.'))

    # Validar que la cédula tenga exactamente 10 dígitos
    longitud = len(cedula)
    if longitud != 10:
      raise ValidationError(_('Cantidad de dígitos incorrecta.'))

    # Calcular el dígito verificador
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0
    for i in range(9):
      digito = int(cedula[i])
      coeficiente = coeficientes[i]
      producto = digito * coeficiente
      if producto > 9:
        producto -= 9
      total += producto

    digito_verificador = (total * 9) % 10
    if digito_verificador != int(cedula[9]):
      raise ValidationError(_('La cédula no es válida.'))

  @staticmethod
  def validate_license_number(value, instance=None):
    """
    Valida que el número de licencia contenga exactamente 8 dígitos
    y que no coincida con otro número de licencia de doctor.
    """
    value = value.strip()  # Eliminar espacios en blanco

    # Validar que el número de licencia contenga solo dígitos
    if not value.isdigit():
      raise ValidationError(_("El número de licencia debe contener solo dígitos."))

    # Validar que el número de licencia tenga exactamente 8 dígitos
    if len(value) != 8:
      raise ValidationError(_("El número de licencia debe tener exactamente 8 dígitos."))

  @staticmethod
  def validate_expiration_license(value):
    """
    Esta función valida si la fecha de expiración proporcionada es válida.
    La licencia debe expirar en el futuro, no en el pasado o presente.
    """
    if isinstance(value, datetime):
      value = value.date()  # Convertir a fecha si es datetime

    if value <= timezone.now().date():
      raise ValidationError(_('La expiración de la Licencia Médica del Doctor debe ser a futuro.'))

  @staticmethod
  def validate_address(value):
    value = value.strip()  # Eliminar espacios en blanco
    if not value:
      raise ValidationError(_('La dirección no puede estar vacía o ser solo espacios en blanco.'))

    # Validación de longitud mínima
    if len(value) < 5:
      raise ValidationError(_('La dirección debe tener al menos 5 caracteres.'))

    # Validación de caracteres permitidos
    if not re.match(r'^[\w\s,.#-]+$', value):
      raise ValidationError(_('La dirección contiene caracteres no permitidos.'))

    # Notificación en consola (opcional, dependiendo de cómo quieras manejarlo)
    print(f"Validación de dirección exitosa: {value}")
