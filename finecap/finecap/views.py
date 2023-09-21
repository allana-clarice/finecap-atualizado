from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm

def detalhes_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    return render(request,'reservas/detalhes_reserva.html', {'reserva': reserva})

def adicionar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/adicionar_reserva.html', {'form': form})

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/listar_reservas.html', {'reservas': reservas})

def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/adicionar_reserva.html', {'form': form})

def excluir_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()
    return redirect('listar_reservas')


def index(request):
    return render(request,"reservas/index.html")