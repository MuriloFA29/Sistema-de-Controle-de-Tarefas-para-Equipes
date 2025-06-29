-- Tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('admin', 'membro')) NOT NULL
);

-- Tabela de tarefas
CREATE TABLE IF NOT EXISTS tarefas (
    id_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    status TEXT CHECK(status IN ('A fazer', 'Concluído')) DEFAULT 'A fazer',
    prioridade TEXT CHECK(prioridade IN ('Alta', 'Média', 'Baixa')) DEFAULT 'Média',
    responsavel_id INTEGER,
    responsavel_nome TEXT,
    data_criacao TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (responsavel_id) REFERENCES usuarios(id_usuario)
);
