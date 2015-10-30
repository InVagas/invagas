from django.shortcuts import render

from invagasapp.models import Vagas


def index(request):
    list_vagas = Vagas.objects.order_by('-data_postagem')[:5]
    return render(request, "../static/../templates/index.html", {'list_vagas': list_vagas})