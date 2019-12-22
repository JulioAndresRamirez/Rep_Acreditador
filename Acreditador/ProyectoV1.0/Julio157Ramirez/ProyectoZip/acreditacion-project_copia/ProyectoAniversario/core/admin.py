from django.contrib import admin
from .models import Asistente
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.

class AsistenteResource(resources.ModelResource):
    class Meta:
        model = Asistente
        import_id_fields = ('identificador',)
        fields = ('identificador', 'nombre', 'apellido', 'email', 'validador')
        exclude = ('created', 'updated',)

    def dehydrate_full_title(self, asistente):
        if  asistente:
            return  'Acreditado'
        else:
            return 'No acreditado'

@admin.register(Asistente)
class AsistenteAdmin(ImportExportActionModelAdmin):
    resource_class = AsistenteResource
    list_display = ('identificador', 'nombre','apellido','email', 'validador',)
    readonly_fields = ('created', 'updated',)
    list_filter = ('validador',)



