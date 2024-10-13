from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView
from django.templatetags.static import static
from BackEnd.Apps.Auth.Forms.auth import CustomUserLoginForm, CustomUserForm


class SignUpView(CreateView):
  form_class = CustomUserForm
  template_name = 'auth/signup.html'
  success_url = reverse_lazy('Auth:signin')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['global'] = 'Registrarse'
    context['saludos'] = 'Bienvenido a Nuestra Clinica JSC'
    context['default_image_url'] = static('public/clinic/avatar.jpg')  # Ruta de la imagen predeterminada
    return context

  def form_valid(self, form):
    # Guardar el usuario sin hacer commit
    user = form.save(commit=False)
    # Guardar cualquier campo adicional (como la imagen)
    user.save()
    # Autologin después de guardar el usuario
    login(self.request, user)
    return super().form_valid(form)

  def form_invalid(self, form):
    print(form.errors)  # Para depurar errores
    return super().form_invalid(form)


# class SignUpView(CreateView):
#   model = CustomUser
#   form_class = CustomUserForm
#   template_name = 'auth/signup.html'
#   success_url = reverse_lazy('Auth:signin')
#
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['global'] = 'Registrarse'
#     context['saludos'] = 'Bienvenido a Nuestra Clinica JSC'
#     context['default_image_url'] = static('public/clinic/avatar.jpg')  # Ruta de la imagen predeterminada
#     return context
#
#   def form_valid(self, form):
#     user = form.save()
#     login(self.request, user)  # Inicia sesión automáticamente tras registrarse
#     messages.success(self.request, '¡Te has registrado exitosamente!')
#     return redirect(self.success_url)
#
#   def form_invalid(self, form):
#     # Manejo de errores personalizados si el formulario no es válido
#     messages.error(self.request, 'Por favor corrige los errores en el formulario.')
#     return self.render_to_response(self.get_context_data(form=form))


# Vista de registro
# class SignUpView(CreateView):
#     model = CustomUser  # Usamos CustomUser como modelo
#     form_class = CustomUserForm  # Usamos CustomUserForm
#     template_name = 'auth/signup.html'
#     success_url = reverse_lazy('Auth:signin')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['global'] = 'Registrarse'
#         context['saludos'] = 'Bienvenido a Nuestra Clinica JSC'
#         return context
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)  # Inicia sesión automáticamente tras registrarse
#         messages.success(self.request, '¡Te has registrado exitosamente!')
#         return redirect(self.success_url)


# Vista de inicio de sesión
class SignInView(LoginView):
  form_class = CustomUserLoginForm  # Utiliza el formulario de inicio de sesión personalizado
  template_name = 'auth/signin.html'
  success_url = reverse_lazy('Auth:home')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['global'] = 'Iniciar Sesion'
    context['saludos'] = 'Bienvenido a Nuestra Clinica JSC'
    return context

  @method_decorator(never_cache)
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect(self.success_url)  # Redirige si ya está autenticado
    return super().dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    messages.success(self.request, '¡Has iniciado sesión exitosamente!')
    return super().form_valid(form)


# Vista de cierre de sesión
class SignOutView(LoginRequiredMixin, LogoutView):
  next_page = reverse_lazy('Auth:home')  # Redirige tras cerrar sesión

  @method_decorator(never_cache)
  def dispatch(self, request, *args, **kwargs):
    messages.success(request, '¡Has cerrado sesión exitosamente!')
    return super().dispatch(request, *args, **kwargs)

# Vista para cambiar la contraseña
# class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
#     template_name = 'appAccounts/resetPassword.html'
#     success_url = reverse_lazy('Auth:home')
#
#     def form_valid(self, form):
#         messages.success(self.request, '¡Tu contraseña ha sido actualizada exitosamente!')
#         return super().form_valid(form)
