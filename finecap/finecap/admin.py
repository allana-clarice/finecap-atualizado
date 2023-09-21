from django.contrib import admin
from .models import Stand, Reserva

class StandAdmin(admin.ModelAdmin):
    list_display = ('localizacao', 'valor')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'nome_empresa', 'categoria_empresa', 'quitado','stand')
    

admin.site.register(Stand, StandAdmin)
admin.site.register(Reserva, ReservaAdmin)
