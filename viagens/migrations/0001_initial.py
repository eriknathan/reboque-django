# Generated by Django 4.2.5 on 2023-09-29 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Carro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("modelo", models.CharField(max_length=100)),
                ("marca", models.CharField(max_length=50)),
                ("cor", models.CharField(max_length=50)),
                ("placa", models.CharField(max_length=20)),
                ("ano", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Contato",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("telefone", models.CharField(max_length=15)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="EnderecoDestino",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rua", models.CharField(max_length=255)),
                ("numero", models.CharField(max_length=10)),
                (
                    "complemento",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("municipio_uf", models.CharField(max_length=100)),
                ("cep", models.CharField(max_length=10)),
                ("referencia", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="EnderecoOcorrencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rua", models.CharField(max_length=255)),
                ("numero", models.CharField(max_length=10)),
                (
                    "complemento",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("municipio_uf", models.CharField(max_length=100)),
                ("cep", models.CharField(max_length=10)),
                ("referencia", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Seguradora",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("solicitante", models.CharField(max_length=100)),
                ("produto", models.CharField(max_length=100)),
                (
                    "nome_seguradora",
                    models.CharField(
                        choices=[
                            ("Seguradora A", "Seguradora A"),
                            ("Seguradora B", "Seguradora B"),
                            ("Seguradora C", "Seguradora C"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Servico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("saida", models.IntegerField()),
                ("km_excedente", models.IntegerField()),
                ("valor_total", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="ViagemModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sinistro", models.IntegerField(unique=True)),
                ("data", models.DateField()),
                ("hora", models.TimeField()),
                ("previsao", models.CharField(max_length=40)),
                ("causa_assistencia", models.CharField(max_length=60)),
                ("descricao", models.TextField()),
                (
                    "carro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="viagens.carro"
                    ),
                ),
                (
                    "contato",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="viagens.contato",
                    ),
                ),
                (
                    "endereco_destino",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="viagens.enderecodestino",
                    ),
                ),
                (
                    "endereco_ocorrencia",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="viagens.enderecoocorrencia",
                    ),
                ),
                (
                    "seguradora",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="viagens.seguradora",
                    ),
                ),
                (
                    "servico",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="viagens.servico",
                    ),
                ),
            ],
        ),
    ]
