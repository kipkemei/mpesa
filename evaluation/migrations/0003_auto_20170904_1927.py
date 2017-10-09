# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-04 19:27
from __future__ import unicode_literals

from django.db import migrations, models

import evaluation.models
import evaluation.validators


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0002_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(default=1, upload_to=evaluation.models.upload_location, validators=[evaluation.validators.FileValidator(content_types=('application/pdf',), max_size=5120000, min_size=1024)], verbose_name='Atach a File'),
            preserve_default=False,
        ),
    ]
