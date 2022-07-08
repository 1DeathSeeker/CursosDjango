# Generated by Django 4.0.5 on 2022-07-08 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_alter_cursos_created_alter_cursos_idcurso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('idcomentario', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombre', models.TextField(max_length=30, verbose_name='Nombre de quien contacta')),
                ('correo', models.TextField(verbose_name='Correo electrónico')),
                ('nombrecurso', models.TextField(max_length=30, verbose_name='Nombre del Curso')),
                ('comentario', models.TextField(verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
            ],
            options={
                'verbose_name': 'comentario',
                'verbose_name_plural': 'comentarios',
                'ordering': ['-created'],
            },
        ),
    ]
