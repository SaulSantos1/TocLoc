from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DisponibilidadeForm
from .services import DisponibilidadeService

@login_required
def listar_disponibilidades(request):
    disponibilidades = DisponibilidadeService.listar_disponibilidades()
    print("aqui ", disponibilidades)
    return render(request, 'listar_disponibilidades.html', {'disponibilidades': disponibilidades})

@login_required
def criar_editar_disponibilidade(request, disponibilidade_id=None):
    disponibilidade = (
        DisponibilidadeService.buscar_disponibilidade_por_id(disponibilidade_id)
        if disponibilidade_id else None
    )
    
    if request.method == 'POST':
        form = DisponibilidadeForm(request.POST, instance=disponibilidade)
        if form.is_valid():
            DisponibilidadeService.criar_ou_atualizar_disponibilidade(form.cleaned_data, disponibilidade)
            return redirect('listar_disponibilidades')
    else:
        form = DisponibilidadeForm(instance=disponibilidade)

    return render(request, 'criar_editar_disponibilidade.html', {'form': form})

@login_required
def excluir_disponibilidade(request, disponibilidade_id):
    sucesso = DisponibilidadeService.excluir_disponibilidade(disponibilidade_id)
    if sucesso:
        return redirect('listar_disponibilidades')
    else:
        return render(request, 'erro.html', {'mensagem': 'Disponibilidade não encontrada.'})
