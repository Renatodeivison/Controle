## Instalação:

1. Instalar o [Python](https://www.python.org/downloads/)

2. Instalar dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Gere um `.env` local

    ```bash
    python contrib/env_gen.py
    ```


4. Sincronize a base de dados:

    ```bash
    python manage.py migrate
    ```

5. Crie um usuário (Administrador do sistema):

    ```bash
    python manage.py createsuperuser
    ```

6. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):

    ```bash
    python manage.py runserver
    ```

## Créditos

- [AdminBSBMaterialDesign](https://github.com/gurayyarar/AdminBSBMaterialDesign)
- [geraldo](https://github.com/marinho/geraldo)
- [jQuery-Mask-Plugin](https://igorescobar.github.io/jQuery-Mask-Plugin/)
- [DataTables](https://datatables.net/)
- [JQuery multiselect](http://loudev.com/)
- [thiagopena](https://github.com/thiagopena/djangoSIGE)