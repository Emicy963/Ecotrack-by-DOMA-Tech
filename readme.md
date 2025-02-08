# Sustainable Actions API

## Sobre o Projeto
Este projeto é uma API desenvolvida em Django e Django REST Framework para gerenciar a criação e execução de ações sustentáveis. O sistema permite que usuários registrem e acompanhem suas ações sustentáveis, contribuindo para um mundo mais consciente ambientalmente.

## Tecnologias Utilizadas
- Python 3.12
- Django 5.0.2
- Django REST Framework
- PostgreSQL (ambiente de produção)
- SQLite (ambiente de desenvolvimento)
- JWT para autenticação
- CORS Headers
- drf-yasg para documentação Swagger
- WhiteNoise para servir arquivos estáticos
- Gunicorn como servidor WSGI

## Funcionalidades
- Cadastro e gerenciamento de usuários
- Autenticação via JWT (JSON Web Tokens)
- Criação e gestão de ações sustentáveis
- Documentação interativa da API via Swagger/ReDoc
- Sistema de refresh token
- Proteção CORS configurada
- Interface administrativa Django

## Endpoints da API

### Autenticação
- `POST /api/token/` - Obter token de acesso
- `POST /api/token/refresh/` - Renovar token de acesso

### Usuários
- `POST /api/users/register/` - Registro de novo usuário
- `GET /api/users/profile/` - Obter perfil do usuário
- `PUT /api/users/profile/` - Atualizar perfil do usuário

### Ações Sustentáveis
- `GET /api/actions/` - Listar ações sustentáveis
- `POST /api/actions/` - Criar nova ação sustentável
- `GET /api/actions/{id}/` - Detalhes de uma ação específica
- `PUT /api/actions/{id}/` - Atualizar ação
- `DELETE /api/actions/{id}/` - Deletar ação

### Documentação
- `/swagger/` - Documentação Swagger UI
- `/redoc/` - Documentação ReDoc
- `/swagger.json` - Documentação no formato JSON

## Como Rodar o Projeto

### Localmente
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

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
