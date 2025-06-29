class Usuario:
    def __init__(self, id_usuario, nome, email, senha, tipo="membro"):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo  # 'admin' ou 'membro'

    def __repr__(self):
        return f"<Usuario {self.id_usuario}: {self.nome} ({self.tipo})>"

    def alterar_nome(self, novo_nome):
        if novo_nome and novo_nome != self.nome:
            self.nome = novo_nome
        else:
            print("Nome inválido ou igual ao atual.")

    def alterar_email(self, novo_email):
        if novo_email and novo_email != self.email:
            self.email = novo_email
        else:
            print("Email inválido ou igual ao atual.")

    def alterar_senha(self, nova_senha):
        if nova_senha and nova_senha != self.senha:
            self.senha = nova_senha
        else:
            print("Senha inválida ou igual à atual.")

    def alterar_tipo(self, novo_tipo):
        if novo_tipo in ("admin", "membro"):
            if novo_tipo != self.tipo:
                self.tipo = novo_tipo
            else:
                print(f"Tipo já é '{novo_tipo}'.")
        else:
            raise ValueError("Tipo inválido. Use 'admin' ou 'membro'.")
