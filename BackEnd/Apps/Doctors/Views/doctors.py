from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from BackEnd.Apps.Doctors.Forms.doctors import DoctorForm
from BackEnd.Apps.Doctors.models import Doctor


class DoctorListView(ListView):
  model = Doctor
  template_name = "doctors/doctors_list.html"
  context_object_name = "doctores"
  extra_context = {
    "title": "Medical",
    "title1": "Consulta de Doctores"
  }

  def get_queryset(self):
    # Puedes personalizar el queryset si es necesario
    return Doctor.objects.all()


class DoctorCreateView(CreateView):
  model = Doctor
  form_class = DoctorForm
  template_name = "doctors/doctors_forms.html"
  success_url = reverse_lazy('Doctors:doctors_list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Doctores'
    context['title1'] = 'Añadir Doctores'
    return context

  def form_invalid(self, form):
    context = self.get_context_data()
    context['form'] = form
    context['error'] = 'Error al crear el Doctor.'
    return self.render_to_response(context)


class DoctorUpdateView(UpdateView):
  model = Doctor
  form_class = DoctorForm
  template_name = "doctors/doctors_forms.html"
  success_url = reverse_lazy('Doctors:doctors_list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Doctores'
    context['title1'] = 'Actualizar Doctor'
    return context

  def form_invalid(self, form):
    context = self.get_context_data()
    context['form'] = form
    context['error'] = 'Error al actualizar el Doctor.'
    return self.render_to_response(context)
