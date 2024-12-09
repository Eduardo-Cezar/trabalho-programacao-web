from django import forms

from .models import usuarioCliente
from .models import Prato



class LoginForm(forms.Form):
    emailLogin = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail', 'id': 'emailLogin'}),
        required=True
    )
    senhaLogin = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha', 'id': 'senhaLogin'}),
        required=True
    )
    
class CadastroForm(forms.ModelForm):
    class Meta:
        model = usuarioCliente
        fields = ['email', 'senha', 'telefone', 'bairro', 'rua', 'numero']
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail',
            'id': 'email'
        })
        )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'senha': forms.PasswordInput(),
            'placeholder': 'Digite sua senha',
            'id': 'senha'
        })
        )
    telefone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu telefone',
            'id': 'telefone'
        })
        )
    bairro = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu bairro',
            'id': 'bairro'
        })
        )
    rua = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua rua',
            'id': 'rua'
        })
        )
    numero = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o número',
            'id': 'numero'
        })
        )
    
class PratoForm(forms.ModelForm):
    class Meta:
        model = Prato
        fields = ['nome', 'preco', 'ingredientes']