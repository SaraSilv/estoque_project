from django.contrib import admin
from django.urls import path
from . import views # Corrija para o nome do seu aplicativo

urlpatterns = [
    # path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('admin/', admin.site.urls),
    path('stock_master/', views.stock_master, name='stock_master'),
    path('', views.inicio, name='inicio'),
    path('produtos/', views.produtos, name='produtos'),
    path('movimentacoes/', views.movimentacoes, name='movimentacoes'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('contato/', views.contato, name='contato'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtos-vendidos/', views.produtos_vendidos, name='produtos_vendidos'),
    path('produtos-estoque/', views.produtos_estoque, name='produtos_estoque'),
    path('produtos-mais-saida/', views.produtos_mais_saida, name='produtos_mais_saida'),
    path('produtos-vencimento/', views.produtos_vencimento, name='produtos_vencimento'),
    path('produtos-estoque-baixo', views.produtos_estoque_baixo, name='produtos_estoque_baixo'),
    path('relatorio/entrada-produtos/', views.relatorio_entrada_produtos, name='relatorio_entrada_produtos'),
    path('relatorio/saida-produtos/', views.relatorio_saida_produtos, name='relatorio_saida_produtos'),
    path('relatorio/nome-vendedor/', views.relatorio_nome_vendedor, name='relatorio_nome_vendedor'),
    path('relatorio/tipo-venda/', views.relatorio_tipo_venda, name='relatorio_tipo_venda'),
    path('relatorio/bandeira-cartao/', views.relatorio_bandeira_cartao, name='relatorio_bandeira_cartao'),
    # Adicione outras URLs aqui
]