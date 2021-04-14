from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    create_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.CharField(max_length=200, verbose_name='Local do Evento')

    # python manage.py createsuperuser
    # python manage.py makemigrations core
    # python manage.py sqlmigrate core 0001
    # python manage.py migrate core 0001

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo
