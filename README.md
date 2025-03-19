# ⋆˚✿˖° Backend - Sistema de Gestão de Ações de Marketing ⋆˚✿˖° 

Este repositório contém o backend desenvolvido com **Flask**, permitindo gerenciar ações de marketing com operações **CRUD** (*Create, Read, Update, Delete*).  

---

## 🛠 Tecnologias Utilizadas  
✧ **Flask** → Framework web para Python.  
✧ **SQLAlchemy** → ORM para interagir com o banco de dados SQLite.  
✧ **Flask-CORS** → Habilita requisições de diferentes origens (CORS).  
✧ **SQLite** → Banco de dados leve para persistência de dados.  

---

📂 Projeto
 ├── 📂 backend
 │   ├── 📄 app.py           # Arquivo principal do backend
 │   ├── 📄 requirements.txt # Dependências do projeto



---

## ˚. 🎀  Como Rodar o Backend  

### ★ Pré-requisitos  
Antes de rodar o backend, certifique-se de ter instalado:  
✔ **Python 3.7+**  
✔ **Pip** (gerenciador de pacotes do Python)  

### ★ Instalação  

**Clone o repositório:** 

 #Crie um ambiente virtual (opcional)

# Criar um ambiente virtual
python -m venv venv
# Ativar no Windows
venv\Scripts\activate  
# Ativar no Linux/Mac
source venv/bin/activate 

 #Instale as dependências:

 pip install -r requirements.txt

 Configure o banco de dados:

 O SQLite cria automaticamente um arquivo chamado site.db ao rodar o servidor pela primeira vez.

Execute o servidor Flask:

python app.py


---
---
### ★ Endpoints ★

|  Método  |  Endpoint                     |  Descrição                |
| ** GET**  | `/marketing-actions`           |  Listar todas as ações   |
| ** POST** | `/marketing-actions`           |  Criar uma nova ação     |
| ** PATCH** | `/marketing-actions/{id}`     |  Atualizar uma ação     |
| ** DELETE** | `/marketing-actions/{id}`    |  Deletar uma ação       |

---
### 🌺 Exemplos de Requisição 🌺

#### 🎀 Criar uma nova ação 🎀
```http
POST /marketing-actions
```
📌 **Corpo:**
```json
{
  "action": "Evento",
  "predicted_date": "25/03/2025",
  "predicted_investment": 2000.00
}
```

#### 💕 Atualizar uma ação 💕
```http
PATCH /marketing-actions/{id}
```
📌 **Corpo:**
```json
{
  "action": "Apoio Gráfico",
  "predicted_date": "30/03/2025",
  "predicted_investment": 1800.00
}
```

#### 🌷 Respostas 🌷

|  Código  |  Significado                 |
|------------|------------------------------|
| ** 200** | 🎉 Sucesso                    |
| ** 201** | ✨ Criado com sucesso         |
| ** 400** | ❌ Requisição inválida       |
| ** 404** | ❓ Não encontrado             |

