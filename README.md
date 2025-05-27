# Streaming Educacional 
# Uma plataforma digital voltada ao fornecimento de conteúdos educativos em formato audiovisual, com foco especial no público infantojuvenil. 
🔐 Autenticação e Segurança
O projeto implementa mecanismos de autenticação e segurança para garantir que apenas usuários autorizados acessem determinadas funcionalidades.

🔑 Mecanismos Utilizados
Autenticação: Verificação de usuário e senha através de formulários.

Hash de Senhas: Utilização de algoritmos de hash (como bcrypt) para proteger as senhas armazenadas no banco de dados.

Sessões Seguras: Gerenciamento de sessões com expiração para proteger o acesso contínuo.

Validação de Login: Campos obrigatórios, tratamento de erros e verificação de credenciais.

Criptografia: Proteção de dados sensíveis utilizando bibliotecas de criptografia.

📁 Organização do Código
app.py ou main.py: Ponto de entrada da aplicação, onde são configuradas as rotas e a autenticação.

models.py: Modelos de dados, incluindo o modelo de usuário.

templates/: Arquivos HTML com formulários de login e registro.

database/: Configuração e gerenciamento do banco de dados.

🔒 Fluxo de Autenticação
Cadastro: O usuário fornece e-mail e senha; a senha é criptografada e os dados são salvos no banco de dados.

Login: O usuário fornece credenciais; o sistema verifica a senha criptografada e, se correta, inicia uma sessão.

Acesso Protegido: Rotas específicas exigem autenticação para acesso, como páginas de perfil ou dashboard.

📦 Bibliotecas Utilizadas
bcrypt: Para hash e verificação de senhas.

sqlite3 ou SQLAlchemy: Para gerenciamento do banco de dados.

Flask ou FastAPI: Frameworks web para gerenciamento de rotas e sessões.

Jinja2: Para renderização de templates HTML de forma segura.
