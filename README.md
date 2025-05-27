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
