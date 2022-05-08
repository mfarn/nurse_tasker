# Generated by Django 3.1.4 on 2022-05-08 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prescricao', '0003_auto_20220508_0003'),
        ('ocorrencia', '0002_auto_20220505_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocorrencia',
            name='cpf_paciente',
        ),
        migrations.RemoveField(
            model_name='ocorrencia',
            name='id_ocorrencia',
        ),
        migrations.RemoveField(
            model_name='ocorrencia',
            name='prescicao_associada',
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='prescricao_associada',
            field=models.ForeignKey(default='3ea99c03-da33-4030-91f8-d27554615dd3', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='prescricao.prescricao'),
            preserve_default=False,
        ),
    ]
