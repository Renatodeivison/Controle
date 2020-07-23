# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView
from djangosige.apps.Cadastro.forms import ProdutoForm
from djangosige.apps.Cadastro.models import Produto


class AdicionarProdutoView(CustomCreateView):
    form_class = ProdutoForm
    template_name = "cadastro/produto/produto_add.html"
    success_url = reverse_lazy('Cadastro:listaprodutosview')
    success_message = "Material <b>%(descricao)s </b>adicionado com sucesso."
    permission_codename = 'add_produto'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(AdicionarProdutoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR MATERIAL'
        context['return_url'] = reverse_lazy('Cadastro:listaprodutosview')
        return context

    def get(self, request, *args, **kwargs):
        return super(AdicionarProdutoView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        # Tirar . dos campos decimais
        req_post = request.POST.copy()

        request.POST = req_post

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.save()

            return self.form_valid(form)

        return self.form_invalid(form)


class ProdutosListView(CustomListView):
    template_name = 'cadastro/produto/produto_list.html'
    model = Produto
    context_object_name = 'all_produtos'
    success_url = reverse_lazy('Cadastro:listaprodutosview')
    permission_codename = 'view_produto'

    def get_context_data(self, **kwargs):
        context = super(ProdutosListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'MATERIAIS CADASTRADOS'
        context['add_url'] = reverse_lazy('Cadastro:addprodutoview')
        return context


class EditarProdutoView(CustomUpdateView):
    form_class = ProdutoForm
    model = Produto
    template_name = "cadastro/produto/produto_edit.html"
    success_url = reverse_lazy('Cadastro:listaprodutosview')
    success_message = "Material <b>%(descricao)s </b>editado com sucesso."
    permission_codename = 'change_produto'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(EditarProdutoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('Cadastro:listaprodutosview')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Tirar . dos campos decimais
        req_post = request.POST.copy()

        request.POST = req_post

        form_class = self.get_form_class()
        form = form_class(request.POST, instance=self.object)

        if form.is_valid():
            self.object = form.save()
            return self.form_valid(form)

        return self.form_invalid(form)


class AdicionarOutrosBaseView(CustomCreateView):
    template_name = "base/popup_form.html"

    def get_context_data(self, **kwargs):
        context = super(AdicionarOutrosBaseView,
                        self).get_context_data(**kwargs)
        context['titulo'] = 'Adicionar ' + self.model.__name__
        return context


class EditarOutrosBaseView(CustomUpdateView):
    template_name = "base/popup_form.html"

    def get_context_data(self, **kwargs):
        context = super(EditarOutrosBaseView,
                        self).get_context_data(**kwargs)
        context['titulo'] = 'Editar {0}: {1}'.format(
            self.model.__name__, str(self.object))
        return context

