from flask import Flask, flash, redirect, render_template, request, url_for, session
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

bcrypt = Bcrypt(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirma_senha = request.form['confirma_senha']
        perfil = request.form['perfil']

        if senha != confirma_senha:
            flash("As senhas não coincidem.", "error")
            return render_template("register.html")

        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
            usuario_existente = cursor.fetchone()

            if usuario_existente:
                flash("E-mail já cadastrado. Tente outro.", "error")
                return render_template("register.html")

            senha_criptografada = bcrypt.generate_password_hash(senha).decode('utf-8')
            cursor.execute("INSERT INTO usuarios (nome, email, senha, perfil) VALUES (?, ?, ?, ?)",
                           (nome, email, senha_criptografada, perfil))
            conn.commit()

        flash("Usuário cadastrado com sucesso!", "success")
        return render_template("register.html", sucesso=True)

    return render_template("register.html", sucesso=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
            usuario = cursor.fetchone()

            if usuario and bcrypt.check_password_hash(usuario[3], senha):
                session['user_id'] = usuario[0]
                session['user_nome'] = usuario[1]  # guarda o nome do usuário na sessão
                flash("Login realizado com sucesso!", "success")
                return redirect(url_for('dashboard'))
            else:
                flash("E-mail ou senha inválidos.", "error")

    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    if 'user_nome' not in session:
        flash("Você precisa estar logado para acessar o painel.", "error")
        return redirect(url_for('login'))

    nome = session['user_nome']
    return render_template("dashboard.html", nome=nome)

@app.route('/logout')
def logout():
    session.clear()
    flash("Você foi desconectado.", "success")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
