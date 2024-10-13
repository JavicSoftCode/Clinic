import re
from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Validators:
  @staticmethod
  def validate_full_name(value):
    value = value.strip()  # Eliminar espacios en blanco
    if not value:
      raise ValidationError(_("No se aceptan campos vacíos."))
    MinLengthValidator(3)(value)

    words = value.split()
    if len(words) < 2 or any(len(word) < 2 for word in words):
      raise ValidationError(_("Información incorrecta."))

  @staticmethod
  def validate_birth_date(value):
    if not value:
      raise ValidationError(_("No se aceptan campos vacíos."))
    if value >= timezone.now().date():
      raise ValidationError(_("Información incorrecta."))

    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
      raise ValidationError(_("Información incorrecta."))

  @staticmethod
  def validate_ruc(value, instance=None):
    ruc = str(value).strip()  # Eliminar espacios en blanco
    if not ruc:
      raise ValidationError(_("No se aceptan campos vacíos."))
    if not ruc.isdigit() or len(ruc) != 13:
      raise ValidationError(_("Información incorrecta."))

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
      raise ValidationError(_("Información incorrecta."))

  @staticmethod
  def validate_dni(value, instance=None):
    cedula = str(value).strip()  # Eliminar espacios en blanco
    if not cedula:
      raise ValidationError(_("No se aceptan campos vacíos."))
    if not cedula.isdigit() or len(cedula) != 10:
      raise ValidationError(_("Información incorrecta."))

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
      raise ValidationError(_("Información incorrecta."))

  @staticmethod
  def validate_address(value):
    value = value.strip()  # Eliminar espacios en blanco
    if not value:
      raise ValidationError(_("No se aceptan campos vacíos."))

    # Validación de longitud mínima
    if len(value) < 5:
      raise ValidationError(_("Información incorrecta."))

    # Validación de caracteres permitidos
    if not re.match(r'^[\w\s,.#-]+$', value):
      raise ValidationError(_("Información incorrecta."))

  @staticmethod
  def validate_username(value):
    if not value:
      raise ValidationError(_("No se aceptan campos vacíos."))
    MaxLengthValidator(20)(value)
    if not re.match(r'^\w+$', value):
      raise ValidationError(_("Información incorrecta."))

  @staticmethod
  def validate_email(value):
    if not value:
      raise ValidationError(_("No se aceptan campos vacíos."))
    if "@" not in value:
      raise ValidationError(_("Información incorrecta."))

  @staticmethod
  def validate_and_format_cell_number(cell):
    # Eliminar espacios al principio y al final
    cell = cell.strip()
    if not cell:
      raise ValidationError(_("No se aceptan campos vacíos."))

    # Expresión regular para validar el número de celular
    pattern = re.compile(r'^(?:\+593\s?9\d{8}|09\d{8}|(?:\+593)?9\d{8})$')

    # Comprobar si el número es válido
    if not pattern.match(cell):
      raise ValidationError(_("Información incorrecta."))

    # Formatear el número
    if cell.startswith("+593"):
      formatted_cell = cell.replace(" ", "")
    elif cell.startswith("09"):
      formatted_cell = "+593 " + cell
    else:
      formatted_cell = "+593 " + cell[1:]  # Eliminar el 0 inicial

    return formatted_cell
