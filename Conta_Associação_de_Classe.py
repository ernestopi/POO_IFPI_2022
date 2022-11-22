class Banco:
  def __init__(self, nome):
    self.__nome = nome
    self.__contas = []

  @property
  def nome(self):
    return self.__nome
    print(f'Nome do Banco ==> {self.__nome}')
  
  @property
  def contas(self):
    print('Contas a exibir...')
    return self.__contas

  def adicionar_Conta(self, conta):
    if self.__contas == []:
      self.__contas.append(conta)
      print('Conta adicionada')
    else:
      for c in self.__contas:
        if c != conta:
          self.__contas.append(conta)
        else:
          print('Não é possível adicionar a mesma conta')

  def remover_Contas(self, conta):
    if conta in self.__contas:
      self.__contas.remove(conta)
      print('CONTA REMOVIDA')
    else:
      print('A conta não existe mais')

  def valorTotal(self):
    valor_total = 0
    for c in range(len(self.__contas)):
      valor_total += self.__contas[c].saldo ## COMO FAÇO PRA ACESSAR OS ATRIBUTOS DO OBJETO QUE TÁ NA LISTA DA CLASSE AGREGADA PELA CLASSE AGREGADORA???
    return valor_total
    print('A SOMA TOTAL É ESSA')
      
  def __str__(self):
    valorT = 0
    for c in range(len(self.__contas)):
      valorT += self.__contas[c].saldo
    return f'O banco é {self.__nome} que possui no caixa um valor total de R${valorT},00'

class Conta:
  def __init__(self, numero, titular, saldo=0):
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo

  @property
  def numero(self):
    return self.__numero

  @property
  def saldo(self):
    return self.__saldo

  @property
  def titular(self):
    return self.__titular

  def depositar(self, valor):
    self.__saldo += valor
    print(f'Seu saldo é de R${self.__saldo}')
  
  def sacar(self, valor):
    if valor > self.__saldo:
      print('Não é possível sacar este valor, pois o valor é maior do que o valor q tem na conta')
    else:
      self.__saldo -= valor
      print('Saque Efetuado')

  def __str__(self):
    return f'O numero da conta é {self.__numero}, seu saldo é {self.__saldo}'


class Cliente:
  def __init__(self, nome, cpf):
    self.__nome = nome
    self.__cpf = cpf
  
  @property
  def nome(self):
    return self.__nome
  
  @property
  def cpf(self):
    return self.__cpf
  
  def __str__(self):
    return f'O nome do cliente é {self.__nome} e o CPF que está vinculado é {self.__cpf}'


#CLIENTES
cliente1 = Cliente('Kleber de Sousa Júnior', '05277829393')
cliente2 = Cliente('Cristiane Borges dos Santos', '09898715643')
cliente3 = Cliente('Lucia Maria Sousa da Silva', '94159482312')

#CONTAS
conta1 = Conta('01', cliente1, 8000)
conta2 = Conta('02', cliente2, 10000)
conta3 = Conta('03', cliente3, 50000)
conta4 = Conta('04', cliente1, 20000)
conta5 = Conta('05', cliente2, 5000)
conta6 = Conta('06', cliente3, 100000)

#BANCOS
banco1 = Banco('Itau')
banco2 = Banco('Brasil')
banco3 = Banco('Caixa')


#EXE
banco1.adicionar_Conta(conta1)
conta1.sacar(5000)
conta1.saldo
banco1.adicionar_Conta(conta1)
banco1.adicionar_Conta(conta2)

banco1.adicionar_Conta(conta5)
banco1.valorTotal()
banco1.contas
conta1.saldo
conta2.saldo
conta5.saldo
conta5.sacar(3500)
banco1.valorTotal()
conta1.depositar(14000)
banco1.valorTotal()

banco2.adicionar_Conta(conta1)
conta1.saldo
banco3.adicionar_Conta(conta6)
conta6.saldo
banco3.adicionar_Conta(conta1)
banco3.valorTotal()
banco3.remover_Contas(conta1)
banco3.valorTotal()

