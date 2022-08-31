class Bicicleta:
    def __init__(self, velocidade_atual, altura_cela, calibragem_pneus):
        self.velocidade_atual = velocidade_atual
        self.altura_cela = altura_cela
        self.calibragem_pneus = calibragem_pneus
        self.altura_maxima = 100
        self.altura_minima = 5
        self.calibragem_maxima = 30
        self.calibragem_minima = 0
        self.velocidade_maxima = 65
        self.velocidade_minima = 0

    def regular_cela(self, altura):
        if self.velocidade_atual == 0:
            self.altura_cela += altura
            if self.altura_cela > self.altura_maxima:
                self.altura_cela = self.altura_maxima
            if self.altura_cela < self.altura_minima:
                self.altura_cela = self.altura_minima

            print(f'A altura da cela da  bicicleta é de {self.altura_cela:.1f}cm')
        else:
            print(f'Não podemos ajustar a altura da cela se a bike estiver em movimento')

    def calibrar_pneus(self, ar):
        if self.velocidade_atual == 0:
            self.calibragem_pneus += ar
            if self.calibragem_pneus < self.calibragem_minima:
                self_calibragem_pneus = self.calibragem_minima

            if self.calibragem_pneus > self.calibragem_maxima:
                self.calibragem_pneus = self.calibragem_maxima
            print(f'A calibragem dos pneus foi reajustada para {self.calibragem_pneus}')
        else:
            print('Não podemos calibrar os pneus da bike se ela estiver em movimento')

    def acelerar(self, velocidade):
        self.velocidade_atual += velocidade
        if self.velocidade_atual > self.velocidade_maxima:
            self.velocidade_atual = self.velocidade_maxima
            print(f'A velocidade da bicicleta é de {self.velocidade_atual}km/h')

        elif self.velocidade_atual < 0:
            self.velocidade_atual = 0
            print(f'A velocidade da bicicleta é de {self.velocidade_atual}km/h')

        else:
            print(f'A velocidade da bicicleta é de {self.velocidade_atual}km/h')


bicicleta1 = Bicicleta(12, 34, 25)
bicicleta1.regular_cela(50)
bicicleta1.calibrar_pneus(40)
bicicleta1.acelerar(23)

print(' ')

bicicleta2 = Bicicleta(55, 32, 5)
bicicleta2.regular_cela(1000)
bicicleta2.regular_cela(-1000)
bicicleta2.calibrar_pneus(20)
bicicleta2.acelerar(20)


