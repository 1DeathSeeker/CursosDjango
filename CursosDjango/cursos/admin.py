from django.contrib import admin
from cursos.models import Comentarios
from cursos.models import Cursos
from cursos.models import Actividad

# Register your models here.

class AdministrarModeloCursos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('idcurso', 'nombre', 'activo','duracion')
    search_fields = ('idcurso','nombre','activo','duracion')
    date_hierarchy = 'created'
    list_filter = ('nombre','activo')
    ist_per_page=2
    list_display_links=('nombre','activo')
    list_editable=('duracion',)

admin.site.register(Cursos,AdministrarModeloCursos)

class AdministrarActividades(admin.ModelAdmin):
    list_display = ('idActividad', 'nombre')
    search_fields = ('idActividad', 'coment')
    date_hierarchy = 'created'
    readonly_fields = ('created','idActividad')

admin.site.register(Actividad,AdministrarActividades)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('idcomentario', 'nombre')
    search_fields = ('idcomentario', 'comentario')
    date_hierarchy = 'created'
    readonly_fields = ('created','idcomentario')

admin.site.register(Comentarios,AdministrarComentarios)
