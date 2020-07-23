# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import render

from djangosige.apps.Cadastro.models import Produto

from datetime import datetime


class IndexView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        quantidade_cadastro = {}
        data_atual = datetime.now().date()

        context['data_atual'] = data_atual.strftime('%d/%m/%Y')

        quantidade_cadastro['produtos'] = Produto.objects.all().count()
        context['quantidade_cadastro'] = quantidade_cadastro

        return context


def handler404(request):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
