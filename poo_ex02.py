class Quadrado:
  def __init__(self, lado):
    self.lado = lado

  def mudarLado(self, lado):
    self.lado = lado

  def get_lado(self):
    return self.lado
  
  def calculaArea(self):
    return self.lado * self.lado
 
q1 = Quadrado(2)
print(q1.get_lado())
print(q1.calculaArea())
 
q1.mudarLado(6)
print(q1.lado)
print(q1.calculaArea())
