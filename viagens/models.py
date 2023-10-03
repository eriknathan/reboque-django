from django.contrib.auth.models import User
from django.db import models


class Seguradora(models.Model):
    class Meta:
        verbose_name = "Seguradora"
        verbose_name_plural = "Seguradoras"

    nome_seguradora = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome_seguradora}"


class Condutor(models.Model):
    class Meta:
        verbose_name = "Condutor"
        verbose_name_plural = "Condutores"

    nome = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome}"


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
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    municipio_uf = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    referencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.municipio_uf}"


class EnderecoDestino(models.Model):
    class Meta:
        verbose_name = "Endereço de Destino"
        verbose_name_plural = "Endereços de Destino"

    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    municipio_uf = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    referencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.municipio_uf}"


class Contato(models.Model):
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)  # Suponhamos que seja um campo de telefone comum
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

    sinistro = models.IntegerField(unique=True)
    data = models.DateField()
    hora = models.TimeField()
    previsao = models.CharField(max_length=40)
    condutor = models.ForeignKey(Condutor, on_delete=models.SET_NULL, null=True)
    causa_assistencia = models.CharField(max_length=60)
    descricao = models.TextField()

    # Seguradora
    seguradora = models.ForeignKey(Seguradora, on_delete=models.SET_NULL, null=True)
    solicitante = models.CharField(max_length=90, default='null')
    produto = models.CharField(max_length=90, default='null')

    # Serviço
    saida = models.DecimalField(max_digits=12, decimal_places=2)
    km_excedente = models.DecimalField(max_digits=12, decimal_places=2)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2)

    carro = models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)

    # Endereço
    endereco_ocorrencia = models.OneToOneField(EnderecoOcorrencia, on_delete=models.SET_NULL, null=True)
    endereco_destino = models.OneToOneField(EnderecoDestino, on_delete=models.SET_NULL, null=True)

    contato = models.ForeignKey(Contato, on_delete=models.SET_NULL, null=True)
    imagens = models.ManyToManyField(Imagem, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.sinistro} {self.carro.modelo} - {self.carro.placa}'
