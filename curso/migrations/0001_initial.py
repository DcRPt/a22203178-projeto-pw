# Generated by Django 4.0.6 on 2024-04-06 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCientifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apresentacao', models.TextField()),
                ('objetivos', models.TextField()),
                ('competencias', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('ects', models.IntegerField()),
                ('curricularIUnitReadableCode', models.CharField(max_length=50)),
                ('area_cientifica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.areacientifica')),
            ],
        ),
        migrations.CreateModel(
            name='LinguagemProgramacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('conceitos_aplicados', models.TextField()),
                ('tecnologias_usadas', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='projeto_images')),
                ('video_link', models.URLField(blank=True, null=True)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('disciplina', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='curso.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('disciplinas', models.ManyToManyField(to='curso.disciplina')),
            ],
        ),
    ]
