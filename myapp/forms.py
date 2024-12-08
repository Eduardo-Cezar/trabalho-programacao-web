from django import forms
from django.core.exceptions import ValidationError
from .models import usuarioCliente
from .models import usuarioAdministrador
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    emailLogin = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail', 'id': 'emailLogin'}),
        required=True
    )
    senhaLogin = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha', 'id': 'senhaLogin'}),
        required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        senha = cleaned_data.get('senha')

        # Verificar se o e-mail e a senha são válidos
        if email and senha:
            user = authenticate(username=email, password=senha)
            if user is None:
                raise ValidationError("E-mail ou senha incorretos.")

        return cleaned_data
    
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
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        
        # Remover todos os caracteres não numéricos
        telefoneSoNumero = ''.join(filter(str.isdigit, telefone))

        # Verificar se o telefone contém apenas números
        if len(telefoneSoNumero) != len(telefone):
            raise ValidationError("O telefone deve conter apenas números.")

        # Verificar se o telefone contém 11 caracteres
        if len(telefoneSoNumero) == 11:
            raise ValidationError("O telefone deve ter 11 dígitos.")

        return telefoneSoNumero