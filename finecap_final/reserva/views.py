from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages import views
from django.core.paginator import Paginator
from reserva.models import Reserva
from .forms import ReservaForm

# Create your views here.
class ReservaListView(generic.ListView):
    model = Reserva
    template_name = 'reserva/reserva_list.html'
    context_object_name = 'reservas'
    paginate_by = 2  # Define o número de itens por página

    def get_queryset(self):
        return Reserva.objects.all()


class ReservaDetailView(generic.DetailView):
  model = Reserva

class ReservaCreateView(views.SuccessMessageMixin, generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva:reserva_listar")
  success_message = "Reserva cadastrada com sucesso!"
  
class ReservaDeleteView(views.SuccessMessageMixin, generic.DeleteView):
  model = Reserva
  success_url = reverse_lazy("reserva:reserva_listar")
  success_message = "Reserva removida com sucesso!"
  
class ReservaUpdateView(views.SuccessMessageMixin, generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva:reserva_listar")
  success_message = "Reserva atualizada com sucesso!"