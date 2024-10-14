import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Validators:
  @staticmethod
  def validate_code(value):
    """Valida que el código tenga exactamente 13 dígitos numéricos."""
    if not re.fullmatch(r'\d{13}', value):
      raise ValidationError(
        _('Información incorrecta.')
      )

  @staticmethod
  def validate_description(value):
    """Valida que la descripción tenga al menos 3 caracteres y solo contenga letras y dígitos."""
    if len(value) < 3:
      raise ValidationError(
        _('Información incorrecta.')
      )
    if not re.fullmatch(r'[A-Za-z0-9 ]+', value):
      raise ValidationError(
        _('Información incorrecta.')
      )

  @staticmethod
  def validate_stock(value):
    """Valida que el stock sea un número positivo."""
    if not value.isdigit() or int(value) < 0:
      raise ValidationError(
        _('Información incorrecta.')
      )

  @staticmethod
  def validate_price(value):
    """Valida que el precio sea un número positivo con dos decimales."""
    if not re.fullmatch(r'\d+(\.\d{1,2})?', str(value)):
      raise ValidationError(
        _('Información incorrecta.')
      )
    if float(value) <= 0:
      raise ValidationError(
        _('Información incorrecta.')
      )
