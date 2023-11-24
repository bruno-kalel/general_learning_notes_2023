from jogoteca import app, db
from models import Jogos, Usuários

from flask import render_template, request, redirect, session, flash, url_for


@app.route('/')
def index():
  lista = Jogos.query.order_by(Jogos.id)
  return render_template('lista.html', title='Jogos', jogos=lista)


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
  
  # boolean para verificar se o jogo que se deseja criar já existe no banco de dados
  if Jogos.query.filter_by(nome=nome).first():
    flash('Jogo já existente!')
    return redirect(url_for('index'))
  
  db.session.add(Jogos(nome=nome, categoria=categoria, console=console))
  db.session.commit()
  
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
