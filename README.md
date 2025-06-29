# Sistema de Controle de Tarefas para Equipes

Um sistema simples, baseado em terminal, que simula a gestão de tarefas entre membros de uma equipe — inspirado em ferramentas como Trello. Desenvolvido em Python com foco em lógica, organização e persistência de dados.


## 🛠️ Tecnologias Usadas
- Python 3
- SQLite3
- Estrutura modular (POO)
- Armazenamento em arquivos `.db` e `.log`

## ⚙ Funcionalidades
- Cadastro de usuários com tipo (admin ou membro).
- Criação de tarefas com título, descrição, prioridade, status e responsável.
- Atualização de tarefas (status, descrição, prioridade e responsável).
- Filtros por status ou prioridade.
- Visualização detalhada das tarefas atribuídas.
- Logs de alterações gravados em arquivos .log por tarefa.

## 💭 Estrutura do Projeto
- main.py — Ponto de entrada da aplicação.
- controllers/ — Lógica de controle (usuário, tarefa, sistema).
- models/ — Classes Usuario e Tarefa com métodos próprios.
- data/ — Banco SQLite e schema de inicialização (schema.sql).
- utils/ — Funções auxiliares e sistema de log.
- logs/ — Arquivos .log individuais por tarefa (histórico).

## 🔎 Conceitos Aplicados
- Programação orientada a objetos (POO).
- Conexão e manipulação de banco de dados com SQLite.
- Modularização com pacotes e arquivos organizados.
- Entrada e validação de dados pelo terminal.
- Gravação de logs em arquivos para rastrear alterações.
- Interface baseada em menus com fluxos claros e fáceis.

## ✨ Extras
- A primeira conta criada é automaticamente do tipo admin.
- Os arquivos .log podem ser abertos em qualquer editor de texto para acompanhar o histórico de cada tarefa.
- Pode ser evoluído para interface gráfica (Tkinter) ou web (Flask) futuramente.


## ▶️ Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/MuriloFA29/Sistema-de-Controle-de-Tarefas-para-Equipes.git
   cd Sistema-de-Controle-de-Tarefas-para-Equipes

> **Pré-requisitos**: Python 3 instalado. Não é necessário configurar banco manualmente — o sistema cria o SQLite automaticamente ao iniciar.

## 📷 Diagrama UML

![UML](Projeto%20de%20TI/Diagrama%20de%20Classes%20-%20Sistema%20de%20Controle%20de%20Tarefas.drawio.png)
