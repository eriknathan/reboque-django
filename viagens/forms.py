from django import forms
from django.core.exceptions import ValidationError

from . import models


class EndDestinoForm(forms.ModelForm):
    class Meta:
        model = models.EnderecoOcorrencia
        fields = ('rua', 'numero', 'complemento', 'municipio_uf', 'cep', 'referencia')

        def clean(self):
            self.add_error(
                'rua',
                ValidationError('Mensagem de erro', code='invalid')
            )


class EndOcorrenciaForm(forms.ModelForm):
    class Meta:
        model = models.EnderecoOcorrencia
        fields = ('rua', 'numero', 'complemento', 'municipio_uf', 'cep', 'referencia')

        def clean(self):
            self.add_error(
                'rua',
                ValidationError('Mensagem de erro', code='invalid')
            )


class CarroForm(forms.ModelForm):
    class Meta:
        model = models.Carro
        fields = ('modelo', 'marca', 'cor', 'placa', 'ano',)

        def clean(self):
            self.add_error(
                'placa',
                ValidationError('Mensagem de erro', code='invalid')
            )


class ContatoForm(forms.ModelForm):
    class Meta:
        model = models.Contato
        fields = ('nome', 'telefone', 'whatsapp', 'email',)

        def clean(self):
            self.add_error(
                'nome',
                ValidationError('Mensagem de erro', code='invalid')
            )


class SeguradoraForm(forms.ModelForm):
    class Meta:
        model = models.Seguradora
        fields = ('nome_seguradora', 'solicitante', 'produto',)

        def clean(self):
            self.add_error(
                'nome_seguradora',
                ValidationError('Mensagem de erro', code='invalid')
            )


class ServicoForm(forms.ModelForm):
    class Meta:
        model = models.Servico
        fields = ('saida', 'km_excedente', 'valor_total',)

        def clean(self):
            self.add_error(
                'valor_total',
                ValidationError('Mensagem de erro', code='invalid')
            )


class ViagemForm(forms.ModelForm):
    class Meta:
        model = models.Viagem
        fields = ('sinistro', 'data', 'hora', 'previsao', 'condutor', 'causa_assistencia', 'descricao',)

        def clean(self):
            # cleaned_data = self.cleaned_data

            self.add_error(
                'sinistro',
                ValidationError('Mensagem de erro', code='invalid')
            )
