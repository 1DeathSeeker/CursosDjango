from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Cursos(models.Model): #Define la estructura de nuestra tabla
    idcurso = models.AutoField(primary_key=True,verbose_name="id") #principal auto
    nombre = models.TextField(max_length=30,verbose_name="Nombre del Curso") #Texto largo limitado
    descripcion = models.TextField(verbose_name="Descripción del Curso") #Texto largo
    activo = models.BooleanField(verbose_name="Estatus del Curso") #Booleano
    duracion = models.PositiveSmallIntegerField(verbose_name="Duración del Curso") #Int pequeño
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    updated = models.DateField(auto_now_add=True) 

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["-created"]
        #El - Ordenado del más reciente a más nuevo
    
    def __str__(self):
        return self.nombre
        #Mostrado por nombre

class Actividad(models.Model): #Define la estructura de nuestra tabla
    idActividad= models.SmallIntegerField(primary_key=True,verbose_name="Clave actividad") #principal auto
    nombre = models.TextField(max_length=30,verbose_name="Nombre de la actividad") #Texto largo limitado
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    coment = RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]
        #El - Ordenado del más reciente a más nuevo
    
    def __str__(self):
        return self.nombre
        #Mostrado por nombre

class Comentarios(models.Model): #Define la estructura de nuestra tabla
    idcomentario = models.AutoField(primary_key=True,verbose_name="id") #principal auto
    nombre = models.TextField(max_length=30,verbose_name="Nombre de quien contacta") #Texto l
    comentario = models.TextField(verbose_name="Comentario") 
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"
        ordering = ["-created"]
        #El - Ordenado del más reciente a más nuevo
    
    def __str__(self):
        return self.nombre