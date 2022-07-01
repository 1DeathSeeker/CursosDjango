from django.contrib import admin
from cursos.models import Cursos
from cursos.models import Actividad

# Register your models here.

class AdministrarModeloCursos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('idcurso', 'nombre', 'activo','duracion')
    search_fields = ('idcurso','nombre','activo','duracion')
    date_hierarchy = 'created'
    list_filter = ('nombre','activo')

admin.site.register(Cursos,AdministrarModeloCursos)

class AdministrarActividades(admin.ModelAdmin):
    list_display = ('idActividad', 'nombre')
    search_fields = ('idActividad', 'coment')
    date_hierarchy = 'created'
    readonly_fields = ('created','idActividad')

admin.site.register(Actividad,AdministrarActividades)

