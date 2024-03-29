# Generated by Django 5.0.3 on 2024-03-21 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.TextField()),
                ('seccion', models.TextField()),
                ('hInicio', models.TimeField(db_column='h_inicio')),
                ('hFinal', models.TimeField(db_column='h_final')),
            ],
            options={
                'db_table': 'cursos',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField()),
                ('foto', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('pc1', models.FloatField()),
                ('pc2', models.FloatField()),
                ('pc3', models.FloatField()),
                ('examenFinal', models.FloatField(db_column='examen_final')),
                ('cursoId', models.ForeignKey(db_column='curso_id', on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='colegio.curso')),
            ],
            options={
                'db_table': 'calificaciones',
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField()),
                ('especializacion', models.TextField()),
                ('telefono', models.TextField()),
                ('foto', models.ImageField(upload_to='')),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='docentes_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='docentes_user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'docentes',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='docenteId',
            field=models.ForeignKey(db_column='docente_id', on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='colegio.docente'),
        ),
        migrations.CreateModel(
            name='CursoEstudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('cursoId', models.ForeignKey(db_column='curso_id', on_delete=django.db.models.deletion.CASCADE, to='colegio.curso')),
                ('estudianteId', models.ForeignKey(db_column='estudiante_id', on_delete=django.db.models.deletion.CASCADE, to='colegio.estudiante')),
            ],
            options={
                'db_table': 'curso_estudiante',
            },
        ),
    ]
