class Relogio:
  def __init__(self, horas, minutos, segundos):
    self.horas = horas
    self.minutos = minutos
    self.segundos = segundos

  def mudar_horas(self, horaas):
    if horaas >= 0 and horaas <= 23:
      self.horas = horaas
    else:
      print('Não é possível mudar as horas, digite um valor válido')

  def mudar_minutos(self, minutoos):
    if minutoos >= 0 and minutoos:
      self.minutos = minutoos
    else:
      print('Não é possível ajustar os minutos')

  def mudar_segundos(self, segundoos):
    if segundoos >= 0 and segundoos <= 60:
      self.segundos = segundoos
    else:
      print('Não é possível ajustar os segundos:')

  def mostrar_horario(self):
    print(f'Neste relógio são marcado exatamente {self.horas}horas {self.minutos}minutos e {self.segundos}segundos')


relogio1 = Relogio(0, 0, 0)
relogio1.mudar_horas(15)
relogio1.mudar_minutos(12)
relogio1.mudar_segundos(58)

relogio2 = Relogio(0,0,0)
relogio2.mudar_horas(12)
relogio2.mudar_minutos(32)
relogio2.mudar_segundos(12)

relogio1.mostrar_horario()

relogio2.mostrar_horario()