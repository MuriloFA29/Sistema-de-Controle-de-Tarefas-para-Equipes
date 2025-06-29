from models.usuario import Usuario
import sqlite3
from data.database import get_db_connection
from utils.helpers import confirmar_acao


def cadastrar_usuario(nome, email, senha, tipo="membro"):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nome, email, senha, tipo) VALUES (?, ?, ?, ?)", (nome, email, senha, tipo))
    conn.commit()

    print(f"Usuário '{nome}' cadastrado com sucesso.")
    conn.close()


def autenticar_usuario(email, senha):
    """
    Verifica se existe um usuário com o email e senha fornecidos.
    Retorna um dicionário com os dados do usuário ou None se não encontrado.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        return {
            "id_usuario": usuario["id_usuario"],
            "nome": usuario["nome"],
            "email": usuario["email"],
            "tipo": usuario["tipo"]
        }
    else:
        return None


def verificar_existe_admin():
    """
    Verifica se já existe algum usuário do tipo 'admin' no banco.
    Retorna True se existir pelo menos 1 admin, False caso contrário.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE tipo = 'admin'")
    resultado = cursor.fetchone()
    conn.close()

    return resultado[0] > 0


def deletar_usuario_flow():
    """Admin deleta um usuário"""
    print("\n--- Deletar Usuário ---")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE tipo = 'membro'")
    membros = cursor.fetchall()

    if not membros:
        print("Nenhum membro encontrado.")
        conn.close()
        return

    print("Membros:")
    for m in membros:
        print(f"[{m['id_usuario']}] {m['nome']} - {m['email']}")

    id_membro = input("Digite o ID do membro a ser deletado: ")

    # Validar se o ID existe e pegar nome para confirmar
    cursor.execute(
        "SELECT nome FROM usuarios WHERE id_usuario = ? AND tipo = 'membro'", (id_membro,))
    membro = cursor.fetchone()

    if not membro:
        print("ID de membro não encontrado.")
        conn.close()
        return

    nome_membro = membro['nome']

    if confirmar_acao(f"Tem certeza que deseja deletar o usuário {nome_membro}? (s/n): "):
        cursor.execute(
            "DELETE FROM usuarios WHERE id_usuario = ? AND tipo = 'membro'", (id_membro,))
        conn.commit()
        print("Usuário deletado com sucesso.")
    else:
        print("Ação cancelada.")

    conn.close()


def adicionar_membro_flow():
    """Admin adiciona novo membro"""
    print("\n--- Adicionar Novo Membro ---")

    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    tipo = "membro"

    cadastrar_usuario(nome, email, senha, tipo)


def modificar_login_flow():
    """Admin modifica login (email/senha) de um membro"""
    print("\n--- Modificar Login de Membro ---")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE tipo = 'membro'")
    membros = cursor.fetchall()

    if not membros:
        print("Nenhum membro encontrado.")
        conn.close()
        return

    print("Membros:")
    for m in membros:
        print(f"[{m['id_usuario']}] {m['nome']} - {m['email']}")

    id_membro = input("Digite o ID do membro a modificar: ")

    cursor.execute(
        "SELECT * FROM usuarios WHERE id_usuario = ? AND tipo = 'membro'", (id_membro,))
    membro = cursor.fetchone()

    if not membro:
        print("Membro não encontrado.")
        conn.close()
        return

    novo_email = input(f"Novo email (atual: {membro['email']}): ")
    nova_senha = input("Nova senha: ")

    cursor.execute("""
        UPDATE usuarios
        SET email = ?, senha = ?
        WHERE id_usuario = ?
    """, (novo_email, nova_senha, id_membro))

    conn.commit()
    conn.close()

    print("Login do membro atualizado com sucesso!")


def listar_usuarios_simples():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id_usuario, nome, email, tipo FROM usuarios")
    usuarios = cursor.fetchall()

    print(f"{'ID':<5} {'Nome':<20} {'Email':<25} {'Tipo':<10}")
    print("-" * 60)
    for u in usuarios:
        print(f"{u[0]:<5} {u[1]:<20} {u[2]:<25} {u[3]:<10}")

    conn.close()
