// URL da API
const apiUrl = "http://127.0.0.1:5000/tarefas";

// Elementos do DOM
const adicionarTarefaBtn = document.getElementById('adicionarTarefa');
const tarefasList = document.getElementById('tarefasList');
const tituloTarefaInput = document.getElementById('tituloTarefa');
const editarTarefaContainer = document.getElementById('editarTarefaContainer');
const tituloTarefaEditInput = document.getElementById('tituloTarefaEdit');
const atualizarTarefaBtn = document.getElementById('atualizarTarefa');
const cancelarEdicaoBtn = document.getElementById('cancelarEdicao');

// Armazenar o ID da tarefa que está sendo editada
let tarefaIdParaEditar = null;

// Função para listar todas as tarefas
async function listarTarefas() {
    try {
        const response = await fetch(apiUrl);
        const tarefas = await response.json();

        tarefasList.innerHTML = ''; // Limpar lista antes de adicionar

        tarefas.forEach(tarefa => {
            const li = document.createElement('li');
            li.innerHTML = `
                <span class="tarefa-titulo">${tarefa.titulo}</span>
                <div class="botoes">
                    <button class="edit-btn" onclick="editarTarefa(${tarefa.id})">Editar</button>
                    <button class="excluir-btn" onclick="deletarTarefa(${tarefa.id})">Deletar</button>
                </div>
            `;
            tarefasList.appendChild(li);
        });        
    } catch (error) {
        console.error('Erro ao listar tarefas:', error);
    }
}

// Função para adicionar uma nova tarefa
async function adicionarTarefa() {
    const titulo = tituloTarefaInput.value.trim();
    if (titulo) {
        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ titulo })
            });

            if (response.ok) {
                tituloTarefaInput.value = '';  // Limpar campo de input
                listarTarefas();  // Recarregar a lista de tarefas
            }
        } catch (error) {
            console.error('Erro ao adicionar tarefa:', error);
        }
    }
}

// Função para editar uma tarefa
function editarTarefa(id) {
    tarefaIdParaEditar = id;  // Salvar o ID da tarefa que será editada
    editarTarefaContainer.style.display = 'block';  // Exibir o formulário de edição

    // Buscar dados da tarefa para preencher no formulário de edição
    fetch(`${apiUrl}/${id}`)
        .then(response => response.json())
        .then(tarefa => {
            tituloTarefaEditInput.value = tarefa.titulo;  // Preencher com o título atual
        })
        .catch(error => console.error('Erro ao buscar tarefa:', error));
}

// Função para atualizar a tarefa
async function atualizarTarefa() {
    const novoTitulo = tituloTarefaEditInput.value.trim();
    if (novoTitulo && tarefaIdParaEditar !== null) {
        try {
            const response = await fetch(`${apiUrl}/${tarefaIdParaEditar}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ titulo: novoTitulo })
            });

            if (response.ok) {
                editarTarefaContainer.style.display = 'none';  // Esconder o formulário de edição
                listarTarefas();  // Recarregar a lista de tarefas
            }
        } catch (error) {
            console.error('Erro ao atualizar tarefa:', error);
        }
    }
}

// Função para cancelar a edição
function cancelarEdicao() {
    editarTarefaContainer.style.display = 'none';  // Esconder o formulário de edição
}

// Função para deletar uma tarefa
async function deletarTarefa(id) {
    try {
        const response = await fetch(`${apiUrl}/${id}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            listarTarefas();  // Recarregar a lista de tarefas após a exclusão
        }
    } catch (error) {
        console.error('Erro ao deletar tarefa:', error);
    }
}

// Inicializa a lista de tarefas ao carregar a página
window.onload = listarTarefas;

// Adiciona evento de clique para o botão "Adicionar"
adicionarTarefaBtn.addEventListener('click', adicionarTarefa);

// Adiciona evento de clique para o botão "Atualizar"
atualizarTarefaBtn.addEventListener('click', atualizarTarefa);

// Adiciona evento de clique para o botão "Cancelar"
cancelarEdicaoBtn.addEventListener('click', cancelarEdicao);
