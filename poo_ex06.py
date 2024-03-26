class Tv:
  def __init__(self, canal, volume):
    self.canal = canal
    self.volume = volume

  def mudaCanal(self, canal):
    if(canal > 0 and canal <= 10):
      self.canal = canal
    else:
      print('Canal não existe')
 
  def aumentaVolume(self):
    if(self.volume < 10):
      self.volume = self.volume + 1
    else:
      print('Volume no máximo')

  def diminuiVolume(self):
    if(self.volume >= 1):
      self.volume = self.volume - 1
    else:
      print('Volume no mínimo')
 
 
tv1 = Tv(2, 5)
print(f'A Tv está no canal {tv1.canal} com {tv1.volume} de volume')
tv1.mudaCanal(1)
tv1.aumentaVolume()
print(f'A Tv está no canal {tv1.canal} com {tv1.volume} de volume')
