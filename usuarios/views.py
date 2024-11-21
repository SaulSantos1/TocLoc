from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib import messages
from .services import UsuarioService

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após login
        else:
            print("Falha na autenticação")  # Confirma se o usuário é None
            return render(request, 'autenticacao/login.html', {'error': 'Credenciais inválidas'})
    logout(request)
    return render(request, 'autenticacao/login.html')

def user_cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após cadastro
    else:
        form = CustomUserCreationForm()
    return render(request, 'autenticacao/cadastro.html', {'form': form})

@login_required
def editar_usuario(request, user_id):
    """View para edição do usuário."""
    try:
        usuario = UsuarioService.get_usuario(user_id)
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('erro')

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=usuario)
        print(form)
        if form.is_valid():
            UsuarioService.update_usuario(user_id, form.cleaned_data)
            messages.success(request, "Usuário atualizado com sucesso!")
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=usuario)

    return render(request, 'editar_usuario.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout

@login_required
def home(request):
    return render(request, 'home/home.html',{'user':request.user})
