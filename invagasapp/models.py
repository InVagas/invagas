# coding=utf-8
from django.conf import settings

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

TIPO = (
    ('EP', 'Emprego'),
    ('ES', 'Estágio'),
)


class Vagas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=2048)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=TIPO)
    data_postagem = models.DateTimeField(default=timezone.now)
    postado_por = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.titulo
