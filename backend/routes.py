# Importando as bibliotecas necessárias
from flask import Blueprint, request, jsonify  # type: ignore # Para criar rotas, receber dados e retornar JSON
from models import Tarefa  # Modelo de tarefa
from extensions import db  # Instância do banco de dados

# Blueprint para as rotas de tarefas
tarefas_bp = Blueprint('tarefas', __name__)

# Rota para criar uma nova tarefa (POST)
@tarefas_bp.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()  # Recebe dados JSON da requisição
    nova_tarefa = Tarefa(titulo=dados['titulo'])  # Cria uma tarefa com o título enviado
    db.session.add(nova_tarefa)  # Adiciona a tarefa ao banco de dados
    db.session.commit()  # Confirma a adição
    return jsonify(nova_tarefa.to_dict()), 201  # Retorna a tarefa criada com código 201

# Rota para listar todas as tarefas (GET)
@tarefas_bp.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = Tarefa.query.all()  # Obtém todas as tarefas do banco
    return jsonify([t.to_dict() for t in tarefas])  # Retorna as tarefas em JSON

# Rota para obter uma tarefa específica (GET)
@tarefas_bp.route('/tarefas/<int:id>', methods=['GET'])
def obter_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)  # Busca a tarefa pelo ID, retorna erro 404 se não encontrada
    return jsonify(tarefa.to_dict())  # Retorna os dados da tarefa

# Rota para atualizar uma tarefa (PUT)
@tarefas_bp.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)  # Busca a tarefa pelo ID
    dados = request.get_json()  # Recebe os dados da requisição
    tarefa.titulo = dados.get('titulo', tarefa.titulo)  # Atualiza o título
    db.session.commit()  # Salva a alteração
    return jsonify(tarefa.to_dict())  # Retorna a tarefa atualizada

# Rota para deletar uma tarefa (DELETE)
@tarefas_bp.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)  # Busca a tarefa pelo ID
    db.session.delete(tarefa)  # Deleta a tarefa
    db.session.commit()  # Confirma a exclusão
    return jsonify({'mensagem': 'Tarefa deletada com sucesso'})  # Retorna mensagem de sucesso
