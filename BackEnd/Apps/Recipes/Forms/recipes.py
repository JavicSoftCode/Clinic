from django import forms

from BackEnd.Apps.Recipes.models import Medicamento


# Asegúrate de que en tu formulario utilices los nombres correctos:
class MedicamentoForm(forms.ModelForm):
  class Meta:
    model = Medicamento
    fields = ['code', 'description', 'price', 'stock', 'status', 'user']  # Usa los nombres correctos aquí
