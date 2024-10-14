from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from BackEnd.Apps.Recipes.Forms.recipes import MedicamentoForm
from BackEnd.Apps.Recipes.models import Medicamento


class MedicamentoListView(ListView):
  model = Medicamento
  template_name = 'recipes/recipes_list.html'
  context_object_name = 'medicamentos'
  extra_context = {
    "icon": static('public/clinic/icon/medicamento_ico.ico'),
    "global": "Administración de Medicamentos",
    "saludos": "Consulta de Medicamentos",
  }


class MedicamentoCreateView(CreateView):
  model = Medicamento
  form_class = MedicamentoForm
  template_name = 'recipes/recipes_forms.html'
  success_url = reverse_lazy('Recipes:recipes_list')
  extra_context = {
    "icon": static('public/clinic/icon/medicamento_ico.ico'),
    "global": "Registrando Medicamento",
    "saludos": "Registrar Medicamento",
  }

  def form_valid(self, form):
    form.instance.usuario = self.request.user
    return super().form_valid(form)


class MedicamentoUpdateView(UpdateView):
  model = Medicamento
  form_class = MedicamentoForm
  template_name = 'recipes/recipes_forms.html'
  success_url = reverse_lazy('Recipes:recipes_list')
  extra_context = {
    "icon": static('public/clinic/icon/medicamento_ico.ico'),
    "global": "Actualizando Medicamento",
    "saludos": "Actualizar Medicamento",
  }


class MedicamentoDeleteView(DeleteView):
  model = Medicamento
  template_name = 'recipes/recipes_delete.html'
  success_url = reverse_lazy('Recipes:recipes_list')
  extra_context = {
    "icon": static('public/clinic/icon/medicamento_ico.ico'),
    "global": "Eliminación del Medicamento",
    "saludos": "Eliminar Medicamento",
  }
