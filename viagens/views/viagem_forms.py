from django.shortcuts import render

from viagens.forms import (CarroForm, ContatoForm, EndDestinoForm,
                           EndOcorrenciaForm, SeguradoraForm, ServicoForm,
                           ViagemForm)


def create(request):
    if request.method == 'POST':
        context = {
            'form': ViagemForm(request.POST),
            'form_contact': ContatoForm(request.POST),
            'form_service': ServicoForm(request.POST),
            'form_service': SeguradoraForm(request.POST),
            'form_carro': CarroForm(request.POST),
            'form_end_ocorrencia': EndOcorrenciaForm(request.POST),
            'form_end_destino': EndDestinoForm(request.POST)
        }
        return render(
            request,
            'viagens/create.html',
            context
        )

    context = {
        'form': ViagemForm(),
        'form_contact': ContatoForm(),
        'form_service': ServicoForm(),
        'form_seguradora': SeguradoraForm(),
        'form_carro': CarroForm(),
        'form_end_ocorrencia': EndOcorrenciaForm(),
        'form_end_destino': EndDestinoForm()
    }
    return render(
        request,
        'viagens/create.html',
        context
    )
