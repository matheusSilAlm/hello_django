from django.contrib import admin
from app_hellodjango.models import evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','data_evento','data_criacao')
    list_filter = ('usuario','data_evento',)

admin.site.register(evento,EventoAdmin)
