from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('BackEnd.Apps.Auth.urls', namespace='Auth')),
                path('core', include('BackEnd.Apps.Core.urls', namespace='Core')),
                path('doctors', include('BackEnd.Apps.Doctors.urls', namespace='Doctors')),
                path('doctors', include('BackEnd.Apps.Recipes.urls', namespace='Recipes')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
