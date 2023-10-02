from django.shortcuts import render, redirect
from .models import Agregados, Lagostas_brabas, Tabelados, Author
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  brabas = Lagostas_brabas.objects.all()
  agregadas = Agregados.objects.all()
  tabelados = Tabelados.objects.all()
  autor = Author.objects.all()
  return render(request, "home.html", context={"brabas": brabas, "agregadas": agregadas, "tabelados": tabelados, "autor": autor})

#template

from .forms import AuthorForm
from django.http import HttpResponse

# Campo de Formulários
@login_required
def Criar_braba(request):
  if request.method == "POST":
    Lagostas_brabas.objects.create(
      title = request.POST["title"],
      genero = request.POST["gen"],
      release_date = request.POST["data"],
      afiliacao_partidaria = request.POST["part"],
    )
    return redirect('home')
  else:
    return render(request, "brabas.html", context={"type": "Adicionar"})

@login_required
def Author_suggestion(request):
    if request.method == 'POST':
       form = AuthorForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("home")
    else:
       form = AuthorForm()
    context = {'form': form}
    return render(request, 'agregados.html', context)

# Campo dos updates

@login_required
def update_braba(request, id):
  item = Lagostas_brabas.objects.get(id = id)
  if request.method == "POST":
    item.title = request.POST["title"]
    item.genero = request.POST["gen"]
    item.release_date = request.POST["data"]
    item.afiliacao_partidaria = request.POST["part"]
    item.save()
    
    return redirect('home')
  else:
    return render(request, "brabas.html", context={"item":item, "type":"Atualizar"})

@login_required
def update_Author(request, id):
  item = Author.objects.get(id = id)
  if request.method == "POST":
    item.title = request.POST["title"]
    item.origem = request.POST["origem"]
    item.save()
    
    return redirect('home')
  else:
    return render(request, "Author.html", context={"item":item, "type":"Atualizar"})

#Campo dos delets

@login_required
def delete_braba(request, id):
  item = Lagostas_brabas.objects.get(id = id)
  if request.method == "POST":
    if "sim" in request.POST:
      item.delete()

    return redirect('home')
  else:
    return render(request, "USure.html", context={"item":item})

@login_required
def delete_Author(request, id):
  item = Author.objects.get(id = id)
  if request.method == "POST":
    if "sim" in request.POST:
      item.delete()

    return redirect('home')
  else:
    return render(request, "USure.html", context={"item":item})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(request.POST["username"],
    request.POST["email"],
    request.POST["password"])
    
    user.save
    
    return redirect("home")
  
  return render(request,"register.html", context={"action": "adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")