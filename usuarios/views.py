from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import CustomUserCreationForm

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

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout

@login_required
def home(request):
    return render(request, 'home/home.html',{'user':request.user})
