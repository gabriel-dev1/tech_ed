from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 
from django.contrib import auth, messages
from app.forms import LoginForm, RegisterForm

# Create your views here.
def index(request):
  return render(request, 'index.html')

def computer(request):
  return render(request, 'computer.html')

def software(request):
   return render(request, 'software.html')

def login(request):
  form = LoginForm()
  
  if request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      name = form['nome'].value()
      password = form['password'].value()

    user = auth.authenticate(request, username=name, password = password)

    if user is not None:
      auth.login(request, user)
      return redirect('software')
  return render(request, 'login.html', {'form': form})

def register(request):
  form = RegisterForm()

  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
        if form['password1'].value() != form['password2'].value():
          messages.error(request, 'As senhas não são iguais.')
          return redirect('register')

        name = form['nome'].value()
        email = form['email'].value()
        password = form['password1'].value()

        if User.objects.filter(username=name).exists():
                messages.error(request, 'Esse usuário já existe.')
                return redirect('register')
            
        user = User.objects.create_user(
            username= name,
            email= email,
            password = password,
            )
        user.save()
        messages.success(request, 'Cadastro efetuado.')
        return redirect('login')
  return render(request, 'register.html', {'form': form})