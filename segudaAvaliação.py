
''' Segunda Prova de POO realizada em coletiva pelos alunos
Miguel Ernesto da Silva Filho
Gildeir Barbosa de Oliveira '''

class Cliente:
    def __init__(self,nome, idade,cpf,):

        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return f'nome: {self.__nome}\ncpf: {self.__cpf}\nidade: {self.__idade}'

class Seguro:
    def __init__(self, numero_apolice, proprietario):
        self._numero_apolice = numero_apolice
        if type(proprietario) == Cliente:
            self._proprietario = proprietario
        else:
            self._proprietario = None

    def __str__(self):
        return f'nome: {self._proprietario},\nnumero apolice: {self._numero_apolice}'

    def calcularValor(self):
        pass
    def calcularPremio(self):
        pass

class SeguroVida(Seguro):

    def __init__(self, numero_apolice, proprietario, nome_beneficiario):
        super().__init__(numero_apolice, proprietario)
        self.__nome_beneficiario = nome_beneficiario

    @property
    def nome_beneficiario(self):
        return self.__nome_beneficiario

    def calcularValor(self):
        valor = 0
        if self._proprietario.idade <= 30:
            valor = 800
        elif self._proprietario.idade >= 31 and self._proprietario.idade <= 50:
            valor = 1300
        elif self._proprietario.idade > 50:
            valor = 1600
        return valor

    def calcularPremio(self):
        valor = 0
        if self._proprietario.idade <= 30:
            valor = 50000
        elif self._proprietario.idade >= 31 and self._proprietario.idade <= 50:
            valor = 30000
        elif self._proprietario.idade > 50:
            valor = 20000
        return valor

    def __str__(self):
        return f'numero apolice: {self._numero_apolice}\nproprietario: {self._proprietario.nome}\nnome beneficiario: {self.__nome_beneficiario}\nvalor: {self.calcularValor()}\npremio:{self.calcularPremio()}'

class SeguroVeiculo(Seguro):
    def __init__(self, numero_apolice, proprietario, numero_licenca, nome_modelo, ano, valor_veiculo):
        super().__init__(numero_apolice, proprietario)
        self.__numero_licenca = numero_licenca
        self.__nome_modelo = nome_modelo
        self.__ano = ano
        self.__valor_veiculo = valor_veiculo

    @property
    def numero_licenca(self):
        return  self.__numero_licenca
    @property
    def nome_modelo(self):
        return self.__nome_modelo
    @property
    def ano(self):
        return self.__ano
    @property
    def valorAutomovel(self):
        return self.__valor_veiculo

    def calcularValor(self):
        valorSeguro = self.__valor_veiculo * 0.03
        return valorSeguro

    def calcularPremio(self):
        premio = self.__valor_veiculo * 0.8
        return premio

    def calcularFranquia(self):
        franquia = (self.__valor_veiculo * 0.03) * 0.4
        return franquia

    def __str__(self):
        return f'numero apolice: {self._numero_apolice}\nnome do segurado: {self._proprietario.nome}\nvalor: {self.calcularValor():.0f}\npremio: {self.calcularPremio():.0f}\nfranquia: {self.calcularFranquia():.0f}'




class ControledeSeguros:
    def __init__(self, total_valores=0, total_premio=0):
        self._seguros = []
        self._total_valores = total_valores
        self._total_premio = total_premio


    def adicionarSeguros(self, seguro):

        if isinstance(seguro, Seguro):
            self._seguros.append(seguro)
            print('cadastro realizado com sucesso!')
        else:
            print("objeto inválido")

    def relatorio(self):
        self._total_valores = 0
        segVei = segVida = 0
        for i in self._seguros:
            self._total_valores += i.calcularValor()
            self._total_premio += i.calcularPremio()
            if type(i) is SeguroVeiculo:
                segVei += 1
            else:
                segVida += 1
            print(i)
            print()
        print(f"Seguro de Veiculo (Qtd): {segVei}\nSeguro de Vida (Qtd): {segVida}")

    @property
    def total_valores(self):
        return self._total_valores
    @property
    def total_premio(self):
        return self._total_premio


BBseguros = ControledeSeguros()
Antonio = Cliente('Antonio',20,10000)
Jose = Cliente('Jose',35,20000)
Ricardo = Cliente('Ricardo', 54, 30000)
BBseguros.adicionarSeguros(SeguroVida(3,Antonio, 'Antonio'))
BBseguros.adicionarSeguros(SeguroVida(1,Antonio, 'Miguel'))
BBseguros.adicionarSeguros(SeguroVeiculo(2, Jose, 10, 'Camaro', 2020, 450000))
BBseguros.adicionarSeguros(SeguroVida(4,Ricardo,Jose))
BBseguros.relatorio()
print(f"O Total dos Valores: R$ {BBseguros._total_valores:.2f}")
print(f"O Total dos Premios: R$ {BBseguros._total_premio:.2f}")
