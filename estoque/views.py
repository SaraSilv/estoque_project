from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto # Supondo que você tenha um modelo Produto para armazenar os dados

def lista_produtos(request):
    # produtos = Produto.objects.all()
    # return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})
    return render(request, 'estoque/lista_produtos.html')

def stock_master(request):
    return render(request, 'stock_master.html')

def inicio(request):
    return render(request, 'inicio.html')

def produtos(request):
    return render(request, 'produtos.html')  # Certifique-se de que o caminho do template está correto

def movimentacoes(request):
    return render(request, 'movimentacoes.html')

def relatorios(request):
    return render(request, 'relatorios.html')

def contato(request):
    return render(request, 'contato.html')

def cadastrar_produto(request):
    if request.method == 'POST':
        foto = request.FILES['foto']
        codigo = request.POST['codigo']
        nome = request.POST['nome']
        quantidade = request.POST['quantidade']

        # Crie uma instância do modelo Produto e salve no banco de dados
        produto = Produto(foto=foto, codigo=codigo, nome=nome, quantidade=quantidade)
        produto.save()

        return redirect('produtos')  # Redireciona para a página de produtos

    return render(request, 'produtos.html')

def produtos_vendidos(request):
    # Lógica para gerar o relatório de produtos vendidos
    return render(request, 'produtos_vendidos.html')

def produtos_estoque(request):
    # Lógica para gerar o relatório de produtos vendidos
    return render(request, 'produtos_estoque.html')

def produtos_mais_saida(request):
    # Lógica para gerar o relatório de produtos vendidos
    return render(request, 'produtos_mais_saida.html')

def produtos_vencimento(request):
    # Lógica para gerar o relatório de produtos vendidos
    return render(request, 'produtos_vencimento.html')

def produtos_estoque_baixo(request):
    # Lógica para gerar o relatório de produtos vendidos
    return render(request, 'produtos_estoque_baixo.html')

def relatorio_entrada_produtos(request):
    # Lógica para gerar o relatório de entrada de produtos
    return render(request, 'entrada_produtos.html')

def relatorio_saida_produtos(request):
    # Lógica para gerar o relatório de saída de produtos
    return render(request, 'saida_produtos.html')

def relatorio_nome_vendedor(request):
    # Lógica para gerar o relatório de entrada de produtos
    return render(request, 'nome_vendedor.html')

def relatorio_tipo_venda(request):
    # Lógica para gerar o relatório de saída de produtos
    return render(request, 'tipo_venda.html')

def relatorio_bandeira_cartao(request):
    # Lógica para gerar o relatório de entrada de produtos
    return render(request, 'bandeira_cartao.html')

# E assim por diante para os outros relatórios...
