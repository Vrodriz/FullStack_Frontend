# Gestão de Tarefas

Este é um sistema simples de **Gestão de Tarefas** desenvolvido com **Flask** no backend e **HTML, CSS e JavaScript** no frontend. O sistema permite a criação, listagem, edição e remoção de tarefas via API RESTful.

## ✨ Funcionalidades

- ✅ **Criar uma nova tarefa**
- 📋 **Listar tarefas cadastradas**
- 📝 **Editar tarefa existente**
- ❌ **Excluir uma tarefa**

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Banco de Dados**: SQLite (via Flask-SQLAlchemy)

## 📁 Estrutura do Projeto

```
fullstack-test/
├── backend/
│   ├── app.py              # Arquivo principal do backend (Flask)
│   ├── routes.py           # Arquivo de rotas da API
│   ├── models.py           # Modelo de dados da tarefa
│   ├── extensions.py       # Configuração do banco de dados (Flask-SQLAlchemy)
│   ├── init_db.py          # Criação manual do banco de dados (caso necessário)
│   └── requirements.txt    # Dependências do backend
├── frontend/
│   ├── index.html          # HTML do frontend
│   ├── styles.css          # Estilização da interface
│   └── script.js           # Lógica de interação com a API
```

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/fullstack-test.git
cd fullstack-test
```

### 2. Configure o ambiente do backend

```bash
cd backend
python -m venv venv
# Ative o ambiente virtual:
# No Linux/macOS:
source venv/bin/activate
# No Windows:
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

O banco de dados será criado automaticamente ao executar a aplicação. Para garantir a criação das tabelas:

```bash
python
from app import app
from extensions import db
with app.app_context():
    db.create_all()
exit()
```

> 💡 **Ou alternativamente:** execute `init_db.py` para criar o banco, caso ele não seja gerado automaticamente:
```bash
python init_db.py
```

### 5. Execute o servidor Flask

```bash
python app.py
```

Se tudo estiver certo, você verá algo como:
```
* Running on http://127.0.0.1:5000
```

### 6. Execute o frontend

- Navegue até a pasta `frontend/`
- Abra o arquivo `index.html` com o navegador (ou usando a extensão **Live Server** no VS Code para recarregamento automático)

```bash
# ou simplesmente:
code frontend/index.html
```

### 7. Interaja com o sistema

- Adicione, edite e exclua tarefas
- As tarefas aparecerão listadas dinamicamente após cada operação

## 📌 Observações

- O backend roda por padrão na porta **5000**
- O frontend consome a API REST de forma local
