/**
 * StudyFlow — Script Principal
 * Gerencia interações do lado do cliente:
 * - Animação da barra de progresso
 * - Modal de confirmação de exclusão
 * - Validação HTML5 customizada
 * - Auto-dismiss de alertas
 */

document.addEventListener('DOMContentLoaded', function () {

  // -------------------------------------------------------------------------
  // Animação da barra de progresso no Dashboard
  // -------------------------------------------------------------------------
  const progressBar = document.getElementById('progressBar');
  if (progressBar) {
    const targetValue = parseInt(progressBar.dataset.value, 10) || 0;
    // Inicia em 0 e anima até o valor real
    progressBar.style.width = '0%';
    setTimeout(() => {
      progressBar.style.width = targetValue + '%';
    }, 200);
  }

  // -------------------------------------------------------------------------
  // Modal de confirmação de exclusão
  // Popula o modal com o título e a rota correta antes de exibir
  // -------------------------------------------------------------------------
  const deleteModal = document.getElementById('deleteModal');
  if (deleteModal) {
    deleteModal.addEventListener('show.bs.modal', function (event) {
      const button = event.relatedTarget;
      const taskId    = button.getAttribute('data-task-id');
      const taskTitle = button.getAttribute('data-task-title');

      // Atualiza o título exibido no modal
      document.getElementById('deleteTaskTitle').textContent = '"' + taskTitle + '"';

      // Define a action do formulário de exclusão
      const deleteForm = document.getElementById('deleteForm');
      deleteForm.action = '/tasks/delete/' + taskId;
    });
  }

  // -------------------------------------------------------------------------
  // Validação HTML5 customizada com Bootstrap
  // Impede envio do formulário se campos obrigatórios estiverem vazios
  // -------------------------------------------------------------------------
  const taskForm = document.getElementById('taskForm');
  if (taskForm) {
    taskForm.addEventListener('submit', function (event) {
      if (!taskForm.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      taskForm.classList.add('was-validated');
    });
  }

  // -------------------------------------------------------------------------
  // Auto-dismiss de alertas após 5 segundos
  // -------------------------------------------------------------------------
  const alerts = document.querySelectorAll('.alert.fade.show');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      bsAlert.close();
    }, 5000);
  });

});
