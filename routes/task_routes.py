"""
Rotas do sistema StudyFlow.
Gerencia todas as operações CRUD de tarefas acadêmicas.
"""

from datetime import date, datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from models.task import Task, PRIORITY_OPTIONS, STATUS_OPTIONS

# Blueprint responsável por todas as rotas de tarefas
task_bp = Blueprint('tasks', __name__)


# ---------------------------------------------------------------------------
# Dashboard
# ---------------------------------------------------------------------------

@task_bp.route('/')
def dashboard():
    """Página inicial com estatísticas e tarefas mais próximas do prazo."""

    today = date.today()
    all_tasks = Task.query.all()

    # Cálculo das estatísticas
    total_tasks = len(all_tasks)
    completed_tasks = sum(1 for t in all_tasks if t.status == 'Concluído')
    pending_tasks = sum(1 for t in all_tasks if t.status != 'Concluído')
    overdue_tasks = sum(1 for t in all_tasks if t.is_overdue())

    # Percentual de conclusão (evita divisão por zero)
    completion_percentage = (
        round((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0
    )

    # 5 tarefas não concluídas com prazo mais próximo
    upcoming_tasks = (
        Task.query
        .filter(Task.status != 'Concluído')
        .order_by(Task.due_date.asc())
        .limit(5)
        .all()
    )

    return render_template(
        'dashboard.html',
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
        overdue_tasks=overdue_tasks,
        completion_percentage=completion_percentage,
        upcoming_tasks=upcoming_tasks,
        today=today,
    )


# ---------------------------------------------------------------------------
# Listagem de tarefas
# ---------------------------------------------------------------------------

@task_bp.route('/tasks')
def list_tasks():
    """Lista todas as tarefas com filtros opcionais por disciplina e status."""

    # Lê os filtros enviados via query string
    filter_subject = request.args.get('subject', '').strip()
    filter_status = request.args.get('status', '').strip()
    filter_pending = request.args.get('pending')
    filter_overdue = request.args.get('overdue')

    query = Task.query

    if filter_subject:
        query = query.filter(Task.subject.ilike(f'%{filter_subject}%'))

    if filter_status:
        query = query.filter(Task.status == filter_status)

    if filter_pending:
        query = query.filter(Task.status.in_(["A Fazer", "Em Andamento"]))

    if filter_overdue:
        query = query.filter(Task.due_date < date.today(), Task.status != 'Concluído')

    tasks = query.order_by(Task.due_date.asc()).all()

    # Lista de disciplinas únicas para o select de filtro
    all_subjects = [
        row[0] for row in db.session.query(Task.subject).distinct().order_by(Task.subject).all()
    ]

    return render_template(
        'tasks.html',
        tasks=tasks,
        status_options=STATUS_OPTIONS,
        all_subjects=all_subjects,
        filter_subject=filter_subject,
        filter_status=filter_status,
        today=date.today(),
    )


# ---------------------------------------------------------------------------
# Cadastro de tarefa
# ---------------------------------------------------------------------------

@task_bp.route('/tasks/new', methods=['GET', 'POST'])
def new_task():
    """Exibe o formulário de cadastro e processa a criação de uma nova tarefa."""

    if request.method == 'POST':
        # Coleta os dados do formulário
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        subject = request.form.get('subject', '').strip()
        due_date_str = request.form.get('due_date', '').strip()
        priority = request.form.get('priority', '').strip()
        status = request.form.get('status', '').strip()

        # Validação dos campos obrigatórios
        errors = []

        if not title:
            errors.append('O título é obrigatório.')
        if not subject:
            errors.append('A disciplina é obrigatória.')
        if not due_date_str:
            errors.append('A data de entrega é obrigatória.')
        if priority not in PRIORITY_OPTIONS:
            errors.append('Prioridade inválida.')
        if status not in STATUS_OPTIONS:
            errors.append('Status inválido.')

        # Converte a data de string para objeto date
        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            except ValueError:
                errors.append('Formato de data inválido.')

        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template(
                'task_form.html',
                priority_options=PRIORITY_OPTIONS,
                status_options=STATUS_OPTIONS,
                form_data=request.form,
                action='new',
            )

        # Cria e salva a tarefa no banco de dados
        task = Task(
            title=title,
            description=description or None,
            subject=subject,
            due_date=due_date,
            priority=priority,
            status=status,
        )
        db.session.add(task)
        db.session.commit()

        flash('Tarefa cadastrada com sucesso!', 'success')
        return redirect(url_for('tasks.list_tasks'))

    # GET: exibe o formulário vazio
    return render_template(
        'task_form.html',
        priority_options=PRIORITY_OPTIONS,
        status_options=STATUS_OPTIONS,
        form_data={},
        action='new',
    )


# ---------------------------------------------------------------------------
# Edição de tarefa
# ---------------------------------------------------------------------------

@task_bp.route('/tasks/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    """Exibe o formulário preenchido e processa a atualização de uma tarefa."""

    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        subject = request.form.get('subject', '').strip()
        due_date_str = request.form.get('due_date', '').strip()
        priority = request.form.get('priority', '').strip()
        status = request.form.get('status', '').strip()

        # Validação
        errors = []

        if not title:
            errors.append('O título é obrigatório.')
        if not subject:
            errors.append('A disciplina é obrigatória.')
        if not due_date_str:
            errors.append('A data de entrega é obrigatória.')
        if priority not in PRIORITY_OPTIONS:
            errors.append('Prioridade inválida.')
        if status not in STATUS_OPTIONS:
            errors.append('Status inválido.')

        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            except ValueError:
                errors.append('Formato de data inválido.')

        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template(
                'task_form.html',
                priority_options=PRIORITY_OPTIONS,
                status_options=STATUS_OPTIONS,
                form_data=request.form,
                task=task,
                action='edit',
            )

        # Atualiza os campos da tarefa
        task.title = title
        task.description = description or None
        task.subject = subject
        task.due_date = due_date
        task.priority = priority
        task.status = status

        db.session.commit()

        flash('Tarefa atualizada com sucesso!', 'success')
        return redirect(url_for('tasks.list_tasks'))

    # GET: preenche o formulário com os dados atuais da tarefa
    form_data = {
        'title': task.title,
        'description': task.description or '',
        'subject': task.subject,
        'due_date': task.due_date.strftime('%Y-%m-%d'),
        'priority': task.priority,
        'status': task.status,
    }

    return render_template(
        'task_form.html',
        priority_options=PRIORITY_OPTIONS,
        status_options=STATUS_OPTIONS,
        form_data=form_data,
        task=task,
        action='edit',
    )


# ---------------------------------------------------------------------------
# Exclusão de tarefa
# ---------------------------------------------------------------------------

@task_bp.route('/tasks/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Remove uma tarefa do banco de dados após confirmação no frontend."""

    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()

    flash(f'Tarefa "{task.title}" excluída com sucesso.', 'success')
    return redirect(url_for('tasks.list_tasks'))
