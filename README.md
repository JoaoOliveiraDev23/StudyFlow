# StudyFlow

Sistema web para organização de estudos e gerenciamento de tarefas acadêmicas, desenvolvido como Projeto Integrador para a UNIVESP.

## Sobre

O StudyFlow foi criado para auxiliar estudantes na organização de suas atividades acadêmicas, permitindo o controle de tarefas, prazos, prioridades e acompanhamento do progresso dos estudos de forma simples e intuitiva.

A proposta surgiu a partir da identificação das dificuldades enfrentadas por estudantes universitários na gestão de compromissos acadêmicos, trabalhos, provas e atividades extracurriculares.

## Funcionalidades

* Cadastro de tarefas acadêmicas
* Edição e exclusão de tarefas
* Organização por disciplina
* Definição de prioridades (Baixa, Média e Alta)
* Controle de status (A Fazer, Em Andamento e Concluído)
* Dashboard com indicadores de produtividade
* Visualização de tarefas pendentes e concluídas
* Identificação de tarefas vencidas
* Barra de progresso baseada nas tarefas concluídas
* Interface responsiva para desktop, tablet e dispositivos móveis

## Tecnologias

* Python
* Flask
* SQLAlchemy
* SQLite
* HTML5
* CSS3
* JavaScript
* Bootstrap 5
* Git e GitHub

## Como Rodar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/studyflow.git
cd studyflow
```

Crie e ative o ambiente virtual:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Execute o projeto:

```bash
python app.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

## Estrutura do Projeto

```text
studyflow/
│
├── app.py
├── extensions.py
├── requirements.txt
│
├── models/
│   └── task.py
│
├── routes/
│   └── task_routes.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── tasks.html
│   └── task_form.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── instance/
    └── studyflow.db
```

## Objetivo Acadêmico

O projeto tem como objetivo aplicar conceitos estudados durante o curso, incluindo:

* Desenvolvimento Web com Framework
* Banco de Dados Relacional
* Programação Back-end
* Interface Web Responsiva
* Controle de Versão com Git
* Trabalho Colaborativo em Equipe

## Integrantes

* João Pedro de Oliveira Rodrigues
* João Victor Cavalcante Vilela 
* Valdemir Fernandes da Silva Filho 

## Disciplina

UNIVESP — PJI110 Projeto Integrador — Ano: 2026
