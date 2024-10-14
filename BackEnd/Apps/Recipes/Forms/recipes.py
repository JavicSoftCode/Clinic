from django import forms

from BackEnd.Apps.Recipes.models import Medicamento


# Asegúrate de que en tu formulario utilices los nombres correctos:
class MedicamentoForm(forms.ModelForm):
  class Meta:
    model = Medicamento
    fields = ['code', 'description', 'price', 'stock', 'status', 'user']  # Usa los nombres correctos aquí

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name, field in self.fields.items():
      field.widget.attrs.update({'class': 'form-control input forgot-password signup', 'placeholder': field.label})
