from django.urls import path
from . import views

app_name = "reserva"

urlpatterns = [
    path('', views.ReservaListView.as_view(), name='reserva_listar'),
    path('cadastrar/', views.ReservaCreateView.as_view(), name='reserva_cadastrar'),
    path('detalhar/<int:pk>/', views.ReservaDetailView.as_view(), name='reserva_detalhar'),
    path('editar/<int:pk>/', views.ReservaUpdateView.as_view(), name='reserva_editar'),
    path('deletar/<int:pk>/', views.ReservaDeleteView.as_view(), name='reserva_deletar'),

 ] 
