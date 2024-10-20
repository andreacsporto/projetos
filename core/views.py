from django.shortcuts import render, redirect
from.models import Livro

def home(request):
    livros = Livro.objects.all()
    return render(request, "index.html", {"livros": livros})

def salvar (request):
    vnome = request.POST.get("nome")
    Livro.object.create(nome=vnome)
    livros = Livro.object.all()
    return render(request, "index.html", {"livros": livros})

def editar (request, id):
    livro = Livro.object.get(id = id)
    return render(request, "update.html", {"livro": livro})

def update (request, id):
    vnome = request.POST.get("nome")
    livro = Livro.object.get(id = id)
    livro.nome = vnome
    livro.save()
    return redirect(home)
    
def delete (request, id):
    Livro = Livro.object.get(id = id)
    livro.delete()
    return redirect(home)
   
    

