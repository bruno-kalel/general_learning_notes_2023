# pip install flask, flask_sqlalchemy psycopg2
# pip não é declarado explicitamente, mas precisa ser instalado
from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from os import listdir, remove, path
from time import time

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


class Jogos(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(50), nullable=False)
  categoria = db.Column(db.String(40), nullable=False)
  console = db.Column(db.String(20), nullable=False)


class Usuários(db.Model):
  nome = db.Column(db.String(20), nullable=False)
  nickname = db.Column(db.String(8), primary_key=True)
  senha = db.Column(db.String(100), nullable=False)


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
  
  return render_template('novo.html',
                         title='Novo jogo')


@app.route('/editar/<int:identificador>')
def editar(identificador):
  if session.get('usuário_autenticado') is None:
    return redirect(url_for('login',
                            next=url_for('editar')))
  
  jogo = Jogos.query.filter_by(id=identificador).first()
  
  capa_jogo = recuperar_imagem(identificador)
  
  return render_template('editar.html',
                         title='Editar jogo',
                         jogo=jogo,
                         capa_jogo=capa_jogo)


@app.route('/criar', methods=['POST', ])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  
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
  jogo = Jogos.query.filter_by(id=request.form['id']).first()
  jogo.nome = request.form['nome']
  jogo.categoria = request.form['categoria']
  jogo.console = request.form['console']
  
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
  return render_template('login.html',
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
  # boolean que identificá a presença do usuário no banco de dados
  usuário = Usuários.query.filter_by(nickname=request.form['usuário']).first()
  
  if usuário:
    
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
