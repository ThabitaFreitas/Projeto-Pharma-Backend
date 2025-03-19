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
│   ├── 📄 app.py  
│   ├── 📄 requirements.txt  


---

## ˚. 🎀  Como Rodar o Backend  

## ★ Pré-requisitos  
Antes de rodar o backend, certifique-se de ter instalado:  

- ✔ **Python 3.7+**  
- ✔ **Pip** (gerenciador de pacotes do Python)  

---

## ★ Instalação  

### 1️⃣ Clone o repositório  

git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>

2️⃣ Crie um ambiente virtual (opcional)

# Criar um ambiente virtual
python -m venv venv

# Ativar no Windows
venv\Scripts\activate  

# Ativar no Linux/Mac
source venv/bin/activate  

3️⃣ Instale as dependências

pip install -r requirements.txt

4️⃣ Configure o banco de dados

O SQLite cria automaticamente um arquivo chamado site.db ao rodar o servidor pela primeira vez.

5️⃣ Execute o servidor Flask

python app.py

---
---
### ★ Endpoints ★

**GET**  
`/marketing-actions`  
Listar todas as ações  

**POST**  
`/marketing-actions`  
Criar uma nova ação  

**PATCH**  
`/marketing-actions/{id}`  
Atualizar uma ação  

**DELETE**  
`/marketing-actions/{id}`  
Deletar uma ação  



#### 🌷 Respostas 🌷

|  Código  |  Significado                 |
|------------|------------------------------|
| ** 200** | 🎉 Sucesso                    |
| ** 201** | ✨ Criado com sucesso         |
| ** 400** | ❌ Requisição inválida       |
| ** 404** | ❓ Não encontrado             |

