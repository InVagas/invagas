# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invagasapp', '0002_auto_20150912_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('razao_social', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=20)),
                ('endeco', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='vagas',
            options={'verbose_name': 'vaga', 'verbose_name_plural': 'vagas'},
        ),
        migrations.AlterField(
            model_name='vagas',
            name='data_postagem',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vagas',
            name='empresa_vaga',
            field=models.ForeignKey(related_name='vagas', default=1, to='invagasapp.Empresa'),
            preserve_default=False,
        ),
    ]
