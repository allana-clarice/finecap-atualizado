from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages import views
from django.core.paginator import Paginator
from stand.models import Stand
from stand.forms import StandForm

class StandListView(generic.ListView):
    model = Stand
    template_name = 'stand/stand_list.html'
    context_object_name = 'stands'
    paginate_by = 2  # Define o número de itens por página

    def get_queryset(self):
        return Stand.objects.all()

class StandCreateView(views.SuccessMessageMixin, generic.CreateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand:stand_listar")
  success_message = "Reserva cadastrada com sucesso!"
  
class StandDeleteView(views.SuccessMessageMixin, generic.DeleteView):
  model = Stand
  success_url = reverse_lazy("stand:stand_listar")
  success_message = "Reserva removida com sucesso!"
  
class StandUpdateView(views.SuccessMessageMixin, generic.UpdateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand:stand_listar")
  success_message = "Reserva atualizada com sucesso!"
