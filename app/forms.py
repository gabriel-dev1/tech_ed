from django import forms

class LoginForm(forms.Form):
    nome = forms.CharField(
        label = 'Nome de Login: ',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite seu nome',
            }
        )
    )
    password = forms.CharField(
        label = 'Senha: ',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

class RegisterForm(forms.Form):
    nome = forms.CharField(
        label = 'Digite seu nome: ',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'teste',
            }
        )
    )
    email = forms.EmailField(
        label = 'Digite seu email: ',
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'teste',
            }
        )
    )
    password1 = forms.CharField(
        label = 'Digite sua senha: ',
        required = True, 
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'teste',
            }
        )
    )
    password2 = forms.CharField(
        label = 'Confirme sua senha: ',
        required = True, 
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder':  'teste',

            }
        )
    )