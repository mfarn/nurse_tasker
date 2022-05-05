# Generated by Django 3.1.4 on 2022-05-05 20:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescricao',
            fields=[
                ('id_prescricao', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_droga', models.CharField(max_length=255)),
                ('patologia', models.CharField(max_length=255)),
                ('dosagem', models.CharField(max_length=255)),
                ('status_atual', models.CharField(max_length=1)),
                ('cpf_cadastrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.usuario')),
                ('cpf_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.paciente')),
            ],
        ),
    ]