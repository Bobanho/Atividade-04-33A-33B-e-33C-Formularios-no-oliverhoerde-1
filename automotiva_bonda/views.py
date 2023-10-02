from django.shortcuts import render, redirect
from .models import Agregados, Lagostas_brabas, Tabelados, Author

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

def delete_braba(request, id):
  item = Lagostas_brabas.objects.get(id = id)
  if request.method == "POST":
    if "sim" in request.POST:
      item.delete()

    return redirect('home')
  else:
    return render(request, "USure.html", context={"item":item})

def delete_Author(request, id):
  item = Author.objects.get(id = id)
  if request.method == "POST":
    if "sim" in request.POST:
      item.delete()

    return redirect('home')
  else:
    return render(request, "USure.html", context={"item":item})