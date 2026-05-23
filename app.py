"""
StudyFlow - Sistema de Gerenciamento de Tarefas Acadêmicas
Ponto de entrada da aplicação Flask.
"""

import os
from flask import Flask
from extensions import db
from routes.task_routes import task_bp


def create_app():
    """Cria e configura a instância da aplicação Flask."""

    app = Flask(__name__)

    # Configuração do banco de dados SQLite
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'sqlite:///' + os.path.join(basedir, 'instance', 'studyflow.db')
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Chave secreta para mensagens flash (altere em produção)
    app.config['SECRET_KEY'] = 'studyflow-secret-key-2024'

    # Inicializa extensões
    db.init_app(app)

    # Registra os blueprints de rotas
    app.register_blueprint(task_bp)

    # -------------------------------------------------------------------------
    # Filtros Jinja2 — geram badges HTML coloridas para prioridade e status
    # -------------------------------------------------------------------------

    @app.template_filter('priority_badge')
    def priority_badge(priority):
        """Retorna HTML de badge colorida conforme a prioridade."""
        mapping = {
            'Alta':  ('badge-priority-alta',   'bi-arrow-up-circle-fill'),
            'Média': ('badge-priority-media',  'bi-dash-circle-fill'),
            'Baixa': ('badge-priority-baixa',  'bi-arrow-down-circle-fill'),
        }
        css_class, icon = mapping.get(priority, ('bg-secondary', 'bi-circle'))
        return f'<span class="badge {css_class}"><i class="bi {icon} me-1"></i>{priority}</span>'

    @app.template_filter('status_badge')
    def status_badge(status):
        """Retorna HTML de badge colorida conforme o status."""
        mapping = {
            'Concluído':    ('badge-status-concluido',  'bi-check-circle-fill'),
            'Em Andamento': ('badge-status-andamento',  'bi-play-circle-fill'),
            'A Fazer':      ('badge-status-afazer',     'bi-circle'),
        }
        css_class, icon = mapping.get(status, ('bg-secondary', 'bi-circle'))
        return f'<span class="badge {css_class}"><i class="bi {icon} me-1"></i>{status}</span>'

    # Cria as tabelas no banco de dados se não existirem
    with app.app_context():
        os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)
        db.create_all()

    return app


# Ponto de execução direto
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
