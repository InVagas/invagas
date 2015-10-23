from django.contrib import admin
from invagasapp.models import Vagas, Empresa


@admin.register(Vagas)
class VagasAdmin(admin.ModelAdmin):


    list_display = ('titulo', 'descricao', 'data_postagem')

    list_filter = ['data_postagem']

    search_fields = ('data_postagem', 'titulo')


admin.site.register(Empresa)