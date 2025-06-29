from controllers.usuario_controller import listar_usuarios_simples
from data.database import get_db_connection
from utils.helpers import registrar_log_tarefa


def criar_tarefa_flow(usuario_logado):
    """Fluxo para criar uma nova tarefa"""
    print("\n--- Criar Nova Tarefa ---")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    status = "A fazer"
    while True:
        prioridade = input("Prioridade (Alta / Média / Baixa): ").capitalize()
        if prioridade in ["Alta", "Média", "Baixa"]:
            break
        print("Prioridade inválida, tente novamente.")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tarefas (titulo, descricao, status, prioridade, responsavel_id, responsavel_nome)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, descricao, status, prioridade, usuario_logado["id_usuario"], usuario_logado["nome"]))

    id_tarefa = cursor.lastrowid

    conn.commit()
    conn.close()

    print("Tarefa criada com sucesso!")

    registrar_log_tarefa(
        id_tarefa,
        f"Tarefa criada - Título: {titulo}, Status: {status}, Prioridade: {prioridade}, Responsável: {usuario_logado["nome"]} (ID: {usuario_logado["id_usuario"]}), Criado por: {usuario_logado['nome']} (ID: {usuario_logado['id_usuario']})"
    )


def atualizar_tarefa_flow(usuario_logado):
    """Fluxo para atualizar uma tarefa"""
    print("\n--- Atualizar Tarefa ---")

    conn = get_db_connection()
    cursor = conn.cursor()

    # Mostra lista de tarefas do usuário logado
    cursor.execute("""
        SELECT * FROM tarefas
        WHERE responsavel_id = ?
    """, (usuario_logado["id_usuario"],))

    tarefas = cursor.fetchall()

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        conn.close()
        return

    print("\nTarefas:")
    for t in tarefas:
        print(
            f"[{t['id_tarefa']}] {t['titulo']} - {t['status']} - Prioridade: {t['prioridade']}")

    try:
        id_tarefa = int(
            input("\nDigite o ID da tarefa que deseja atualizar: "))
    except ValueError:
        print("ID inválido! Digite um número.")
        return

    # Verifica se a tarefa existe e pertence ao usuário
    cursor.execute("""
        SELECT * FROM tarefas
        WHERE id_tarefa = ? AND responsavel_id = ?
    """, (id_tarefa, usuario_logado["id_usuario"]))

    tarefa = cursor.fetchone()

    if not tarefa:
        print("Tarefa não encontrada ou você não tem permissão para editá-la.")
        conn.close()
        return

    while True:
        novo_status = input("Novo status (A fazer / Concluído): ").capitalize()
        if novo_status in ["A fazer", "Concluído"]:
            break
        print("Prioridade inválida, tente novamente.")

    while True:
        nova_prioridade = input(
            "Nova prioridade (Alta / Média / Baixa): ").capitalize()
        if nova_prioridade in ["Alta", "Média", "Baixa"]:
            break
        print("Prioridade inválida, tente novamente.")

    cursor.execute("""
        UPDATE tarefas
        SET status = ?, prioridade = ?
        WHERE id_tarefa = ?
    """, (novo_status, nova_prioridade, id_tarefa))

    conn.commit()
    conn.close()

    print("Tarefa atualizada com sucesso!")

    registrar_log_tarefa(
        id_tarefa,
        f"Tarefa atualizada - Novo status: {novo_status}, Nova prioridade: {nova_prioridade}, Alterado por: {usuario_logado['nome']} (ID: {usuario_logado['id_usuario']})"
    )


