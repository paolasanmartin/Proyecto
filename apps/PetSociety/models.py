from django.db import models
import re
from django.db.models.deletion import PROTECT
from django.db.models.query_utils import select_related_descend

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')

# Create your models here.
class DuenosManager (models.Manager):
    
    def validacionesBasicas(self, data, ):
        errores ={}
        
        validarLongitud("nombre", data["nombre"], 3, errores)
        validarLongitud("apellido", data["apellido"],3,errores)
        validarLongitud("email", data["email"], 10, errores)
        validarLongitud("password", data["password"],8,  errores)

        if not EMAIL_REGEX.match(data["email"]):
            errores["email"] = "El email no es valido"
        
        if data["password"] !=data ["confirmarContraseña"]:
            errores["password"] = "las contraseñas no coinciden"
        
        return errores

class Duenos(models.Model):
    nombre  = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=15, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    objects = DuenosManager()   

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"  


class MascotasManager (models.Manager):
    def validacionesBasicas(self, data):
        errores ={}
        validarLongitud("nombre", data ["nombre"], errores)
        validarLongitud("sexo", data, ["sexo"],errores)
        validarLongitud("tipo", data ["tipo"],  errores)

            
        return errores

class Mascota (models.Model):
    nombre = models.CharField(max_length=50) 
    sexo = models.PositiveSmallIntegerField()
    tipo = models.CharField(max_length=10)
    duenos = models.ForeignKey(Duenos, related_name= "mascotas", on_delete= models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    
 
    def __str__(self):
        return f"{self.nombre} {self.sexo} {self.tipo}"  


class MensajeManager(models.Manager):
    def validarComentario(selft, comentario):
        error ={}
        validarLongitud("comentario", comentario.comentario, 20)

 

class Comentario(models.Model):
    comentario = models.CharField(max_length=300)
    created_at = models.DateTimeField (auto_now_add=True)
    update_at = models.DateTimeField (auto_now=True)
    

object = MensajeManager()


def validarLongitud(campo, datos, minLenght, errors):
    if (len(datos)) < minLenght:
        errors[campo] = f"El {campo} del usuario no puede ser menos a {minLenght}caracters"
