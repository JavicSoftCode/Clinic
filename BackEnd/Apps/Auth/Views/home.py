from django.templatetags.static import static
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
  template_name = 'auth/home.html'

  extra_context = {
    "icon": static('public/clinic/icon/hospital_ico.ico'),
    "global": 'Bienvenidos JSC',
    "saludos": 'Bienvenidos a la Clínica SaludVital',
    "descripcion": 'Bienvenido a la Clínica SaludVital'
  }

  #
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['global'] = 'Bienvenidos JSC'
  #   context['saludos'] = 'Bienvenidos a la Clínica SaludVital'
  #   context['descripcion'] = 'Bienvenido a la Clínica SaludVital'
  #   return context
