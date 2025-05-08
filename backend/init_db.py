# Importa a instância do aplicativo e o banco de dados
from app import app
from extensions import db

# Cria o contexto do aplicativo (necessário para interagir com o banco de dados)
with app.app_context():
    # Cria todas as tabelas no banco de dados conforme definidas pelos modelos
    db.create_all()
    
    # Mensagem para confirmar que as tabelas foram criadas com sucesso
    print("Banco de dados criado com sucesso!")
