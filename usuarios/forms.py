from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario
from django import forms

class CustomUserCreationForm(UserCreationForm):
    # Adicionando o campo de email
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'tipo_usuario']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
        }
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text=''  # Defina como vazio para não exibir
    )

    # Sobrescrevendo labels para os campos de senha
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Digite sua senha'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Digite novamente sua senha'
    )

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'profile_image']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    profile_image = forms.CharField(
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='Alterar imagem'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None