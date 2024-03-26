class Macaco:
  def __init__(self, nome):
    self.nome = nome
    self.bucho = []

  def comer(self, alimento):
    self.bucho.append(alimento)

  def verBucho(self):
    return self.bucho
  
  def digerir(self):
    self.bucho.pop(0)
    
m1 = Macaco('Samuel')
m2 = Macaco('Leo')
print(m1.verBucho())
 
m1.comer('banana ')
m1.comer('laranja ')
print(m1.verBucho())
 
m1.digerir()
print(m1.verBucho())
 
m1.comer(m2.nome)
print(m1.verBucho())