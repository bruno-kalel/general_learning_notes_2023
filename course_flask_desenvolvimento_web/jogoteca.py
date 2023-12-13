# pip install flask flask_sqlalchemy flask-wtf flask-bcrypt psycopg2
# pip não é declarado explicitamente, mas precisa ser instalado
from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from os import listdir, remove, path
from time import time
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField, PasswordField, validators

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)


class Jogos(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(50), nullable=False)
  categoria = db.Column(db.String(40), nullable=False)
  console = db.Column(db.String(20), nullable=False)


class Usuários(db.Model):
  nome = db.Column(db.String(20), nullable=False)
  nickname = db.Column(db.String(8), primary_key=True)
  senha = db.Column(db.String(100), nullable=False)


class FormJogo(FlaskForm):
  nome = StringField('Nome',
                     [validators.DataRequired(), validators.Length(min=1, max=50)])
  categoria = StringField('Categoria',
                          [validators.DataRequired(), validators.Length(min=1, max=40)])
  console = StringField('Console',
                        [validators.DataRequired(), validators.Length(min=1, max=20)])
  submit = SubmitField('Salvar')


class FormLogin(FlaskForm):
  nickname = StringField('Nickname',
                         [validators.DataRequired(),
                          validators.Length(min=1, max=8)])
  senha = PasswordField('Senha', [validators.DataRequired(),
                                  validators.Length(min=1, max=100)])
  submit = SubmitField('Login')
  

def recuperar_imagem(identificador):
  for nome_arquivo in listdir(app.config['UPLOAD_PATH']):
    if f'artwork{identificador}' in nome_arquivo:
      return nome_arquivo
  return 'default.png'


def deletar_imagem(identificador):
  arquivo = recuperar_imagem(identificador)
  if arquivo != 'default.png':
    remove(path.join(app.config['UPLOAD_PATH'], arquivo))


@app.route('/')
def index():
  lista = Jogos.query.order_by(Jogos.id)
  return render_template('lista.html',
                         title='Jogos',
                         jogos=lista)


@app.route('/novo')
def novo():
  if session.get('usuário_autenticado') is None:
    return redirect(url_for('login',
                            next=url_for('novo')))
  
  form = FormJogo()
  return render_template('novo.html',
                         title='Novo jogo',
                         form=form)


@app.route('/editar/<int:identificador>')
def editar(identificador):
  if session.get('usuário_autenticado') is None:
    return redirect(url_for('login',
                            next=url_for('editar')))
  
  jogo = Jogos.query.filter_by(id=identificador).first()
  
  form = FormJogo()
  form.nome.data = jogo.nome
  form.categoria.data = jogo.categoria
  form.console.data = jogo.console
  
  capa_jogo = recuperar_imagem(identificador)
  
  return render_template('editar.html',
                         title='Editar jogo',
                         id=identificador,
                         capa_jogo=capa_jogo,
                         form=form)


@app.route('/criar', methods=['POST', ])
def criar():
  form = FormJogo(request.form)
  
  if not form.validate_on_submit():
    flash('Erro no formulário!')
    return redirect(url_for('novo'))
  
  nome = form.nome.data
  categoria = form.categoria.data
  console = form.console.data
  
  # boolean para verificar se o jogo que se deseja criar já existe no banco de dados
  if Jogos.query.filter_by(nome=nome).first():
    flash('Jogo já existente!')
    return redirect(url_for('index'))
  
  novo_jogo = Jogos(nome=nome,
                    categoria=categoria,
                    console=console)
  db.session.add(novo_jogo)
  db.session.commit()
  
  arquivo = request.files['arquivo']
  upload_path = app.config['UPLOAD_PATH']
  arquivo.save(f'{upload_path}/artwork{novo_jogo.id}-{time()}.jpg')
  
  return redirect(url_for('index'))


@app.route('/atualizar', methods=['POST', ])
def atualizar():
  form = FormJogo(request.form)
  
  if form.validate_on_submit():
    jogo = Jogos.query.filter_by(id=request.form['id']).first()
    jogo.nome = form.nome.data
    jogo.categoria = form.categoria.data
    jogo.console = form.console.data
    
    db.session.add(jogo)
    db.session.commit()
    
    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    deletar_imagem(jogo.id)
    arquivo.save(f'{upload_path}/artwork{jogo.id}-{time()}.jpg')
  
  return redirect(url_for('index'))


@app.route('/deletar/<int:identificador>')
def deletar(identificador):
  if session.get('usuário_autenticado') is None:
    return redirect(url_for('login'))
  
  Jogos.query.filter_by(id=identificador).delete()
  db.session.commit()
  flash('Jogo deletado com sucesso!')
  
  return redirect(url_for('index'))


@app.route('/login')
def login():
  form = FormLogin()
  return render_template('login.html',
                         form=form,
                         next=request.args.get('next', url_for('index')))


@app.route('/logout')
def logout():
  # login = session guarda o nome do usuário
  # logout = session não guarda o nome do usuário
  session['usuário_autenticado'] = None
  flash('Logout efetuado com sucesso!')
  return redirect(url_for('index'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
  return send_from_directory('uploads', nome_arquivo)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
  form = FormLogin(request.form)
  
  # boolean que identificá a presença do usuário no banco de dados
  usuário = Usuários.query.filter_by(nickname=form.nickname.data).first()
  
  if usuário:
    
    if form.senha.data == usuário.senha:
      session['usuário_autenticado'] = usuário.nickname
      flash('Usuário ' + usuário.nickname + ' autenticado com sucesso!')
      next_page = request.form['next']
      return redirect(next_page)
    
    flash('Usuário não autenticado! Senha incorreta.')
    return redirect(url_for('login'))
  
  flash('Usuário não autenticado! Usuário não existe.')
  return redirect(url_for('login'))


if __name__ == '__main__':
  app.run(debug=True)
