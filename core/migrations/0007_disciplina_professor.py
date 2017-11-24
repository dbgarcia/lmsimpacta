# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 19:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('carga_horaria', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Disciplina')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.usuario',),
        ),
    ]
