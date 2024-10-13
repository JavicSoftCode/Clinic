from django.urls import path

from BackEnd.Apps.Core.Views.admin import AdminTemplateView

app_name = 'Core'

urlpatterns = [
  path('adminClinic/', AdminTemplateView.as_view(), name='adminClinic'),
]
