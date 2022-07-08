from django import forms
from .models import Comentarios, Cursos

class ComentarioContactoForm (forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['nombre','comentario']

class CursosForm (forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre','duracion','activo','descripcion']
