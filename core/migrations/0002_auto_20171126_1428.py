# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArquivoQuestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CursoTurma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('data_limite_entrega', models.DateField(verbose_name='Entrega')),
                ('descricao', models.TextField()),
                ('data', models.DateField()),
                ('arquivo', models.FileField(upload_to='arquivos/')),
            ],
        ),
        migrations.RenameField(
            model_name='disciplina',
            old_name='bib_basica',
            new_name='bibliografia_basica',
        ),
        migrations.RenameField(
            model_name='disciplina',
            old_name='bib_complementar',
            new_name='bibliografia_complementar',
        ),
        migrations.RenameField(
            model_name='periododisciplina',
            old_name='disciplina',
            new_name='Disciplina',
        ),
        migrations.RenameField(
            model_name='periododisciplina',
            old_name='periodo',
            new_name='Periodo',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='letra_turma',
        ),
        migrations.AddField(
            model_name='turma',
            name='turma',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disciplinaofertada',
            name='ano',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='gradecurricular',
            name='ano',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='numero',
            field=models.SmallIntegerField(unique=True),
        ),
        migrations.AddField(
            model_name='questao',
            name='Disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Disciplina'),
        ),
        migrations.AddField(
            model_name='questao',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Turma'),
        ),
        migrations.AddField(
            model_name='cursoturma',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Turma'),
        ),
        migrations.AddField(
            model_name='arquivoquestao',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Questao'),
        ),
    ]
