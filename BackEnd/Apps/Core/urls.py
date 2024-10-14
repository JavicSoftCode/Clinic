from django.urls import path, include

from BackEnd.Apps.Core.Views.admin import AdminTemplateView

app_name = 'Core'

urlpatterns = [
  path('adminClinic/', AdminTemplateView.as_view(), name='adminClinic'),
  path('', include('BackEnd.Apps.Auth.urls', namespace='Auth')),

]
