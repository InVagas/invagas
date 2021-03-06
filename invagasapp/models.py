# coding=utf-8
from django.conf import settings

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

TIPO = (
    ('EP', 'Emprego'),
    ('ES', 'Estágio'),
)

class Empresa(models.Model):
    razao_social = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)


    def __unicode__(self):
        return self.nome

class Vagas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=2048)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=TIPO)
    data_postagem = models.DateTimeField(default=timezone.now)
    postado_por = models.ForeignKey(settings.AUTH_USER_MODEL)
    empresa_vaga = models.ForeignKey(Empresa, related_name='vagas')

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = 'vaga'
        verbose_name_plural = 'vagas'
