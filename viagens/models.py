from django.contrib.auth.models import User
from django.db import models


class Seguradora(models.Model):
    class Meta:
        verbose_name = "Seguradora"
        verbose_name_plural = "Seguradoras"

    SOLICITANTE_CHOICES = [
        ('Seguradora A', 'Seguradora A'),
        ('Seguradora B', 'Seguradora B'),
        ('Seguradora C', 'Seguradora C'),
    ]

    nome_seguradora = models.CharField(max_length=20, choices=SOLICITANTE_CHOICES, verbose_name="Nome da Seguradora")
    solicitante = models.CharField(max_length=90, verbose_name="Solicitante")
    produto = models.CharField(max_length=90, verbose_name="Produto")

    def __str__(self):
        return f"{self.nome_seguradora}"


class Condutor(models.Model):
    class Meta:
        verbose_name = "Condutor"
        verbose_name_plural = "Condutores"

    nome = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome}"


class Servico(models.Model):
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    saida = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Saída (Valor)")
    km_excedente = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="KM Excedente (valor)")
    valor_total = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Valor total")

    def __str__(self):
        return f"{self.valor_total}"


class Carro(models.Model):
    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=20)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.modelo}, {self.placa}, {self.ano}"


class EnderecoOcorrencia(models.Model):
    class Meta:
        verbose_name = "Endereço da Ocorrência"
        verbose_name_plural = "Endereços da Ocorrência"

    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(max_length=255, blank=True, null=True)
    municipio_uf = models.CharField(max_length=100, verbose_name="Município / UF")
    cep = models.CharField(max_length=10)
    referencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.municipio_uf}"


class EnderecoDestino(models.Model):
    class Meta:
        verbose_name = "Endereço de Destino"
        verbose_name_plural = "Endereços de Destino"

    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(max_length=255, blank=True, null=True)
    municipio_uf = models.CharField(max_length=100, verbose_name="Município / UF")
    cep = models.CharField(max_length=10)
    referencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.municipio_uf}"


class Contato(models.Model):
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Imagem(models.Model):
    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"

    imagem = models.ImageField(upload_to='pictures/%Y/%m/')

    def __str__(self):
        return self.imagem.name


class Viagem(models.Model):
    class Meta:
        verbose_name = "Viagem"
        verbose_name_plural = "Viagens"

    # Viagem
    sinistro = models.IntegerField(unique=True, verbose_name="Sinistro")
    data = models.DateField(verbose_name="Data da Viagem")
    hora = models.TimeField(verbose_name="Hora da Viagem")
    previsao = models.CharField(max_length=40, verbose_name="Previsão")
    condutor = models.ForeignKey(Condutor, on_delete=models.SET_NULL, null=True, verbose_name="Condutor do Reboque")
    causa_assistencia = models.CharField(max_length=60, verbose_name="Causa da Assistência")
    descricao = models.TextField(verbose_name="Descrição")

    # Serviço
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True)

    # Seguradora
    seguradora = models.ForeignKey(Seguradora, on_delete=models.SET_NULL, null=True)

    # Carro
    carro = models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)

    # Contato
    contato = models.ForeignKey(Contato, on_delete=models.SET_NULL, null=True)

    # Endereço
    endereco_ocorrencia = models.OneToOneField(EnderecoOcorrencia, on_delete=models.SET_NULL, null=True)
    endereco_destino = models.OneToOneField(EnderecoDestino, on_delete=models.SET_NULL, null=True)

    imagens = models.ManyToManyField(Imagem, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.sinistro} {self.carro.modelo} - {self.carro.placa}'
