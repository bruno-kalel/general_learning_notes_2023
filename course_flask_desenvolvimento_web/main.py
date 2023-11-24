from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy


class Jogo:
  def __init__(self, nome, categoria, console):
    self.nome = nome
    self.categoria = categoria
    self.console = console


jogo_1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo_2 = Jogo('God of War', 'Hack and slash', 'PS2')
jogo_3 = Jogo('Mortal Kombat', 'Fighting', 'Super Nintendo')

jogos = [jogo_1, jogo_2, jogo_3]


class Usuário:
  def __init__(self, nome, nickname, senha):
    self.nome = nome
    self.nickname = nickname
    self.senha = senha


usuário_1 = Usuário('bruno', 'bruno123', 'bruno')
usuário_2 = Usuário('isaac', 'isaac456', 'isaac')
usuário_3 = Usuário('girotto', 'girotto789', 'girotto')

usuários = {usuário_1.nickname: usuário_1,
            usuário_2.nickname: usuário_2,
            usuário_3.nickname: usuário_3}

app = Flask(__name__)
app.secret_key = ''

CONFIG_DBMS = ''
CONFIG_USER = ''
CONFIG_PASSWORD = ''
CONFIG_SERVER = ''
CONFIG_DATABASE = ''

app.config['SQLALCHEMY_DATABASE_URI'] = \
  f'{CONFIG_DBMS}://{CONFIG_USER}:{CONFIG_PASSWORD}@{CONFIG_SERVER}/{CONFIG_DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Jogos(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(50), nullable=False)
  categoria = db.Column(db.String(40), nullable=False)
  console = db.Column(db.String(20), nullable=False)
  
  def __repr__(self):
    return '<Name %r' % self.name


class Usuários(db.Model):
  nome = db.Column(db.String(20), nullable=False)
  nickname = db.Column(db.String(8), primary_key=True)
  senha = db.Column(db.String(100), nullable=False)
  
  def __repr__(self):
    return '<Name %r' % self.name


@app.route('/')
def index():
  return render_template('lista.html', title='Jogos', jogos=jogos)


@app.route('/novo')
def novo():
  if session.get('usuário_autenticado') is None:
    return redirect(url_for('login', next=url_for('novo')))
  
  return render_template('novo.html', title='Novo jogo')


@app.route('/criar', methods=['POST', ])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  
  jogo = Jogo(nome, categoria, console)
  jogos.append(jogo)
  
  return redirect(url_for('index'))


@app.route('/login')
def login():
  return render_template('login.html', next=request.args.get('next', url_for('index')))


@app.route('/logout')
def logout():
  # login = session guarda o nome do usuário
  # logout = session não guarda o nome do usuário
  session['usuário_autenticado'] = None
  flash('Logout efetuado com sucesso!')
  return redirect(url_for('index'))


@app.route('/autenticar', methods=['POST', ])
def autenticar():
  if request.form['usuário'] in usuários:
    usuário = usuários[request.form['usuário']]
    
    if request.form['senha'] == usuário.senha:
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
