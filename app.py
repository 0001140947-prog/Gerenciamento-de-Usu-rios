from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Model
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


# Rotas
@app.route("/")
def landing_page():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro_usuario():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")

        if not nome or not email:
            return render_template(
                "cadastro.html",
                erro="Todos os campos são obrigatórios"
            )

        # Verificar email duplicado
        existente = Usuario.query.filter_by(email=email).first()
        if existente:
            return render_template(
                "cadastro.html",
                erro="E-mail já cadastrado"
            )

        usuario = Usuario(nome=nome, email=email)
        db.session.add(usuario)
        db.session.commit()

        return redirect(url_for("listar_usuarios"))

    return render_template("cadastro.html")


@app.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template("usuarios.html", usuarios=usuarios)


@app.route("/excluir", methods=["GET", "POST"])
def excluir_usuario():
    if request.method == "POST":
        usuario_id = request.form["usuario_id"]
        usuario = Usuario.query.get(usuario_id)

        if usuario:
            db.session.delete(usuario)
            db.session.commit()

        return redirect(url_for("listar_usuarios"))

    usuarios = Usuario.query.all()
    return render_template("excluir_usuario.html", usuarios=usuarios)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria as tabelas, se não existirem
    app.run(debug=True)
