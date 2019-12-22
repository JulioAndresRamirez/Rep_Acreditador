# Generated by Django 2.1.1 on 2018-10-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asistente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=12, verbose_name='Numero Identificador')),
                ('nombre', models.CharField(max_length=256, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=256, verbose_name='Apellido')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('validador', models.BooleanField(default=False, verbose_name='Estado acreditacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Asistente',
                'verbose_name_plural': 'Asistentes',
                'ordering': ['nombre', 'validador'],
            },
        ),
    ]
