# Generated by Django 4.0.6 on 2024-04-20 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0005_projeto_nome_alter_disciplina_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='disciplinas',
            field=models.ManyToManyField(related_name='cursos', to='curso.disciplina'),
        ),
    ]
