from functools import reduce
import re
from django.db.models.expressions import Value
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here
def portada(request):
    usuarios = Duenos.objects.all()
    context = {
        "usuarios": usuarios 
    }
    return render (request, 'portada.html', context)

def registro(request):
    if request.method == "GET":
        return render(request, "registro.html")
    elif request.method == "POST":
        print(request.POST)
        usuario = Duenos(
        nombre = request.POST["nombre"],
        apellido =request.POST["apellido"],
        email =request.POST["email"],
        password =request.POST["password"],
         )
   
    errores = Duenos.objects.validacionesBasicas(request.POST)
   
    if len(errores) > 0:
        print("hola mundo")
        for key, value in errores.items():
            messages.error(request,value, key)
        context ={
            "usuario": usuario
        }
        return render(request, "registro.html", context)
    else:
        usuario.save()    

    return redirect("/registroMascota")
        

def registromascotas (request):
    if request.method == "GET":
        return render(request, "registro2.html")
    elif request.method == "POST"   :
        print(request.POST)
        mascotas = Mascota(
        nombre = request.Post ["nombre"],
        sexo =request.Post ["sexo"],
        tipo =request.Post ["tipo"],
         )
   
    errores = Mascota.objects.validacionesBasicas(request.POST)
   
    if len(errores) > 0:
        for key, value in errores.item():
            messages.errores(request,value, key)
        context ={
            "mascotas": mascotas
        }
        return render(request, "registro2.html", context)
    else:
        mascotas.save()    

    return redirect("/")

def editar(request, idUsuario):
    usuario = obtenerUsuario(idUsuario)
    if usuario:
        context = {
            "usuarios" : usuario
        }
        if request.method =="GET":
            return render (request, "info.html",context)
        elif request.method =="POST":
            if esValido(request):
                usuario.nombre = request.POST["nombre"]
                usuario.apellido = request.POST["apellido"]
                usuario.email = request.POST["email"]
                usuario.password = request.POST["password"]
                usuario.save()
            else:
                return render(request, "info.html", context)
    return redirect("/")
    

def eliminar(request, idUsuario):
    usuarios = obtenerUsuario(idUsuario)
    if usuarios:
        usuarios.delete()
    return redirect ("/")


def inicio(request):
    if request.method == "GET":
         return render (request, "inicio.html" )
    elif request.method == "POST":
        usuario = obtenerUsuario(email=request.POST["email"])
        if usuario:
            request.sessiom["id"] = usuario.id
            return redirect ("/home")
        else:
            return redirect("/")
        
def tienda(request):
    return render(request,"tienda.html")

def mapa(request):
    return render(request, "mapa.html" )



def home(request):
    return render(request, "index.html")
    # if "id" in request.session:
    #     comentario = Comentario.objects.all 
    #     context ={
    #         "comentario": comentario
    #     }
    #     if request.method == "GET":
    #         return render (request, "index.html", context)
    #     elif request.method == "POST":
    #         comentario = Comentario {
    #             comentario = request.POST ["comentario"]
    #         }
    #         if esValido(request, comentario):
    #             comentario.save()
    #         else:
    #             context = {
    #                 "comentario" : comentario
    #             }
    #             return render(request, "index.html",context)
    #         return redirect ("/home")

def esValido(request):
    errores = Duenos.objects.validacionesBasicas(request.POST)
   
    if len(errores) > 0:
        
        for key, value in errores.items():
            messages.error(request,value, key)
    
def obtenerUsuario(idUsuario = None, email = None):
    try: 
        if idUsuario:
            usuarios = Duenos.objects.get(id = idUsuario)
        elif email:
            usuarios = Duenos.objects.get(email = email)
    
        return usuarios
    except:
        return None