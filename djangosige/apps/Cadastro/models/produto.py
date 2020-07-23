# -*- coding: utf-8 -*-

from django.db import models


class Produto(models.Model):
    item = models.CharField(max_length=32, blank=True, null=True)
    fornecedor = models.CharField(max_length=32, null=True, blank=True)
    transmissora = models.CharField(max_length=32, null=True, blank=True)
    contrato = models.CharField(max_length=32, null=True, blank=True)
    nota_fiscal = models.CharField(max_length=32, null=True, blank=True)
    codigo = models.CharField(max_length=32, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    qtn_fornecida = models.CharField(max_length=32, null=True, blank=True)
    local_entrega = models.CharField(max_length=32, null=True, blank=True)
    qtn_entrega = models.CharField(max_length=32, null=True, blank=True)
    data_entrada = models.CharField(max_length=32, null=True, blank=True)
    qtn_saida = models.CharField(max_length=32, null=True, blank=True)
    data_saida = models.CharField(max_length=32, null=True, blank=True)
    saldo = models.CharField(max_length=32, null=True, blank=True)
    observacoes = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Produto"

    def __unicode__(self):
        s = u'%s' % self.descricao
        return s

    def __str__(self):
        s = u'%s' % self.descricao
        return s
