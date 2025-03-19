# 🚀 Backend - Sistema de Gestão de Ações de Marketing  

Este repositório contém o backend desenvolvido com **Flask**, permitindo gerenciar ações de marketing com operações **CRUD** (*Create, Read, Update, Delete*).  

---

## 🛠 Tecnologias Utilizadas  
📌 **Flask** → Framework web para Python.  
📌 **SQLAlchemy** → ORM para interagir com o banco de dados SQLite.  
📌 **Flask-CORS** → Habilita requisições de diferentes origens (CORS).  
📌 **SQLite** → Banco de dados leve para persistência de dados.  

---

## 📂 Estrutura do Projeto  

/backend │── app.py # Arquivo principal do backend │── /migrations # Diretório de migrações do banco de dados └── requirements.txt # Dependências do projeto



---

## ▶️ Como Rodar o Backend  

### 🔹 Pré-requisitos  
Antes de rodar o backend, certifique-se de ter instalado:  
✔ **Python 3.7+**  
✔ **Pip** (gerenciador de pacotes do Python)  

### 🔹 Instalação  

1️⃣ **Clone o repositório:**  

2️⃣ Crie um ambiente virtual (opcional)

# Criar um ambiente virtual
python -m venv venv
# Ativar no Windows
venv\Scripts\activate  
# Ativar no Linux/Mac
source venv/bin/activate 

3️⃣ Instale as dependências:

pip install -r requirements.txt

4️⃣ Configure o banco de dados:

O SQLite cria automaticamente um arquivo chamado site.db ao rodar o servidor pela primeira vez.

5️⃣ Execute o servidor Flask:

python app.py


---

📡 **Endpoints da API**  
A API permite gerenciar as ações de marketing através das operações **CRUD**.


🔹 1. Listar todas as ações de marketing
GET /marketing-actions



json
[
    {
        "id": 1,
        "action": "Palestra",
        "predicted_date": "25/12/2025",
        "predicted_investment": 1000.00
    }
]
🔹 2. Criar uma nova ação de marketing
POST /marketing-actions

📤 Corpo da Requisição:

json
Copiar
Editar
{
    "action": "Evento",
    "predicted_date": "10/10/2025",
    "predicted_investment": 2000.00
}
📥 Resposta:

json
Copiar
Editar
{
    "message": "Ação de marketing criada com sucesso!"
}
🔹 3. Editar uma ação de marketing
PATCH /marketing-actions/{id}

📤 Corpo da Requisição:

json
Copiar
Editar
{
    "action": "Apoio Gráfico",
    "predicted_date": "15/11/2025",
    "predicted_investment": 1500.00
}
📥 Resposta:

json
Copiar
Editar
{
    "message": "Ação de marketing atualizada!"
}
🔹 4. Deletar uma ação de marketing
DELETE /marketing-actions/{id}

📥 Resposta:

json
Copiar
Editar
{
    "message": "Ação de marketing deletada!"
}
⚠️ Validações
🔸 Ação: Deve ser uma das opções válidas: "Palestra", "Evento", "Apoio Gráfico".
🔸 Investimento: Deve ser um número positivo.
🔸 Data: Deve seguir o formato DD/MM/AAAA e ser pelo menos 10 dias no futuro.

Se algum dado for inválido, a API retorna um erro correspondente.

📦 Dependências
As dependências do projeto estão listadas em requirements.txt:

txt
Copiar
Editar
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
Flask-CORS==3.1.1
