from django.shortcuts import render
from viagens.forms import ViagemForm
from viagens.models import Viagem


def create(request):
    if request.method == 'POST':
        context = {
            'form': ViagemForm(request.POST)
        }
        return render(
            request,
            'viagens/create.html',
            context
        )

    context = {
        'form': ViagemForm()
    }
    return render(
        request,
        'viagens/create.html',
        context
    )
