import sqlite3
import os

DATABASE_FILE = "data/database.db"
SCHEMA_FILE = "data/schema.sql"


def get_db_connection():
    """Retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row  # permite acessar colunas por nome
    return conn


def inicializar_db():
    """Inicializa o banco de dados criando as tabelas se necessário."""
    if not os.path.exists(DATABASE_FILE):
        print("Banco de dados não encontrado. Criando novo banco...")
        try:
            conn = get_db_connection()
            with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
                schema_sql = f.read()
            conn.executescript(schema_sql)
            conn.commit()
        except Exception as e:
            print(f"Erro ao criar o banco de dados: {e}")
            raise
        finally:
            conn.close()
        print("Banco de dados criado com sucesso.")
    else:
        print("Banco de dados já existente. OK.")
