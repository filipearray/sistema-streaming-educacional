#  Sistema de Streaming Educacional  

**Sistema Web educacional** com arquitetura separada de Frontend e Backend (API), com foco em segurança da informação, autenticação de usuários e acesso a conteúdos educacionais.  

---

##  Arquitetura do Projeto  
O sistema é dividido em duas camadas independentes:  

| **Camada**       | **Descrição**                                                                 |
|------------------|------------------------------------------------------------------------------|
| **Frontend**     | Interface com o usuário (páginas HTML, formulários, layout, exibição).       |
| **Backend (API)**| Lógica de negócio, autenticação, segurança e conexão com o banco de dados.   |

A comunicação entre as camadas ocorre via **requisições HTTP (POST/GET)** entre os formulários do frontend e os endpoints do backend.  

---

##  Mecanismos de Segurança Implementados  
- **Autenticação de Usuário** com login e senha.  
- **Hash de Senhas** com `bcrypt` para proteger credenciais.  
- **Validação de Entrada** para evitar dados inválidos ou vazios.  
- **Proteção de Rotas**: usuários não autenticados são redirecionados.  
- **Gerenciamento de Sessão** com expiração.  

---

##  Tecnologias Utilizadas  
| **Camada**       | **Tecnologias**                              |
|------------------|---------------------------------------------|
| **Backend**      | Python, Flask, bcrypt, SQLite               |
| **Frontend**     | HTML, CSS, Jinja2 Templates                 |

---

##  Estrutura de Diretórios   
```plaintext
  sistema-streaming/
├─── backend/               # Tudo do backend
│    ├── app.py             # Ponto de entrada principal
│    ├── models.py          # Definição dos modelos
│    ├── database.db        # Banco de dados SQLite
│    ├── requirements.txt   # Dependências
│    └── __pycache__/       # Cache Python (gerado automaticamente)
│
├─── frontend/              # Interface do usuário
│    └── templates/         # Páginas HTML
│
├── build/                  # Arquivos de build (gerados)
│   └── main               # Executável temporário
│
├── dist/                   # Output final (gerado)
│
├── iniciar_app.bat         # Script de inicialização
└── main.spec               # Configuração do PyInstaller
##  Como Executar

### Modo de Desenvolvimento (via Python)

1. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Instale as dependências:
   ```bash
   pip install flask flask-bcrypt
   ```

3. Crie o banco de dados (apenas uma vez):
   ```python
   import sqlite3
   conn = sqlite3.connect('database.db')
   cursor = conn.cursor()
   cursor.execute("""
   CREATE TABLE usuarios (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome TEXT NOT NULL,
       email TEXT NOT NULL UNIQUE,
       senha TEXT NOT NULL
   );
   """)
   conn.commit()
   conn.close()
   ```

4. Execute a aplicação:
   ```bash
   python main.py
   ```

5. Acesse no navegador:
   ```
   http://127.0.0.1:5000/register
   ```

---

### Modo Executável (.exe)

1. Compile com PyInstaller:
   ```bash
   pyinstaller --noconfirm --onefile --add-data "templates;templates" main.py
   ```

2. O executável estará disponível na pasta `dist/`:
   ```
   dist/main.exe
   ```

3. Para facilitar o uso, crie um `iniciar_app.bat`:
   ```bat
   @echo off
   cd /d %~dp0dist
   start main.exe
   ```

4. Execute `iniciar_app.bat` para iniciar a aplicação.

---

##  Observações

- O projeto roda localmente em `127.0.0.1:5000` ou `127.0.0.1:8000`, conforme configurado no `main.py`.
- Ideal para testes e aprendizado. **Não recomendado para produção sem ajustes de segurança.**
- O campo “perfil” foi removido na versão final conforme solicitado.

---

## Licença

Este projeto é de uso livre para fins acadêmicos e educacionais.
