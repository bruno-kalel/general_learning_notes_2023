from jogoteca import db


class Jogos(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(50), nullable=False)
  categoria = db.Column(db.String(40), nullable=False)
  console = db.Column(db.String(20), nullable=False)
  
  # para mostrar uma versão em string quando ocorre o acesso à classe em modo interativo
  # similar ao __str__(self) para usuários finais
  def __repr__(self):
    return '<Name %r' % self.name


class Usuários(db.Model):
  nome = db.Column(db.String(20), nullable=False)
  nickname = db.Column(db.String(8), primary_key=True)
  senha = db.Column(db.String(100), nullable=False)
  
  def __repr__(self):
    return '<Name %r' % self.name
