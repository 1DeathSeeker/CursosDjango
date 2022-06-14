from django.shortcuts import render,HttpResponse

# Create your views here.
menu="""
    <a href="/">Raiz></a>
    <a href="/cursos">Cursos></a>
    <a href="/contacto">Contactanos</a>
"""

def principal(request):
    contenido ="""
    <h1>Hello humans</h1>
    <p>Esta es una página de ejemplo para la actividad 1</p>
    """
    return HttpResponse(menu + contenido)

def cursos(request):
    contenido ="""
    <h1>Página de cursos</h1>
    <p>Cursos disponibles:</p>
    <p>curso 1</p>
    <p>curso 2</p>
    <p>curso 3</p>
    """
    return HttpResponse(menu + contenido)    

def contacto(request):
    contenido= """<h2>Información</h2>
    <p>Nombre: <input type="text" name="nombre"></p>
    <p>Correo: <input type="email" id="email"></p>
    <select name="Cursos" id="cursos">
    <option value="curso1">curso 1</option>
    <option value="curso2">curso 2</option>
    <option value="curso3">curso 3</option>
    </select>
    <p>Comentarios:</p>
    <p><textarea cols="30" rows="10"></textarea></p>
    <p><input type="Button" name="enviar" value="Enviar"/></p>"""
    return HttpResponse(menu + contenido)