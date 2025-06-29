import datetime


class Tarefa:
    def __init__(self, id_tarefa, titulo, descricao, status="A fazer", prioridade="Média", responsavel_id=None, responsavel_nome=""):
        self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.status = status  # 'A fazer' ou 'Concluído'
        self.prioridade = prioridade  # 'Alta', 'Média', 'Baixa'
        self.responsavel_id = responsavel_id
        self.responsavel_nome = responsavel_nome
        self.historico = []  # lista de (data, alteração)

    def __repr__(self):
        return f"<Tarefa {self.id_tarefa}: {self.titulo} [{self.status}]>"

    def atualizar_status(self, novo_status):
        if novo_status in ("A fazer", "Concluído"):
            if novo_status != self.status:
                self.status = novo_status
                self._adicionar_historico(
                    f"Status alterado para '{novo_status}'")
            else:
                print("Status já está definido como:", novo_status)
        else:
            raise ValueError("Status inválido. Use 'A fazer' ou 'Concluído'.")

    def alterar_prioridade(self, nova_prioridade):
        if nova_prioridade in ("Alta", "Média", "Baixa"):
            if nova_prioridade != self.prioridade:
                self.prioridade = nova_prioridade
                self._adicionar_historico(
                    f"Prioridade alterada para '{nova_prioridade}'")
            else:
                print("Prioridade já está definida como:", nova_prioridade)
        else:
            raise ValueError(
                "Prioridade inválida. Use 'Alta', 'Média' ou 'Baixa'.")

    def atribuir_responsavel(self, id_usuario, nome_usuario):
        if id_usuario != self.responsavel_id:
            self.responsavel_id = id_usuario
            self.responsavel_nome = nome_usuario
            self._adicionar_historico(
                f"Responsável atribuído: {nome_usuario} (ID {id_usuario})")
        else:
            print(f"Responsável já é {nome_usuario} (ID {id_usuario})")

    def atualizar_descricao(self, nova_descricao):
        if nova_descricao != self.descricao:
            antiga = self.descricao
            self.descricao = nova_descricao
            self._adicionar_historico(
                f"Descrição alterada de '{antiga}' para '{nova_descricao}'")
        else:
            print("Descrição não foi alterada.")

    def _adicionar_historico(self, descricao):
        data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.historico.append((data, descricao))

    def exibir_historico(self):
        print(f"Histórico da tarefa {self.id_tarefa} - {self.titulo}:")
        for data, desc in self.historico:
            print(f"[{data}] {desc}")
