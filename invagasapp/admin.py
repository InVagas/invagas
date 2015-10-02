from django.contrib import admin
from invagasapp.models import Vagas


class VagasAdmin(admin.ModelAdmin):


    list_display = ('titulo', 'descricao', 'data_postagem')

    list_filter = ['data_postagem']

    search_fields = ('data_postagem', 'titulo')

admin.site.register(Vagas, VagasAdmin)
