# Generated by Django 3.1.4 on 2022-05-05 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ocorrencia', '0001_initial'),
        ('prescricao', '0001_initial'),
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocorrencia',
            name='prescicao_associada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescricao.prescricao'),
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='usuario_cadastrante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.usuario'),
        ),
    ]
