from django.contrib import admin
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_cientifica_nome', 'display_disciplinas')
    list_filter = ('area_cientifica__nome',)
    search_fields = ('nome', 'apresentacao', 'objetivos', 'competencias')
    
    def area_cientifica_nome(self, obj):
        return obj.area_cientifica.nome if obj.area_cientifica else 'Sem área definida'
    area_cientifica_nome.short_description = 'Área Científica'
    
    def display_disciplinas(self, obj):
        return ", ".join([d.nome for d in obj.disciplinas.all()])
    display_disciplinas.short_description = 'Disciplinas'

class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

# Admin para Disciplina
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects', 'curricular_unit_code', 'curso_nome', 'area_cientifica_nome')
    list_filter = ('ano', 'semestre', 'curso__nome', 'area_cientifica__nome')
    search_fields = ('nome', 'curso__nome', 'area_cientifica__nome')
    
    def curso_nome(self, obj):
        return obj.curso.nome if obj.curso else 'Sem curso associado'
    curso_nome.short_description = 'Curso'
    
    def area_cientifica_nome(self, obj):
        return obj.area_cientifica.nome
    area_cientifica_nome.short_description = 'Área Científica'

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina_nome', 'descricao_resumida', 'github_link')
    list_filter = ('disciplina__nome',)
    search_fields = ('nome', 'descricao', 'disciplina__nome', 'conceitos_aplicados', 'tecnologias_usadas')
    
    def disciplina_nome(self, obj):
        return obj.disciplina.nome
    disciplina_nome.short_description = 'Disciplina'
    
    def descricao_resumida(self, obj):
        return obj.descricao[:60] + "..." if len(obj.descricao) > 60 else obj.descricao
    descricao_resumida.short_description = 'Descrição'

class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'projetos_listados')
    
    def projetos_listados(self, obj):
        return ", ".join([p.nome for p in obj.projetos.all()])
    projetos_listados.short_description = 'Projetos'

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'list_disciplinas')
    search_fields = ('nome',)
    
    def list_disciplinas(self, obj):
        return ", ".join([d.nome for d in obj.disciplinas.all()])
    list_disciplinas.short_description = 'Disciplinas'

admin.site.register(Curso, CursoAdmin)
admin.site.register(AreaCientifica, AreaCientificaAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(LinguagemProgramacao, LinguagemProgramacaoAdmin)
admin.site.register(Docente, DocenteAdmin)