def atualizar_tarefa_membro_flow():
    """Admin atualiza tarefas de membros"""
    print("\n--- Atualizar Tarefa de Membro ---")

    conn = get_db_connection()
    cursor = conn.cursor()

    # Listar tarefas de todos os membros
    cursor.execute("""
        SELECT * FROM tarefas
    """)

    tarefas = cursor.fetchall()

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        conn.close()
        return

    print("\nTarefas:")
    for t in tarefas:
        print(f"[{t['id_tarefa']}] {t['titulo']} - {t['status']} - Prioridade: {t['prioridade']} - Responsável: {t['responsavel_nome']}")

    try:
        id_tarefa = int(input("Digite o ID da tarefa a atualizar: "))
    except ValueError:
        print("ID inválido! Digite um número.")
        return

    cursor.execute("""
        SELECT * FROM tarefas
        WHERE id_tarefa = ?
    """, (id_tarefa,))

    tarefa = cursor.fetchone()

    if not tarefa:
        print("Tarefa não encontrada.")
        conn.close()
        return

    novo_status = input("Novo status (A fazer / Concluído): ").capitalize()
    nova_prioridade = input(
        "Nova prioridade (Alta / Média / Baixa): ").capitalize()

    cursor.execute("""
        UPDATE tarefas
        SET status = ?, prioridade = ?
        WHERE id_tarefa = ?
    """, (novo_status, nova_prioridade, id_tarefa))

    conn.commit()
    conn.close()

    print("Tarefa de membro atualizada com sucesso!")


def listar_tarefas_interativo():
    print("\n--- Filtrar Tarefas ---")
    filtro_status = input(
        "Filtrar por status (A fazer / Concluído) ou Enter para todos: ").capitalize()
    filtro_prioridade = input(
        "Filtrar por prioridade (Alta / Média / Baixa) ou Enter para todos: ").capitalize()

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM tarefas WHERE 1=1"
    params = []

    if filtro_status:
        sql += " AND status = ?"
        params.append(filtro_status)

    if filtro_prioridade:
        sql += " AND prioridade = ?"
        params.append(filtro_prioridade)

    cursor.execute(sql, params)
    tarefas = cursor.fetchall()
    conn.close()

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    print("\nTarefas:")
    for t in tarefas:
        print(f"[{t['id_tarefa']}] {t['titulo']} - {t['status']} - Prioridade: {t['prioridade']} - Responsável: {t['responsavel_nome']}")


def criar_tarefa_para_membro_flow():
    """Admin cria tarefa para outro membro"""
    print("\n--- Criar Tarefa para Membro ---")

    conn = get_db_connection()
    cursor = conn.cursor()

    # Listar membros
    cursor.execute("SELECT * FROM usuarios WHERE tipo = 'membro'")
    membros = cursor.fetchall()

    if not membros:
        print("Nenhum membro encontrado.")
        conn.close()
        return

    print("Membros:")
    for m in membros:
        print(f"[{m['id_usuario']}] {m['nome']} - {m['email']}")

    try:
        id_membro = int(input("Digite o ID do membro responsável: "))
    except ValueError:
        print("ID inválido! Digite um número.")
        return

    cursor.execute(
        "SELECT * FROM usuarios WHERE id_usuario = ? AND tipo = 'membro'", (id_membro,))
    membro = cursor.fetchone()

    if not membro:
        print("Membro não encontrado.")
        conn.close()
        return

    titulo = input("Título: ")
    descricao = input("Descrição: ")
    status = "A fazer"
    prioridade = input("Prioridade (Alta / Média / Baixa): ").capitalize()

    cursor.execute("""
        INSERT INTO tarefas (titulo, descricao, status, prioridade, responsavel_id, responsavel_nome)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, descricao, status, prioridade, membro["id_usuario"], membro["nome"]))

    conn.commit()
    conn.close()

    print("Tarefa criada para membro com sucesso!")


def listar_todas_tarefas_flow():
    """Admin vê TODAS as tarefas do sistema"""
    print("\n--- Lista Geral de Tarefas (Admin) ---")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tarefas
        ORDER BY status ASC, prioridade DESC, data_criacao DESC
    """)

    tarefas = cursor.fetchall()
    conn.close()

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nTarefas:")
    for t in tarefas:
        print(f"[{t['id_tarefa']}] {t['titulo']} | {t['status']} | Prioridade: {t['prioridade']} | Responsável: {t['responsavel_nome']} | Criada em: {t['data_criacao']}")


