from django.urls import path
from . import views

urlpatterns=[
    path("", views.portada ),
    path("registro" ,views.registro),
    path("registroMascota",views.registromascotas),
    path("editar/<int:idUsuario>", views.editar),
    path("eliminar/<int:idUsuario>", views.eliminar),
    path("inicioSesion", views.inicio),
    path("home", views.home),
    path("tienda",views.tienda),
    path("mapa", views.mapa),

#     # comentarios
#     path("comentario/nuevo".views.nuevoMensaje),
#     path(),
#     path("cometario/eliminar/<int:idUsuario>".views.eliminarMensajae)
]
