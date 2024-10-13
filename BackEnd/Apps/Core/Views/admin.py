from django.views.generic import TemplateView


class AdminTemplateView(TemplateView):
  template_name = 'core/admin.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['global'] = 'Administracion JSC'
    context['saludos'] = 'Administrador Sotware Clinico  <i class="fas fa-hospital" style="font-size: 35px; cursor: pointer"></i>'
    return context
