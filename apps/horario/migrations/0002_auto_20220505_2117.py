# Generated by Django 3.1.4 on 2022-05-05 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horario',
            old_name='prescrisao_associada',
            new_name='prescricao_associada',
        ),
    ]
