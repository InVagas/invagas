# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=2048)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100, choices=[(b'EP', b'Emprego'), (b'ES', b'Est\xc3\xa1gio')])),
                ('data_postagem', models.DateTimeField(default=datetime.datetime(2015, 9, 12, 18, 21, 42, 698751))),
                ('empresa', models.ForeignKey(to='invagasapp.Empresa')),
                ('postado_por', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
