from django.contrib import admin

# Register your models here.

'''
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'descripcion', 'created', 'updated') }),('Opciones Avanzadas', {'classes': ('collapse',), 'fields':('lugar', 'fecha', ('hora_inicio', 'hora_fin'))}),)
    readonly_fields = ('created', 'updated',)

'''
