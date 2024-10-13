from django.contrib import admin
from BackEnd.Apps.Doctors.models import Clinic, Doctor, License, Profession

admin.site.register(Clinic)
admin.site.register(Doctor)
admin.site.register(License)
admin.site.register(Profession)
# Register your models here.
