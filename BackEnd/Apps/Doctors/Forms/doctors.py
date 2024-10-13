# from django import forms
#
# from BackEnd.Apps.core.models import Doctor
#
#
# class DoctorForm(forms.ModelForm):
#   class Meta:
#     model = Doctor
#     fields = ['dni', 'first_name', 'last_name', 'profession', 'clinic', 'sex', 'birth_date', 'address', 'is_active']


from django import forms
from django.utils.translation import gettext_lazy as _

from BackEnd.Apps.Doctors.models import Doctor
from BackEnd.Apps.Doctors.Utils.utils import Validators  # Asegúrate de importar tus validadores


class DoctorForm(forms.ModelForm):
  class Meta:
    model = Doctor
    fields = ['dni', 'first_name', 'last_name', 'profession', 'clinic', 'sex', 'birth_date', 'address', 'is_active']

  def clean_dni(self):
    dni = self.cleaned_data.get('dni')
    if dni:
      Validators.validate_dni(dni)  # Llama al validador para DNI
    return dni

  def clean_first_name(self):
    first_name = self.cleaned_data.get('first_name')
    if first_name:
      Validators.validate_full_name(first_name)  # Llama al validador para nombres
    return first_name

  def clean_last_name(self):
    last_name = self.cleaned_data.get('last_name')
    if last_name:
      Validators.validate_full_name(last_name)  # Llama al validador para apellidos
    return last_name

  def clean_birth_date(self):
    birth_date = self.cleaned_data.get('birth_date')
    if birth_date:
      Validators.validate_birth_date(birth_date)  # Llama al validador para fecha de nacimiento
    return birth_date

  def clean_address(self):
    address = self.cleaned_data.get('address')
    if address:
      Validators.validate_address(address)  # Llama al validador para dirección
    return address

  # Si necesitas validaciones adicionales para otros campos, puedes añadir métodos similares
