from time import sleep

restaurantes = [{'nome': 'r1', 'categoria': 'c1', 'ativo': False},
                {'nome': 'r2', 'categoria': 'c2', 'ativo': False},
                {'nome': 'r3', 'categoria': 'c3', 'ativo': True}]


def mostrar_subtítulo(evento: str):
  asteriscos = '*' * (len(evento))
  print(asteriscos)
  print(evento)
  print(asteriscos)


def voltar_ao_menu_principal(evento: str):
  print(f'{evento}, voltando ao menu principal...')
  sleep(1)
  main()


def exibir_nome():
  print('')


def exibir_opções():
  print('1. cadastrar')
  print('2. listar')
  print('3. ativar')
  print('4. sair')


def cadastrar():
  mostrar_subtítulo('cadastrando...')
  
  restaurante = {'nome': input('nome: '),
                 'categoria': input('categoria: '),
                 'ativo': False}
  restaurantes.append(restaurante)
  
  voltar_ao_menu_principal('cadastrado com sucesso')


def listar():
  mostrar_subtítulo('listando...')
  
  for restaurante in restaurantes:
    print(restaurante['nome'].ljust(8),
          '|', restaurante['categoria'].ljust(8),
          '|', 'ativo' if restaurante['ativo'] else 'inativo')
  
  voltar_ao_menu_principal('listado com sucesso')


def alternar():
  mostrar_subtítulo('alternando...')
  encontrado = False
  nome = input('nome: ')
  
  for restaurante in restaurantes:
    if nome == restaurante['nome']:
      restaurante['ativo'] = not restaurante['ativo']
      encontrado = True
      voltar_ao_menu_principal('alternado com sucesso')
  
  if not encontrado:
    voltar_ao_menu_principal('restaurante não encontrado')


def sair():
  mostrar_subtítulo('saindo...')


def escolher_opção():
  try:
    opção = int(input('escolha uma opção: '))
    
    match opção:
      case 1:
        cadastrar()
      case 2:
        listar()
      case 3:
        alternar()
      case 4:
        sair()
      case _:
        voltar_ao_menu_principal('opção não identificada')
  
  except ValueError:
    voltar_ao_menu_principal('opção não identificada')


def main():
  exibir_nome()
  exibir_opções()
  escolher_opção()


if __name__ == '__main__':
  main()
