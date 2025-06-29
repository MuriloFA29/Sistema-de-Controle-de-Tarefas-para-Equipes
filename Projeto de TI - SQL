## Plano para Persistência com SQLite:

### 1. Modelagem básica das tabelas:

* **usuarios**

  * id (INTEGER PRIMARY KEY AUTOINCREMENT)
  * nome (TEXT)
  * tipo (TEXT) — "membro" ou "adm"
  * login (TEXT) — único
  * senha (TEXT) — para simplificar, pode ser texto puro (ou hashed se quiser algo extra)

* **boards**

  * id (INTEGER PRIMARY KEY AUTOINCREMENT)
  * nome (TEXT)

* **colunas**

  * id (INTEGER PRIMARY KEY AUTOINCREMENT)
  * nome (TEXT) — ex: "A Fazer", "Em Progresso"
  * board\_id (INTEGER, FOREIGN KEY para boards.id)

* **tarefas**

  * id (INTEGER PRIMARY KEY AUTOINCREMENT)
  * titulo (TEXT)
  * descricao (TEXT)
  * status (TEXT) — poderia estar vinculado a colunas, mas pode ser texto também
  * responsavel\_id (INTEGER, FOREIGN KEY para usuarios.id)
  * coluna\_id (INTEGER, FOREIGN KEY para colunas.id)

---

### 2. Organização no código:

* Criar um módulo `db.py` para lidar com:

  * Criação das tabelas no banco
  * Funções CRUD (Create, Read, Update, Delete)
  * Queries para buscar tarefas por usuário, status, etc.

* Classes modelo podem ser simples, ou podem receber dados do banco e converter para objetos.
