from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from viagens.models import Viagem


def index(request):
    viagens = Viagem.objects \
        .all() \
        .order_by('-id')

    context = {
        'viagens': viagens,
        'site_title': 'Viagens - '
    }
    return render(
        request,
        'viagens/index.html',
        context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('viagens:index')

    viagens = Viagem.objects \
        .all() \
        .filter() \
        .order_by('-id')

    context = {
        'viagens': viagens,
        'site_title': 'Viagens - '
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
        'site_title': f'{single_viagem.sinistro} - '
    }
    return render(
        request,
        'viagens/viagem.html',
        context
    )
