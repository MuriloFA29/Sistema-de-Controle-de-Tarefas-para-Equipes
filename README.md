# 📋 Sistema de Controle de Tarefas para Equipes (CLI)

> Um sistema baseado em terminal que simula a gestão de tarefas para equipes (estilo Trello) com banco de dados SQLite, controle de permissões (Admin/Membro) e sistema de logs.

---

## ✨ Funcionalidades

- [x] **Controle de Acesso:** Cadastro de usuários com perfis diferenciados (`Admin` e `Membro`).
- [x] **Gestão de Tarefas:** Criação, edição (status, prioridade, responsável) e deleção de tarefas.
- [x] **Filtros e Consultas:** Visualização por status, prioridade ou tarefas atribuídas a um membro específico.
- [x] **Sistema de Logs:** Registro em arquivo `.log` dedicado para rastrear o histórico de alterações de cada tarefa.
- [x] **Regra Inicial:** A primeira conta cadastrada no sistema assume automaticamente a função de `Admin`.

---

## 🛠️ Tecnologias & Conceitos Aplicados

* **Linguagem:** Python 3
* **Banco de Dados:** SQLite3 (`.db`) com inicialização via `schema.sql`
* **Arquitetura:** Programação Orientada a Objetos (POO) e arquitetura modularizada (MVC-like)
* **Auditoria:** Manipulação de arquivos para geração de logs individuais (`.log`)

---

## 📁 Estrutura do Projeto

* `main.py` — Ponto de entrada da aplicação.
* `controllers/` — Lógica de controle de usuários, tarefas e sistema.
* `models/` — Regras de negócio e classes (`Usuario` e `Tarefa`).
* `data/` — Banco SQLite e script de criação (`schema.sql`).
* `utils/` — Utilitários e manipuladores do sistema de log.
* `logs/` — Diretório com arquivos `.log` históricos.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.8 ou superior instalado.
* *(Não é necessário instalar ou configurar banco de dados externamente — o SQLite é nativo do Python e cria o arquivo `.db` automaticamente na primeira execução).*

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/MuriloFA29/Sistema-de-Controle-de-Tarefas-para-Equipes.git](https://github.com/MuriloFA29/Sistema-de-Controle-de-Tarefas-para-Equipes.git)

1. **Acesse a pasta do projeto:**
   ```bash
   cd Sistema-de-Controle-de-Tarefas-para-Equipes

1. **Execute a aplicação:**
   ```bash
   python main.py

---

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
