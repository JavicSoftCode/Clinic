from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from BackEnd.Apps.Auth.Utils.utils import Validators
from BackEnd.Apps.Auth.models import CustomUser


class CustomUserForm(UserCreationForm):
  """
  Formulario para la creación de usuarios basado en el modelo CustomUser.
  Incluye validación de las contraseñas (password1 y password2) y utiliza validadores personalizados.
  """
  birth_day = forms.DateField(
    widget=forms.DateInput(
      attrs={
        'type': 'date',
        'class': 'form-control'
      }
    )
  )
  email = forms.EmailField(required=True, label='Correo Electrónico')

  class Meta:
    model = CustomUser  # El modelo asociado al formulario
    fields = [
      'dni', 'first_name', 'last_name', 'gender',
      'birth_day', 'cell', 'email', 'image', 'username', 'password1', 'password2'
    ]  # Campos del formulario

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name, field in self.fields.items():
      field.widget.attrs.update({'class': 'form-control input forgot-password signup', 'placeholder': field.label})
      # field.widget.attrs.update({'style': 'margin-top:-5px'})

  def clean_dni(self):
    """Validación personalizada para el campo DNI."""
    dni = self.cleaned_data.get('dni')
    Validators.validate_dni(dni)  # Utiliza el método de validación personalizado
    return dni

  def clean_cell(self):
    """Validación personalizada para el campo de celular."""
    cell = self.cleaned_data.get('cell')
    return Validators.validate_and_format_cell_number(cell)  # Usa la validación y el formato del número celular

  def clean_first_name(self):
    """Validación personalizada para el campo nombre."""
    first_name = self.cleaned_data.get('first_name')
    Validators.validate_full_name(first_name)  # Valida el nombre completo
    return first_name

  def clean_last_name(self):
    """Validación personalizada para el campo apellido."""
    last_name = self.cleaned_data.get('last_name')
    Validators.validate_full_name(last_name)  # Valida el apellido completo
    return last_name

  def clean_birth_day(self):
    """Validación personalizada para el campo fecha de nacimiento."""
    birth_day = self.cleaned_data.get('birth_day')
    Validators.validate_birth_date(birth_day)  # Valida la fecha de nacimiento
    return birth_day

  # def clean_address(self):
  #   """Validación personalizada para el campo dirección."""
  #   address = self.cleaned_data.get('address')
  #   Validators.validate_address(address)  # Valida la dirección
  #   return address

  def clean_email(self):
    """Validación personalizada para el campo de correo electrónico."""
    email = self.cleaned_data.get('email')
    Validators.validate_email(email)  # Valida el formato del correo
    if CustomUser.objects.filter(email=email).exists():
      raise forms.ValidationError("Este correo electrónico ya está en uso.")
    return email

  def clean_username(self):
    """Validación personalizada para el nombre de usuario."""
    username = self.cleaned_data.get('username')
    Validators.validate_username(username)  # Valida el nombre de usuario
    return username


class CustomUserLoginForm(AuthenticationForm):
  """
  Formulario para el inicio de sesión de usuarios basado en el modelo CustomUser.
  """

  class Meta:
    model = CustomUser
    CustomUser.email = forms.EmailField(required=True)
    fields = ('email', 'password')

  def clean(self):
    cleaned_data = super().clean()
    email = cleaned_data.get('email')
    password = cleaned_data.get('password')

    if email and password:
      user = authenticate(email=email, password=password)
      if user is None:
        raise forms.ValidationError(_('Las credenciales son incorrectas.'))
    return cleaned_data

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name, field in self.fields.items():
      field.widget.attrs.update({'class': 'form-control input forgot-password', 'placeholder': field.label})
      # field.widget.attrs.update({'style': 'margin-top:-5px'})
