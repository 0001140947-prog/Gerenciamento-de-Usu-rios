📌 Projeto Flask – Gerenciamento de Usuários

Este projeto é uma aplicação web desenvolvida com Flask e Flask-SQLAlchemy, cujo objetivo é realizar o cadastro, listagem e exclusão de usuários, utilizando banco de dados SQLite.

📁 Estrutura do Projeto
Atividade flask/
│
├── app.py
├── usuarios.db
├── README.md
│
├── templates/
│   ├── index.html
│   ├── cadastro.html
│   ├── usuarios.html
│   └── excluir_usuario.html
│
└── static/
    └── style.css

🧪 Tecnologias Utilizadas

Python 3.12+

Flask

Flask-SQLAlchemy

SQLite

HTML5 + CSS3

⚙️ Criação do Ambiente Virtual (opcional, recomendado)
Windows
python -m venv venv
venv\Scripts\activate

Linux / macOS
python3 -m venv venv
source venv/bin/activate

📦 Instalação das Dependências

Com o ambiente virtual ativado (ou sem, se não estiver usando):

pip install flask flask-sqlalchemy

▶️ Como Executar a Aplicação

No diretório raiz do projeto:

python app.py


Após executar, o Flask iniciará o servidor em modo desenvolvimento.

Acesse no navegador:

http://127.0.0.1:5000


O banco de dados usuarios.db será criado automaticamente na primeira execução.

🌐 Rotas Implementadas
/

Página inicial

Exibe a página principal da aplicação.

Contém links para cadastro e listagem de usuários.

/cadastro

Cadastro de usuário

Método: GET e POST

Permite cadastrar um novo usuário informando nome e e-mail.

Valida campos obrigatórios e impede e-mails duplicados.

/usuarios

Listagem de usuários

Método: GET

Exibe todos os usuários cadastrados no banco de dados.

Contém links para excluir usuários ou voltar à página inicial.

/excluir

Exclusão de usuário

Método: GET e POST

Exibe uma lista de usuários cadastrados.

Permite excluir um usuário selecionado pelo ID.

Após a exclusão, redireciona para a listagem de usuários.

🗄️ Banco de Dados

Banco: SQLite

Arquivo: usuarios.db

Tabela principal: Usuario

id (chave primária)

nome

email (único)

✅ Observações Finais

O projeto segue boas práticas básicas de organização em Flask.

Todas as funcionalidades exigidas pela atividade foram implementadas.

A aplicação é executada via navegador, sem necessidade de uso de terminal após inicialização.

Código comentado e estrutura simples para fins acadêmicos.
