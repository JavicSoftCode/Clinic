from django import forms

from BackEnd.Apps.Recipes.models import Medicamento


class MedicamentoForm(forms.ModelForm):
  class Meta:
    model = Medicamento
    fields = ['codigo', 'descripcion', 'precio', 'stop', 'estado']
