"""
Modelo da tabela de tarefas acadêmicas.
Define a estrutura de dados e os valores permitidos para cada campo.
"""

from datetime import datetime, date
from extensions import db


# Opções válidas para prioridade
PRIORITY_OPTIONS = ['Baixa', 'Média', 'Alta']

# Opções válidas para status
STATUS_OPTIONS = ['A Fazer', 'Em Andamento', 'Concluído']


class Task(db.Model):
    """Representa uma tarefa acadêmica cadastrada pelo estudante."""

    __tablename__ = 'tasks'

    # Identificador único auto incrementado
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Título da tarefa (obrigatório)
    title = db.Column(db.String(150), nullable=False)

    # Descrição detalhada (opcional)
    description = db.Column(db.Text, nullable=True)

    # Disciplina/matéria relacionada (obrigatório)
    subject = db.Column(db.String(100), nullable=False)

    # Data de entrega (obrigatório)
    due_date = db.Column(db.Date, nullable=False)

    # Prioridade: Baixa, Média ou Alta (obrigatório)
    priority = db.Column(db.String(20), nullable=False)

    # Status: A Fazer, Em Andamento ou Concluído (obrigatório)
    status = db.Column(db.String(30), nullable=False, default='A Fazer')

    # Data de criação preenchida automaticamente
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def is_overdue(self):
        """Verifica se a tarefa está vencida (prazo passado e não concluída)."""
        return self.due_date < date.today() and self.status != 'Concluído'

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'
