class Conta:
  def __init__(self, numero_conta, titular, saldo = 0.00, limite = 1000.00):
    self.__numero = numero_conta
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite

  
  def extrato(self):
    print(f'{"Número da conta:":<20}{self.__numero:>20}')
    print(f'{"Titular:":<20}{self.__titular:>20}')
    print(f'{"Saldo:":<28}{self.__saldo:>12.2f}')
    print(f'{"Limite:":<26}{self.__limite:>14.2f}\n')
    print('=+'*20,'\n')


  def depositar(self, valor):
    self.__saldo += valor


  def __pode_sacar(self, valor_a_sacar):
    valor_disponivel = self.__limite + self.__saldo
    return valor_disponivel >= valor_a_sacar
    
    
  def __ajusta_valor_limite(self):
    if (self.saldo < 0):
        self.__limite += self.__saldo
        self.__saldo = 0

  
  def sacar(self, valor):
    if(self.__pode_sacar(valor)):
      self.__saldo -= valor
      self.__ajusta_valor_limite()
      print('Valor sacado.')
    else:
      print('Saldo insuficiente para saques.')

  
  def transferir(self, valor, destino):
    self.sacar(valor)
    destino.depositar(valor)
    print(f'Transferido {valor:.2f}.')

  @property
  def saldo(self):
    return self.__saldo
    

  @property
  def titular(self):
    return self.__titular


  @property
  def limite(self):
    return self.__limite


  @limite.setter
  def limite(self, novolimite):
    self.__limite = novolimite


  @staticmethod
  def codigo_banco():
    return '001'
