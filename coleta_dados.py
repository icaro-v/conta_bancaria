from time import sleep

def imprime_ola():
  msg = 'Bem vindo usuário, vamos criar sua conta bancária.\n'
  for letra in msg:
    sleep(0.08)
    print(letra,end='',flush = True)
  
  msg = """\nDe início, precisamos definir alguns pontos:\n
   - seu nome
   - seu saldo inicial, caso queira efetuar um depósito
   - seu limite inicial\n\n"""
  
  for letra in msg:
    sleep(0.08)
    print(letra,end='',flush = True)


def processa_nome():
  print('Vamos começar nomeando o titular da conta.')
  while True:
    nome = input('Digite seu nome: ').strip()
    if(nome != ''):
      nome = nome.split()
      for i, en in enumerate(nome):
        nome[i] = en.capitalize()
      nome = ' '.join(nome)
      break
    print('Por favor preencha corretamente.', end = ' ')

  return(nome)


def processa_saldo(nome):
  print(f'\nTudo bem {nome.split()[0]}, agora informe quanto você deseja depositar em sua conta.Caso não quiser depositar nada, pressione enter.\n')
  while True:
    saldo = input('Insira o valor: R$').strip()
    
    if (saldo == ''):
      saldo = 0
      break
    elif(saldo.isnumeric()):
      saldo = float(saldo)
      break
    else:
      print('Digite o saldo corretamente.', end=' ')
  print(f'\nOk, seu saldo inicial será de R${saldo:.2f}.')

  return saldo

def processa_limite():
  limite = 1000.00
  print(f'\nO limite padrão do banco é de R$1000.00, se você quiser pode aumentá-lo.')
  while True:
    resp = input('Deseja aumentar o limite? [S/N] ').upper().strip()

    if(resp in 'SN' and resp != ''):
      break
    print('Escolha corretamente.',end=' ')

  
  if (resp == 'S'):
    print()
    while True:
      novo = input('Insira o valor do seu novo limite: R$').strip()

      if(novo.isnumeric()):
        if(float(novo)>limite):
          limite = float(novo)
          break
      print('\nDigite o novo limite corretamente (deve ser maior que o padrão).', end=' ')
  print(f'\nCerto, seu limite será de R${limite:.2f}.')
    
  return limite



imprime_ola()

nome = processa_nome()
saldo = processa_saldo(nome)
limite = processa_limite()
