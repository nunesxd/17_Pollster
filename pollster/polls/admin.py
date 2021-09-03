from django.contrib import admin

from .models import Question, Choice

# Podemos trocar o cabeçalho de nosso site 'admin', que por padrão fica como 'Django Administration':
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin"
admin.site.index_title = "Welcome to the Pollster Admin area !"

# A estrategia com as classes abaixo, é criar um vínculo entre as questões e as opções (que não existe se a 'registrassemos' na página diretamente).

# Abaixo utilizamos um modelo inline e em tabela, sendo que esta, irá mostrar as opções já cadastradas e mais 3 opções em branco para serem adicionadas:


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

# Abaixo, criamos a relação entre questões e opções, fazendo aparecer na página admin:
# Um campo contendo a pergunta, junto com seu texto; Outro campo contedo a data de criação; Por fim, a tabela, contendo as questões inline.


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]


# Adicionamos a nossa página 'admin', as opções de gerenciamento das questões e opções. No caso, realizamos as primeiras inserções diretamente pelo CLI do SQL:
# Esta forma não é muito interessante, pois não cria um vinculo entre as questões e as opções, sendo que existe no caso contrário, das opções podemos ver as questões associadas.
# admin.site.register(Question)
# admin.site.register(Choice)

# O register abaixo irá adicionar a classe/modelo de questões e a nossa classe customizada, onde juntamos questão com opção (vale lembrar que este link não existe no banco):
admin.site.register(Question, QuestionAdmin)
