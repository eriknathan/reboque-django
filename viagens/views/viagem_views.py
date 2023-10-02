from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from viagens.models import Viagem


def index(request):
    viagens = Viagem.objects \
        .all() \
        .order_by('-id')

    paginator = Paginator(viagens, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
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

    filters = (
        Q(sinistro__icontains=search_value)
        | Q(seguradora__nome_seguradora__icontains=search_value)
        | Q(carro__modelo__icontains=search_value)
        | Q(carro__placa__icontains=search_value)
        | Q(contato__nome__icontains=search_value)
        | Q(data__icontains=search_value)
    )

    viagens = Viagem.objects \
        .all() \
        .filter(filters) \
        .order_by('-id')

    paginator = Paginator(viagens, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
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
