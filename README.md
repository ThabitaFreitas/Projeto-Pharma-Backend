# Projeto de Sistema - Backend (Flask)

Este repositório contém o backend desenvolvido com **Flask** para gerenciar ações de marketing, onde você pode realizar operações como cadastrar, editar, deletar e listar ações de marketing.

## Tecnologias Utilizadas

- **Flask** - Framework web para Python.
- **SQLAlchemy** - ORM para interagir com o banco de dados SQLite.
- **Flask-CORS** - Para permitir requisições de diferentes origens (CORS).
- **SQLite** - Banco de dados leve para persistência de dados.

---

## Estrutura do Projeto

A estrutura do projeto backend é simples e organizada:

/backend │ ├── app.py # Arquivo principal do backend ├── /migrations # Diretório de migrações do banco de dados └── requirements.txt # Dependências do projeto

yaml
Copy

---

## Como Rodar o Backend

### Pré-requisitos

Antes de rodar o backend, tenha certeza de que as seguintes ferramentas estão instaladas:

- **Python 3.7+**
- **Pip** (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-REPOSITORIO/backend.git
   cd backend
Crie um ambiente virtual (recomendado):

bash
Copy
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
Copy
pip install -r requirements.txt
Certifique-se de que o banco de dados esteja configurado corretamente. O código usa um banco de dados SQLite chamado site.db que será criado automaticamente ao rodar o servidor pela primeira vez.

Executando o Servidor
Inicie o servidor Flask:
bash
Copy
python app.py
O servidor estará disponível em http://localhost:5153.

Endpoints da API
A API permite realizar operações CRUD (Create, Read, Update, Delete) para as ações de marketing.

GET /marketing-actions
Retorna todas as ações de marketing cadastradas.

Resposta:

json
Copy
[
    {
        "id": 1,
        "action": "Palestra",
        "predicted_date": "25/12/2025",
        "predicted_investment": 1000.00
    },
    ...
]
POST /marketing-actions
Cria uma nova ação de marketing.

Corpo da Requisição (JSON):

json
Copy
{
    "action": "Evento",
    "predicted_date": "10/10/2025",
    "predicted_investment": 2000.00
}
Resposta:

json
Copy
{}
DELETE /marketing-actions/{id}
Deleta uma ação de marketing pelo ID.

Resposta:

json
Copy
{
    "message": "Ação de marketing deletada!"
}
PATCH /marketing-actions/{id}
Atualiza uma ação de marketing existente.

Corpo da Requisição (JSON):

json
Copy
{
    "action": "Apoio Gráfico",
    "predicted_date": "15/11/2025",
    "predicted_investment": 1500.00
}
Resposta:

json
Copy
{
    "message": "Ação de marketing atualizada!"
}
Validações
Ao enviar dados para criar ou atualizar uma ação de marketing, as seguintes validações são aplicadas:

Ação: Deve ser uma das opções válidas: "Palestra", "Evento", "Apoio Gráfico".
Investimento: Deve ser um número positivo.
Data: A data deve estar no formato dd/mm/yyyy e deve ser pelo menos 10 dias à frente da data atual.
Se algum desses campos for inválido, a API retornará um erro com a mensagem correspondente.

Dependências
As dependências do projeto estão listadas no arquivo requirements.txt:

txt
Copy
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
Flask-CORS==3.1.1