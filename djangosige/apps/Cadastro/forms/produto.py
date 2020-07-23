# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from djangosige.apps.Cadastro.models import Produto


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'fornecedor': forms.TextInput(attrs={'class': 'form-control'}),
            'transmissora': forms.TextInput(attrs={'class': 'form-control'}),
            'contrato': forms.TextInput(attrs={'class': 'form-control'}),
            'nota_fiscal': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'qtn_fornecida': forms.TextInput(attrs={'class': 'form-control'}),
            'local_entrega': forms.TextInput(attrs={'class': 'form-control'}),
            'qtn_entrega': forms.TextInput(attrs={'class': 'form-control'}),
            'data_entrada': forms.TextInput(attrs={'class': 'form-control'}),
            'qtn_saida': forms.TextInput(attrs={'class': 'form-control'}),
            'data_saida': forms.TextInput(attrs={'class': 'form-control'}),
            'saldo': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'item': _('Item'),
            'fornecedor': _('Fornecedor'),
            'descricao': _('Descrição'),
            'transmissora': _('Transmissora'),
            'contrato': _('Contrato'),
            'nota_fiscal': _('Nota fiscal'),
            'codigo': _('Código'),
            'qtn_fornecida': _('Quantidade fornecida'),
            'local_entrega': _('Local entrega'),
            'qtn_entrega': _('Quantidade entrega'),
            'data_entrada': _('Data entrada'),
            'qtn_saida': _('Quantidade saida'),
            'data_saida': _('Data saida'),
            'saldo': _('Saldo'),
            'observacoes': _('Observações'),
        }
