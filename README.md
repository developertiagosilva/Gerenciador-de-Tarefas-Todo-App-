# 📝 Gerenciador de Tarefas (Todo App)

Um sistema simples, prático e visual para o gerenciamento de tarefas diárias, desenvolvido para consolidar os conceitos fundamentais do framework Django e a arquitetura MVT (Model-View-Template).

## 🚀 Funcionalidades

O projeto cumpre todo o ciclo de um CRUD (Create, Read, Update, Delete) aliado a regras de negócio personalizadas:

- **Listagem Dinâmica:** Visualização de todas as tarefas cadastradas em uma tabela responsiva.
- **Ordenação Automática:** As tarefas são organizadas automaticamente pela data de entrega mais próxima utilizando a `class Meta` do Django.
- **Criação e Edição:** Formulários limpos e validados para adicionar e atualizar títulos e prazos de entrega.
- **Exclusão Segura:** Tela de confirmação antes de apagar qualquer registro do banco de dados para evitar cliques acidentais.
- **Conclusão de Tarefas:** Fluxo inteligente onde, ao clicar em "Concluir", o sistema executa um método personalizado no Model que salva automaticamente a data atual (`date.today()`) e desabilita novas alterações.

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Django 6.0** (Utilizando Class-Based Views: `ListView`, `CreateView`, `UpdateView`, `DeleteView`)
- **SQLite** (Banco de dados nativo e leve para desenvolvimento)
- **Bootstrap 5** (Para o design da interface e componentes visuais)
- **Django Crispy Forms** (Para estilização automatizada dos formulários)

## 📁 Estrutura Principal do Código

Para resolver os desafios do projeto, a lógica foi dividida de forma organizada:

* **`models.py`**: Definição da tabela `todo` com ordenação nativa e o método `mark_has_complete()` para isolar a regra de negócio no banco de dados.
* **`views.py`**: Utilização de Views baseadas em classes genéricas para acelerar o desenvolvimento e manter o código limpo.
* **`templates/`**: Páginas HTML integradas com o motor do Django, utilizando herança de template (`base.html`) para reaproveitamento de código.

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python instalado.
2. Ative o seu ambiente virtual:
   ```bash
   .venv\Scripts\activate