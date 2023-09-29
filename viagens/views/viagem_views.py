from django.http import Http404
from django.shortcuts import get_object_or_404, render

from viagens.models import Viagem


def index(request):
    viagens = Viagem.objects \
        .all() \
        .order_by('-id')

    context = {
        'viagens': viagens,
    }
    return render(
        request,
        'viagens/index.html',
        context
    )


def viagem(request, viagem_id):
    # single_viagem = Viagem.objects.filter(pk=viagem_id).first()
    single_viagem = get_object_or_404(Viagem.objects.filter(pk=viagem_id))

    context = {
        'viagens': single_viagem,
    }
    return render(
        request,
        'viagens/viagem.html',
        context
    )
