from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .services import ReservaService
from .forms import ReservaForm

# CRUD para Reserva
@login_required
def lista_reservas(request):
    reservas = ReservaService.listar_reservas()
    for reserva in reservas:
        print(reserva.local)
    return render(request, 'lista_reservas.html', {'reservas': reservas})

@login_required
def criar_editar_reserva(request, reserva_id=None):
    reserva = ReservaService.obter_reserva(reserva_id) if reserva_id else None
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'criar_editar_reserva.html', {'form': form})

@login_required
def excluir_reserva(request, reserva_id):
    ReservaService.excluir_reserva(reserva_id)
    return redirect('listar_reservas')
