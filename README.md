# ⋆˚✿˖° Backend - Sistema de Gestão de Ações de Marketing ⋆˚✿˖° 
Este repositório contém o backend desenvolvido com **Flask**, permitindo gerenciar ações de marketing com operações **CRUD** (*Create, Read, Update, Delete*).  
---
## 🛠 Tecnologias Utilizadas  
✧ **Flask** → Framework web para Python.  
✧ **SQLAlchemy** → ORM para interagir com o banco de dados SQLite.  
✧ **Flask-CORS** → Habilita requisições de diferentes origens (CORS).   
---
📂 Projeto  
├── 📂 backend  
│   ├── 📄 app.py  
│   ├── 📄 requirements.txt  
---
## ˚. 🎀  Como Rodar o Backend  
## ★ Pré-requisitos  

- ✔ **Python 3.7+**  
- ✔ **Pip** (gerenciador de pacotes do Python)
- ✔ **python -m venv venv**
- ✔ **venv\Scripts\activate**
- ✔ **Instale as dependências:**
- ✔ **pip install -r requirements.txt**
- ✔ **Execute o servidor Flask:**
- ✔ **python app.py**
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

