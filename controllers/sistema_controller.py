import os

from controllers import tarefa_controller, usuario_controller

from controllers.usuario_controller import cadastrar_usuario, verificar_existe_admin
from data.database import inicializar_db, get_db_connection
from utils.helpers import input_obrigatorio

# Variável global simples (pra armazenar o usuário logado no momento)
usuario_logado = None


def iniciar_sistema():
    """Inicializa o banco de dados e exibe mensagem inicial."""
    inicializar_db()
    print("\n===== Bem-vindo ao Sistema de Controle de Tarefas para Equipes =====\n")


def menu_login():
    limpar_tela()

    global usuario_logado

    while True:
        print("\n--- Menu Principal ---")
        print("1. Login")
        print("2. Cadastrar Usuário")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario_logado = login()
            if usuario_logado:
                print(
                    f"\nUsuário '{usuario_logado['nome']}' logado com sucesso! (tipo: {usuario_logado['tipo']})")
                if usuario_logado['tipo'] == 'admin':  # Ve se o usuario é admin ou não
                    menu_admin()
                else:
                    menu_membro()
        elif opcao == "2":
            cadastrar_usuario_flow()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def login():
    limpar_tela()

    """Autenticação flexível: ID, Nome ou Email"""
    print("\n--- Login de Usuário ---")
    entrada = input_obrigatorio("Digite seu ID, Nome ou Email: ")
    senha = input_obrigatorio("Senha: ")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM usuarios
        WHERE (CAST(id_usuario AS TEXT) = ? OR nome = ? OR email = ?)
          AND senha = ?
    """, (entrada, entrada, entrada, senha))

    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        print(f"\nBem-vindo(a), {usuario['nome']}! ({usuario['tipo']})")
        return usuario
    else:
        print("Usuário ou senha inválidos.")
        return None


def cadastrar_usuario_flow():
    limpar_tela()

    """Fluxo interativo para cadastrar novo usuário."""
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")

    # Primeiro usuário é admin
    tipo = "admin" if not verificar_existe_admin() else "membro"

    cadastrar_usuario(nome, email, senha, tipo)


def menu_membro():
    limpar_tela()

    while True:
        print("\n--- Menu Membro ---")
        print("1. Criar Tarefa")
        print("2. Atualizar Tarefa")
        print("3. Listar Tarefas")
        print("4. Ver Tarefas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa_controller.criar_tarefa_flow(usuario_logado)
        elif opcao == "2":
            tarefa_controller.atualizar_tarefa_flow(usuario_logado)
        elif opcao == "3":
            tarefa_controller.listar_tarefas_interativo()
        elif opcao == "4":
            tarefa_controller.ver_minhas_tarefas_flow(usuario_logado)
        elif opcao == "0":
            print("Logout realizado.")
            break
        else:
            print("Opção inválida.")


def menu_admin():
    limpar_tela()

    while True:
        print("\n--- Menu Admin ---")
        print("1. Criar Tarefa")
        print("2. Criar Tarefa para Membro")
        print("3. Atualizar Tarefa")
        print("4. Atualizar Tarefa de Membro")
        print("5. Atualizar Responsável Tarefa")
        print("6. Atualizar Descrição Tarefa")
        print("7. Deletar Usuário")
        print("8. Modificar Login")
        print("9. Adicionar Membro")
        print("10. Listar Todas as Tarefas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa_controller.criar_tarefa_flow(usuario_logado)
        elif opcao == "2":
            tarefa_controller.criar_tarefa_para_membro_flow()
        elif opcao == "3":
            tarefa_controller.atualizar_tarefa_flow(usuario_logado)
        elif opcao == "4":
            tarefa_controller.atualizar_tarefa_membro_flow()
        elif opcao == "5":
            tarefa_controller.atualizar_responsavel_flow(usuario_logado)
        elif opcao == "6":
            tarefa_controller.atualizar_descricao_flow(usuario_logado)
        elif opcao == "7":
            usuario_controller.deletar_usuario_flow()
        elif opcao == "8":
            usuario_controller.modificar_login_flow()
        elif opcao == "9":
            usuario_controller.adicionar_membro_flow()
        elif opcao == "10":
            tarefa_controller.listar_todas_tarefas_flow()
        elif opcao == "0":
            print("Logout realizado.")
            break
        else:
            print("Opção inválida.")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
