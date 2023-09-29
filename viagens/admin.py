from django.contrib import admin

from viagens import models


@admin.register(models.Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = 'id', 'sinistro', 'carro', 'data', 'hora', 'seguradora',
    ordering = '-id',
    search_fields = 'id', 'sinistro', 'carro', 'seguradora',
    list_display_links = 'id', 'sinistro',
    list_per_page = 10
    list_max_show_all = 200


@admin.register(models.Seguradora)
class SeguradoraAdmin(admin.ModelAdmin):
    list_display = 'nome_seguradora',


@admin.register(models.Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = 'modelo', 'marca', 'ano', 'placa'


@admin.register(models.EnderecoOcorrencia)
class EnderecoOcorrenciaAdmin(admin.ModelAdmin):
    list_display = 'cep', 'rua', 'municipio_uf'


@admin.register(models.EnderecoDestino)
class EnderecoDestinoAdmin(admin.ModelAdmin):
    list_display = 'cep', 'rua', 'municipio_uf'



@admin.register(models.Condutor)
class CondutorAdmin(admin.ModelAdmin):
    list_display = 'nome',


@admin.register(models.Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'telefone', 'email'


@admin.register(models.Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = 'saida', 'km_excedente', 'valor_total'


@admin.register(models.Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = 'imagem',
