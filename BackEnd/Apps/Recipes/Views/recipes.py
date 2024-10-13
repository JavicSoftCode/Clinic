from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from BackEnd.Apps.Recipes.Forms.recipes import MedicamentoForm  # Importa el formulario aquí
from BackEnd.Apps.Recipes.models import Medicamento


class MedicamentoListView(ListView):
  model = Medicamento
  template_name = 'recipes/recipes_list.html'
  context_object_name = 'medicamentos'


class MedicamentoCreateView(CreateView):
  model = Medicamento
  form_class = MedicamentoForm
  template_name = 'recipes/recipes_forms.html'
  success_url = reverse_lazy('Recipes:recipes_list')

  def form_valid(self, form):
    form.instance.usuario = self.request.user  # Asigna el usuario actual
    return super().form_valid(form)


class MedicamentoUpdateView(UpdateView):
  model = Medicamento
  form_class = MedicamentoForm
  template_name = 'recipes/recipes_forms.html'
  success_url = reverse_lazy('Recipes:recipes_list')


class MedicamentoDeleteView(DeleteView):
  model = Medicamento
  template_name = 'recipes/recipes_delete.html'
  success_url = reverse_lazy('Recipes:recipes_list')
