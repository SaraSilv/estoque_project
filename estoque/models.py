from django.db import models

class Produto(models.Model):
    foto = models.ImageField(upload_to='produtos/')  # Diretório para salvar a foto do produto
    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome

class Movimentacao(models.Model):
    TIPO_MOVIMENTACAO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]
    
    TIPO_VENDA_CHOICES = [
        ('à vista', 'À vista'),
        ('parcelado', 'Parcelado')
    ]

    BANDEIRA_CARTAO_CHOICES = [
        ('VISA', 'VISA'),
        ('MASTER', 'MASTER')
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    tipo_movimentacao = models.CharField(max_length=50, choices=TIPO_MOVIMENTACAO_CHOICES, default='entrada')
    quantidade = models.IntegerField()
    vendedor_nome = models.CharField(max_length=100, blank=True, null=True)
    tipo_venda = models.CharField(max_length=50, choices=TIPO_VENDA_CHOICES, blank=True, null=True)
    bandeira_cartao = models.CharField(max_length=50, choices=BANDEIRA_CARTAO_CHOICES, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.tipo_movimentacao} - {self.produto.nome}'


class Relatorio(models.Model):
    TIPO_RELATORIO_CHOICES = [
        ('entrada', 'Entrada de Produtos'),
        ('saída', 'Saída de Produtos')
        # Adicione mais tipos de relatórios conforme necessário
    ]

    tipo_relatorio = models.CharField(max_length=50, choices=TIPO_RELATORIO_CHOICES)
    data_geracao = models.DateTimeField(auto_now_add=True)
    conteudo = models.TextField()

    def __str__(self):
        return f'Relatório {self.tipo_relatorio} - {self.data_geracao}'


class Contato(models.Model):
    equipe_suporte = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.equipe_suporte