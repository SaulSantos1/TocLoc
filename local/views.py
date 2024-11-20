# views/local_views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .services import LocalService
from .forms import LocalEsportivoForm
from usuarios.models import Usuario

@login_required
def lista_locais(request):
    locais = LocalService.listar_locais(request.user)
    anfitriaos = LocalService.listar_anfitriaos()
    print(anfitriaos)
    return render(request, 'lista_locais.html', {'locais': locais,'anfitriaos':anfitriaos})

@login_required
def criar_local(request):
    if request.method == 'POST':
        form = LocalEsportivoForm(request.POST)
        if form.is_valid():
            print('bbb')
            LocalService.criar_local(form.cleaned_data, request.user)
            return redirect('lista_locais')
    else:
        form = LocalEsportivoForm()
        print(form)
    return render(request, 'criar_local.html', {'form': form})

@login_required
def editar_local(request, local_id):
    # Processa o formulário caso seja um POST
    if request.method == 'POST':
        # Obtém o local específico a ser editado
        local = LocalService.editar_local({}, local_id)

        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        capacidade = request.POST.get('capacidade')
        anfitriao_username = request.POST.get('anfitriao')
        
        anfitriao = Usuario.objects.get(username=anfitriao_username)

        # Atualizar o local com os dados do formulário
        local.nome = nome
        local.endereco = endereco
        local.capacidade = capacidade
        local.anfitriao = anfitriao

        # Salvar as alterações
        local.save()

        return redirect('lista_locais')  # Redireciona para a lista de locais após a edição bem-sucedida

@login_required
def excluir_local(request, local_id):
    local = LocalService.editar_local({}, local_id)
    if not local or local.anfitriao != request.user:
        return redirect('lista_locais')  # Apenas o anfitrião do local pode excluí-lo
    LocalService.excluir_local(local_id)
    return redirect('lista_locais')

@login_required
def visualizar_mapa(request):
    # Obter os parâmetros de latitude, longitude e nome da URL
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    nome = request.GET.get('nome')

    # Verificar se os dados são válidos
    if latitude and longitude:
        try:
            latitude =  float(latitude.replace(',', '.'))
            longitude = float(longitude.replace(',', '.'))
        except ValueError:
            latitude, longitude = None, None
    else:
        latitude, longitude = None, None

    print(latitude)
    print(longitude)

    # Passar os dados para o template
    return render(request, 'mapa.html', {
        'latitude': latitude,
        'longitude': longitude,
        'nome': nome
    })