from django.db import models


class Seguradora(models.Model):
    SOLICITANTE_CHOICES = [
        ('Seguradora A', 'Seguradora A'),
        ('Seguradora B', 'Seguradora B'),
        ('Seguradora C', 'Seguradora C'),
    ]

    solicitante = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    nome_seguradora = models.CharField(max_length=20, choices=SOLICITANTE_CHOICES)

    def __str__(self):
        return f"Solicitante: {self.solicitante}, Cliente: {self.cliente}, Produto: {self.produto}"


class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=20)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.modelo}, Placa: {self.placa}, Ano: {self.ano}"


class EnderecoOcorrencia(models.Model):
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    municipio_uf = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    referencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.municipio_uf}"


class EnderecoDestino(models.Model):
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    municipio_uf = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    referencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.municipio_uf}"


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)  # Suponhamos que seja um campo de telefone comum
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    saida = models.IntegerField()
    km_excedente = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Saida: {self.saida}, KM Excedente: {self.km_excedente}, Valor Total: {self.valor_total}"


class Viagem(models.Model):
    sinistro = models.IntegerField(unique=True)
    data = models.DateField()
    hora = models.TimeField()
    previsao = models.CharField(max_length=40)
    seguradora = models.ForeignKey(Seguradora, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    causa_assistencia = models.CharField(max_length=60)
    endereco_ocorrencia = models.OneToOneField(EnderecoOcorrencia, on_delete=models.CASCADE)
    endereco_destino = models.OneToOneField(EnderecoDestino, on_delete=models.CASCADE)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    descricao = models.TextField()
