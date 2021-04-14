from django.contrib import admin
from core.models import Evento
# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'user', 'data_evento', 'create_date']
    list_filter = ['titulo', 'user', 'data_evento']


admin.site.register(Evento, EventoAdmin)
