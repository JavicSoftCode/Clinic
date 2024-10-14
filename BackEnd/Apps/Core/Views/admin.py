from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class AdminTemplateView(LoginRequiredMixin, TemplateView):
  template_name = 'core/admin.html'
  login_url = reverse_lazy('Core:Auth:signin')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['global'] = 'Administracion JSC'
    context[
      'saludos'] = 'Administrador Sotware Clinico  <i class="fas fa-hospital" style="font-size: 35px; cursor: pointer"></i>'
    return context
