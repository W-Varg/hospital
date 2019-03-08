from django.contrib import admin
from .models import Persona
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    #ordering = ['nombre']
    list_display = ('nombre','apellido_p','apellido_m','carnet','tipo_seguro','region')
    search_fields = ['nombre','apellido_p','apellido_m','carnet','tipo_seguro','region']
    # list_filter = ('region','carnet')

admin.site.register(Persona,PersonAdmin)