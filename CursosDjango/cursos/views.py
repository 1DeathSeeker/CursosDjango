from django.shortcuts import get_object_or_404, render
from .models import Comentarios, Cursos
from .forms import ComentarioContactoForm, CursosForm

# Create your views here.
def cursos(request):
    cursos=Cursos.objects.all()
    return render(request,"cursos/cursos.html",{'cursos':cursos})

def cursosComentario(request):
    return render(request,"cursos/contacto.html")


def comentarios(request):
    comentarios=Comentarios.objects.all()
    return render(request,'cursos/consultarComentarios.html',{'comentarios':comentarios})

def guardarComentario(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #si los datos recibidos son correctos
            form.save() #Inserta
            comentarios=Comentarios.objects.all()
            return render(request,'cursos/consultarComentarios.html',{'comentarios':comentarios})
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario losdatos ingresados
    return render(request,'cursos/contacto.html',{'form':form})


def eliminarComentarioContacto(request,idcomentario, confirmacion='cursos/confirmarEliminarCom.html'):
    comentario = get_object_or_404(Comentarios, idcomentario=idcomentario)
    if request.method == 'POST':
        comentario.delete()
        comentarios=Comentarios.objects.all()
        return render(request,'cursos/consultarComentarios.html',{'comentarios':comentarios})
    return render(request, confirmacion,{'object':comentario})


def editarComentarioContacto(request,idcomentario):
    comentario = get_object_or_404(Comentarios, idcomentario=idcomentario)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=Comentarios.objects.all()
        return render(request,"cursos/consultarComentarios.html",{'comentarios':comentarios})
        
    return render(request,'cursos/editarComentario.html',{'comentario':comentario})

def eliminarCurso(request,idcurso, confirmacion='cursos/confirmarEliminarCurso.html'):
    curso = get_object_or_404(Cursos, idcurso=idcurso)
    if request.method == 'POST':
        curso.delete()
        cursos=Cursos.objects.all()
        return render(request,'cursos/cursos.html',{'cursos':cursos})
    return render(request, confirmacion,{'object':curso})

def editarCurso(request,idcurso):
    curso = get_object_or_404(Cursos, idcurso=idcurso)
    form = CursosForm(request.POST, instance=curso)
    if form.is_valid():
        form.save()
        cursos=Cursos.objects.all()
        return render(request,"cursos/cursos.html",{'cursos':cursos})
        
    return render(request,'cursos/editarCursos.html',{'curso':curso})
