# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('invagasapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vagas',
            name='empresa',
        ),
        migrations.AlterField(
            model_name='vagas',
            name='data_postagem',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 19, 2, 39, 936342)),
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
    ]
