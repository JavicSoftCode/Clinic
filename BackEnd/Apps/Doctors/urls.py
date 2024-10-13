from django.urls import path

from BackEnd.Apps.Doctors.Views.doctors import DoctorListView, DoctorCreateView, DoctorUpdateView

app_name = 'Doctors'

urlpatterns = [
  path('doctor_list/', DoctorListView.as_view(), name='doctors_list'),
  path('doctor_create/', DoctorCreateView.as_view(), name='doctors_create'),
  path('doctor_update/<int:pk>/', DoctorUpdateView.as_view(), name='doctors_update'),
]
