class ContaCorrente:
    def __init__(self, numero, saldo):
        self.__numero=numero
        self.__saldo=saldo

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, value):
        self.__saldo = value

    def creditar(self, value):
        self.__saldo += value
        print(f'O valor de R${value} foi creditado!')

    def debitar(self, value):
        if self.saldo >= value:
            self.__saldo -= value
            print(f'O valor de R${value} foi debitado!')
        else:
            print("Saldo insuficiente!")

    def transferir(self, value, conta):
        if type(conta) == ContaCorrente or ContaPoupança or ContaImposto:
            if self.saldo >= value:
                conta.__saldo += value
                self.__saldo -= value
                print("O valor de R${} foi transferido para a conta {}"\
                    .format(value, conta.__numero))
            else:
                print("Saldo insuficiente para essa transferência!")
        else:
            print("Conta indisponível!")
    
    def __str__(self):
        return "Número da conta: {} ==> Saldo: R${}"\
        .format(self.__numero, self.saldo)


class ContaPoupança(ContaCorrente):
    def __init__(self, numero, saldo, taxa_juros):
        super().__init__(numero, saldo)
        self.__taxa_juros = taxa_juros

    def renderJuros(self):
        self.saldo += self.saldo * self.__taxa_juros/100
        print("Os juros estão rendendo!")


class ContaImposto(ContaCorrente):
    def __init__(self, numero, saldo, percentual_imposto):
        super().__init__(numero, saldo)
        self.__percentual_imposto = percentual_imposto

    def calcula_imposto(self):
        self.saldo -= self.saldo*self.__percentual_imposto/100
        print("Impostos calculados!")
        
        
conta1 = ContaCorrente(12432, 50)
conta2 = ContaCorrente(43215, 0)
conta3 = ContaPoupança(42342, 0, 5)
conta4 = ContaPoupança(99283, 170, 10)
conta5 = ContaImposto(52312, 500, 25)
conta6 = ContaImposto(33333, 439, 8)

conta1.creditar(70)
conta2.transferir(500, conta3)
conta2.debitar(2)
conta1.transferir(20, conta2)
conta3.renderJuros()
conta3.debitar(80)
conta4.renderJuros()
conta5.calcula_imposto()
conta5.debitar(200)
conta6.calcula_imposto()
conta6.creditar(11)
print(conta1)
print(conta2)
print(conta3)
print(conta4)
print(conta5)
print(conta6)
        
        
        
  
