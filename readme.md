# Sustainable Actions API

## Sobre o Projeto
Este projeto é uma API desenvolvida em Django e Django REST Framework para gerenciar a criação e execução de ações sustentáveis.

## Tecnologias Utilizadas
- Python 3
- Django 5.0.2
- Django REST Framework
- PostgreSQL (ambiente de produção)
- SQLite (ambiente de desenvolvimento)
- JWT para autenticação
- CORS Headers

## Funcionalidades
- Cadastro e gerenciamento de usuários
- Autenticação via JWT
- Criação e gestão de ações sustentáveis
- Documentação da API via Swagger

## Como Rodar o Projeto
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` e adicione:
   ```ini
   DJANGO_SECRET_KEY=sua-chave-secreta
   DEBUG=True
   ALLOWED_HOSTS=*
   ```
5. Execute as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```
6. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```
7. Acesse a API em `http://127.0.0.1:8000/`

## Documentação da API
A documentação interativa pode ser acessada em `http://127.0.0.1:8000/swagger/`.

## Autor
- [Seu Nome](https://github.com/seu-usuario)
