from django.urls import path, include
from BackEnd.Apps.Recipes.Views.recipes import MedicamentoListView, MedicamentoCreateView, MedicamentoUpdateView, MedicamentoDeleteView

app_name = 'Recipes'

urlpatterns = [
    path('recipes_list/', MedicamentoListView.as_view(), name='recipes_list'),
    path('recipes_Create/', MedicamentoCreateView.as_view(), name='recipes_Create'),
    path('recipes_Update/<int:pk>/', MedicamentoUpdateView.as_view(), name='recipes_Update'),
    path('recipes_Delete/<int:pk>/', MedicamentoDeleteView.as_view(), name='recipes_Delete'),
    path('', include('BackEnd.Apps.Auth.urls', namespace='Auth')),

]
