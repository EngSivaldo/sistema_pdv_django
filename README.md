# sistema_pdv_django

# 🛒 PDV — Sistema de Vendas

**Descrição**  
PDV é um sistema web simples em **Django** para gerenciar Produtos, Clientes, Fornecedores e Vendas (cadastro, edição, exclusão e registro de vendas).

---

## 🛠 Requisitos

- Python 3.13+
- Django 5.2+
- SQLite (padrão, para desenvolvimento)
- (Opcional) `django-widget-tweaks` para customizar widgets em templates

---

## 🚀 Instalação rápida (local)

```bash
git clone <URL_DO_REPO>
cd pdv
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# Acesse http://127.0.0.1:8000/
⚙️ Principais comandos
Migrar banco: python manage.py migrate

Criar superuser: python manage.py createsuperuser

Rodar servidor: python manage.py runserver

Atualizar dependências: pip freeze > requirements.txt

📂 Estrutura importante (resumida)
bash
Copiar código
pdv/
├── produtos/
│   └── templates/produtos/...
├── clientes/
│   └── templates/clientes/...
├── fornecedores/
│   └── templates/fornecedores/...
├── vendas/
│   └── templates/vendas/...
├── templates/
│   └── base.html
└── manage.py
🔗 Nomes de rota (use estes nomes em {% url %})
Produtos: listar_produtos, cadastrar_produto, editar_produto, excluir_produto

Clientes: listar_clientes, cadastrar_cliente, editar_cliente, excluir_cliente

Fornecedores: listar_fornecedores, cadastrar_fornecedor, editar_fornecedor, excluir_fornecedor

Vendas: fazer_venda, listar_vendas

📝 Templates & widgets
Coloque templates por app: app/templates/<app>/<template>.html

Se usar {{ field|add_class:"..." }}, instale django-widget-tweaks:

bash
Copiar código
pip install django-widget-tweaks
Adicione em settings.py:

py
Copiar código
INSTALLED_APPS += ['widget_tweaks']
Ou prefira definir classes via widgets no forms.py (recomendado).

⚠️ Erros comuns
TemplateDoesNotExist: verifique caminho e nome do template (app/templates/<app>/nome.html) e APP_DIRS = True.

NoReverseMatch: confirme que a name em {% url '...' %} existe em urls.py.

Invalid filter: 'add_class': instale django-widget-tweaks ou remova o filtro.

📦 Exemplo requirements.txt (mínimo)
shell
Copiar código
Django>=5.2,<6
django-widget-tweaks
📬 Contato / Licença
Autor: sivaldo vieira — [sivaldovieiradealmeida@gmail.com]

Licença: Uso educativo / MIT

```
