# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invagasapp', '0003_auto_20151002_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='endeco',
            new_name='endereco',
        ),
    ]
