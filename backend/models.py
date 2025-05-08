# Importando a instância do SQLAlchemy do arquivo 'extensions', que gerencia a conexão com o banco de dados.
from extensions import db

# Classe 'Tarefa' representa uma tabela no banco de dados.
class Tarefa(db.Model):
    
    # Definição das colunas da tabela 'Tarefa': 'id' (chave primária) e 'titulo'.
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)

    # Método que converte o objeto 'Tarefa' em um dicionário, útil para retornar como JSON.
    def to_dict(self):
        return {"id": self.id, "titulo": self.titulo}
