from django import forms
from django.core.exceptions import ValidationError

from . import models


class ViagemForm(forms.ModelForm):
    # picture = forms.ImageField(
    #     widget=forms.FileInput(
    #         attrs={'accept': 'image/*'}
    #     ),
    #     required=False
    # )

    class Meta:
        model = models.Viagem
        fields = ('sinistro', 'data', 'hora', 'previsao', 'condutor', 'causa_assistencia', 'descricao',)

        def clean(self):
            # cleaned_data = self.cleaned_data

            self.add_error(
                'sinistro',
                ValidationError('Mensagem de erro', code='invalid')
            )
