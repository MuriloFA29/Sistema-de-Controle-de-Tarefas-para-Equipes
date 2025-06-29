from datetime import datetime
import os


def input_obrigatorio(mensagem):
    """Pede um input obrigatório, sem aceitar vazio"""
    while True:
        valor = input(mensagem).strip()
        if valor == "":
            print("Este campo não pode ser vazio.")
        else:
            return valor


def confirmar_acao(mensagem="Tem certeza? (s/n): "):
    resp = input(mensagem).strip().lower()
    return resp == 's'


def registrar_log_tarefa(id_tarefa, mensagem):
    """Grava log em arquivo separado por tarefa"""
    # Garante que a pasta logs/ existe
    os.makedirs("logs", exist_ok=True)

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    caminho_log = f"logs/tarefa_{id_tarefa}.log"

    with open(caminho_log, "a", encoding="utf-8") as f:
        f.write(f"[{data_hora}] {mensagem}\n")
