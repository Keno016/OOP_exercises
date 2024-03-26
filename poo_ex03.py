class Retangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def mudaValor(self, base, altura):
    self.base = base
    self.altura = altura

  def get_base(self):
    return self.base
  
  def get_altura(self):
    return self.altura
  
  def calculaArea(self):
    return self.base * self.altura
  
  def calculaPerimetro(self):
    return ((self.base * 2) + (self.altura * 2))
  
r1 = Retangulo(5, 2)
 
print(r1.calculaArea())
print(r1.calculaPerimetro())
