def abrir(nome, saldo,limite):
  import conta
  from time import sleep

  numero_conta = 7
  
  conta_aberta = conta.Conta(numero_conta, nome, saldo, limite)

  pontos = "....."
  print()
  
  for e in pontos:
    sleep(0.1)
    print(e,end=' ',flush = True)
  sleep(0.2)
  
  msg = "\n\nConta criada com sucesso =)\n"
    
  for e in msg:
    sleep(0.1)
    print(e,end='',flush = True)
  sleep(0.2)
  
  sleep(0.2)
  print('\n' + '=+'*20, '\n')
  
  conta.Conta.extrato(conta_aberta)
  