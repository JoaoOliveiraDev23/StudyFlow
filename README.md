# 📚 StudyFlow

> Sistema web para organização de estudos e gerenciamento de tarefas acadêmicas universitárias.

---

## Descrição

O **StudyFlow** permite que estudantes cadastrem, organizem e acompanhem suas tarefas acadêmicas com facilidade. O sistema oferece um dashboard com estatísticas em tempo real, filtros por disciplina e status, e indicadores visuais de prioridade e prazo.

---

## Tecnologias Utilizadas

| Camada     | Tecnologia                  |
|------------|-----------------------------|
| Backend    | Python 3, Flask             |
| ORM        | Flask-SQLAlchemy, SQLAlchemy|
| Banco      | SQLite                      |
| Frontend   | HTML5, CSS3, Bootstrap 5    |
| Scripts    | JavaScript puro             |
| Ícones     | Bootstrap Icons             |
| Fontes     | Google Fonts (Plus Jakarta Sans, DM Mono) |

---

## Estrutura do Projeto

```
studyflow/
├── app.py                  # Fábrica da aplicação Flask
├── extensions.py           # Instância compartilhada do SQLAlchemy
├── requirements.txt        # Dependências Python
├── .gitignore
├── README.md
│
├── models/
│   ├── __init__.py
│   └── task.py             # Modelo da tabela tasks
│
├── routes/
│   ├── __init__.py
│   └── task_routes.py      # Todas as rotas CRUD
│
├── templates/
│   ├── base.html           # Layout base (navbar + footer)
│   ├── dashboard.html      # Página inicial com estatísticas
│   ├── tasks.html          # Listagem com filtros
│   └── task_form.html      # Formulário de criação/edição
│
├── static/
│   ├── css/
│   │   └── style.css       # Estilos personalizados
│   └── js/
│       └── script.js       # Interações cliente
│
└── instance/
    └── studyflow.db        # Banco de dados SQLite (gerado automaticamente)
```

---

## Como Instalar e Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/studyflow.git
cd studyflow
```

### 2. Crie um ambiente virtual Python

```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python app.py
```

### 5. Acesse no navegador

```
http://localhost:5000
```

O banco de dados SQLite (`instance/studyflow.db`) será criado automaticamente na primeira execução.

---

## Rotas Disponíveis

| Método | Rota                   | Descrição                  |
|--------|------------------------|----------------------------|
| GET    | `/`                    | Dashboard                  |
| GET    | `/tasks`               | Listar tarefas             |
| GET    | `/tasks/new`           | Formulário de cadastro     |
| POST   | `/tasks/new`           | Salvar nova tarefa         |
| GET    | `/tasks/edit/<id>`     | Formulário de edição       |
| POST   | `/tasks/edit/<id>`     | Atualizar tarefa           |
| POST   | `/tasks/delete/<id>`   | Excluir tarefa             |

---

## Funcionalidades

- **Dashboard** com cards de estatísticas (total, pendentes, concluídas, vencidas) e barra de progresso animada
- **Listagem** de tarefas em tabela responsiva com filtros por disciplina e status
- **Cadastro** e **edição** de tarefas com validação de campos obrigatórios
- **Exclusão** com confirmação via modal
- **Badges** coloridas por prioridade (Alta/Média/Baixa) e status (A Fazer / Em Andamento / Concluído)
- **Alertas automáticos** com auto-dismiss após 5 segundos
- Interface totalmente **responsiva** (Desktop, Tablet, Celular)

---

## Licença

Projeto acadêmico — uso educacional.
