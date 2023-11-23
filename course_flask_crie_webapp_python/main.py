from flask import Flask, render_template, request, redirect


class Jogo:
  def __init__(self, nome, categoria, console):
    self.nome = nome
    self.categoria = categoria
    self.console = console


jogo_1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo_2 = Jogo('God of War', 'Hack and slash', 'PS2')
jogo_3 = Jogo('Mortal Kombat', 'Fighting', 'Super Nintendo')

jogos = [jogo_1, jogo_2, jogo_3]

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('lista.html', título='Jogos', jogos=jogos)


@app.route('/novo')
def novo():
  return render_template('novo.html', título='Novo jogo')


@app.route('/criar', methods=['POST', ])
def criar():
  nome = request.form["nome"]
  categoria = request.form["categoria"]
  console = request.form["console"]
  
  jogo = Jogo(nome, categoria, console)
  jogos.append(jogo)
  
  return redirect('/')


if __name__ == '__main__':
  app.run(debug=True)
