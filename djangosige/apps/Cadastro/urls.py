# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'Cadastro'
urlpatterns = [
    # Produto
    # Cadastro/produto/adicionar/
    url(r'produto/adicionar/$',
        views.AdicionarProdutoView.as_view(), name='addprodutoview'),
    # Cadastro/produto/listaprodutos
    url(r'produto/listaprodutos/$',
        views.ProdutosListView.as_view(), name='listaprodutosview'),
    # Cadastro/produto/editar/
    url(r'produto/editar/(?P<pk>[0-9]+)/$',
        views.EditarProdutoView.as_view(), name='editarprodutoview'),
]
