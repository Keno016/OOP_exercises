class Bola:
  def __init__(self, cor, circ, material):
    self.cor = cor
    self.circ = circ
    self.material = material

  def trocaCor(self, cor):
    self.cor = cor

  def mostraCor(self):
    return self.cor
  
b1 = Bola('amarela', 2, 'papel')
print(b1.mostraCor())
b1.trocaCor('azul')
print(b1.mostraCor())
