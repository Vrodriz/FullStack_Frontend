from flask import Flask # type: ignore
from flask_cors import CORS # type: ignore
from extensions import db

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Registrar rotas
from routes import tarefas_bp
app.register_blueprint(tarefas_bp)

@app.route('/')
def home():
    return "API de Tarefas no ar!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