def ver_minhas_tarefas_flow(usuario_logado):
    """Membro vê suas tarefas com detalhes"""
    print("\n--- Minhas Tarefas (Detalhado) ---")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tarefas
        WHERE responsavel_id = ?
        ORDER BY status ASC, prioridade DESC, data_criacao DESC
    """, (usuario_logado["id_usuario"],))

    tarefas = cursor.fetchall()
    conn.close()

    if not tarefas:
        print("Você não possui tarefas atribuídas.")
        return

    print("\nSuas Tarefas:")
    for t in tarefas:
        print(f"\n==== Tarefa ID: {t['id_tarefa']} ====")
        print(f"Título      : {t['titulo']}")
        print(f"Status      : {t['status']}")
        print(f"Prioridade  : {t['prioridade']}")
        print(f"Descrição   :\n{t['descricao']}")
        print(f"Criada em   : {t['data_criacao']}")
        print("===================================")


def atualizar_responsavel_flow(usuario_logado):
    """Admin atualiza o responsavel da tarefa"""
    print("\n--- Atualizar Responsável da Tarefa ---")
    listar_tarefas_interativo()  # já mostra as tarefas e seus IDs

    try:
        id_tarefa = int(input("Digite o ID da tarefa que deseja atualizar: "))
    except ValueError:
        print("ID inválido! Digite um número.")
        return

    print("\n--- Usuários Cadastrados ---")
    listar_usuarios_simples()  # nova função que lista ID e Nome dos usuários

    try:
        novo_id_resp = int(input("Digite o ID do novo responsável: "))
    except ValueError:
        print("ID inválido! Digite um número.")
        return

    # Buscar nome do novo responsável no banco
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT nome FROM usuarios WHERE id_usuario = ?", (novo_id_resp,))
    row = cursor.fetchone()

    if not row:
        print("ID de usuário não encontrado. Operação cancelada.")
        conn.close()
        return

    novo_nome_resp = row[0]

    cursor.execute("""
        UPDATE tarefas
        SET responsavel_id = ?, responsavel_nome = ?
        WHERE id_tarefa = ?
    """, (novo_id_resp, novo_nome_resp, id_tarefa))

    conn.commit()
    conn.close()

    print(
        f"Responsável atualizado para {novo_nome_resp} (ID: {novo_id_resp}) com sucesso!")

    registrar_log_tarefa(
        id_tarefa,
        f"Responsável alterado - Novo responsável: {novo_nome_resp} (ID: {novo_id_resp}), Alterado por: {usuario_logado['nome']} (ID: {usuario_logado['id_usuario']})"
    )


def atualizar_descricao_flow(usuario_logado):
    """Admin atualiza a descrição de uma tarefa"""
    print("\n--- Atualizar Descrição da Tarefa ---")
    listar_tarefas_interativo()

    try:
        id_tarefa = int(input("Digite o ID da tarefa que deseja atualizar: "))
    except ValueError:
        print("ID inválido! Digite um número.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()

    # Buscar a descrição atual da tarefa
    cursor.execute(
        "SELECT descricao FROM tarefas WHERE id_tarefa = ?", (id_tarefa,))
    row = cursor.fetchone()

    if not row:
        print("Tarefa não encontrada. Operação cancelada.")
        conn.close()
        return

    descricao_atual = row[0]
    print(f"\nDescrição atual da tarefa:\n{descricao_atual}")

    nova_descricao = input("\nDigite a nova descrição: ")

    cursor.execute("""
        UPDATE tarefas
        SET descricao = ?
        WHERE id_tarefa = ?
    """, (nova_descricao, id_tarefa))

    conn.commit()
    conn.close()

    print("Descrição atualizada com sucesso!")

    registrar_log_tarefa(
        id_tarefa,
        f"Descrição alterada - Anterior: \"{descricao_atual}\" → Nova: \"{nova_descricao}\" - Alterado por: {usuario_logado['nome']} (ID: {usuario_logado['id_usuario']})"
    )
