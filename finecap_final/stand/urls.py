from django.urls import path
from . import views

app_name = "stand"

urlpatterns = [
    path('stand/', views.StandListView.as_view(), name='stand_listar'),
    path('cadastrarstand/', views.StandCreateView.as_view(), name='stand_cadastrar'),
    path('editarstand/<int:pk>/', views.StandUpdateView.as_view(), name='stand_editar'),
    path('deletarstand/<int:pk>/', views.StandDeleteView.as_view(), name='stand_deletar'),
      
] 

