from django.db.models import Count

from curso.models import Curso, Disciplina, AreaCientifica

Curso.objects.all().delete()
Disciplina.objects.all().delete()
AreaCientifica.objects.all().delete()

def explore_database():
    try:

        print("1. Nome das disciplinas, ordenadas alfabeticamente:")
        disciplinas_ordenadas = Disciplina.objects.order_by('nome')
        for disciplina in disciplinas_ordenadas:
            print(disciplina.nome)


        print("\n2. Nome dos cursos, ordenados alfabeticamente:")
        cursos_ordenados = Curso.objects.order_by('nome')
        for curso in cursos_ordenados:
            print(curso.nome)

        print("\n3. Todas as áreas científicas, ordenadas alfabeticamente:")
        areas_cientificas_ordenadas = AreaCientifica.objects.all().order_by('nome')
        for area in areas_cientificas_ordenadas:
            print(area.nome)

        print("\n4. Número de disciplinas por curso:")
        disciplinas_por_curso = Curso.objects.annotate(num_disciplinas=Count('disciplina'))
        for curso in disciplinas_por_curso:
            print(f"Curso: {curso.nome}, Número de disciplinas: {curso.num_disciplinas}")


        print("\n5. Nome das disciplinas e a área científica a que pertencem:")
        disciplinas_com_area = Disciplina.objects.select_related('area_cientifica')
        for disciplina in disciplinas_com_area:
            print(f"Disciplina: {disciplina.nome}, Área Científica: {disciplina.area_cientifica.nome}")


        print("\n6. Disciplinas com mais de 4 ECTS:")
        disciplinas_mais_ects = Disciplina.objects.filter(ects__gt=4)
        for disciplina in disciplinas_mais_ects:
            print(disciplina.nome)


    except Exception as e:
        print(f"Ocorreu um erro durante a exploração da base de dados: {e}")
