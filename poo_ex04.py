class Pessoa:
  def __init__(self, nome, idade, peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura

  def envelhecer(self):
    if(self.idade < 21):
      self.altura = self. altura + 0.05
    self.idade = self.idade + 1

  def engordar(self, peso):
    self.peso = self.peso + peso

  def emagrecer(self, peso):
    self.peso = self.peso - peso

  def crescer(self, altura):
    self.altura = self.altura + altura

p1 = Pessoa('Vinícius', 20, 55, 1.75)
print(f'{p1.nome} tem {p1.idade} anos com {p1.peso}kg e {p1.altura}cm')
p1.envelhecer()
print(f'{p1.nome} tem {p1.idade} anos com {p1.peso}kg e {p1.altura}cm')
p1.envelhecer()
print(f'{p1.nome} tem {p1.idade} anos com {p1.peso}kg e {p1.altura}cm')
p1.engordar(5)
p1.emagrecer(2)
p1.crescer(0.04)
print(f'{p1.nome} tem {p1.idade} anos com {p1.peso}kg e {p1.altura}cm')
