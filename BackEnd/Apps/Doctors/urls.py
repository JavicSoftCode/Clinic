from django.urls import path, include

from BackEnd.Apps.Doctors.Views.doctors import DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView

app_name = 'Doctors'

urlpatterns = [
  path('doctor_list/', DoctorListView.as_view(), name='doctors_list'),
  path('doctor_create/', DoctorCreateView.as_view(), name='doctors_create'),
  path('doctor_update/<int:pk>/', DoctorUpdateView.as_view(), name='doctors_update'),
  path('doctor_delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
  path('', include('BackEnd.Apps.Auth.urls', namespace='Auth')),

]
