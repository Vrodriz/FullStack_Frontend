# Importa a classe SQLAlchemy do flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy # type: ignore

# Cria uma instância de SQLAlchemy, que será usada para interagir com o banco de dados
db = SQLAlchemy()
