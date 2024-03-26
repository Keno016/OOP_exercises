class Tamaguchi:
  def __init__(self, nome, fome, saude, idade):
    self.nome = nome
    self.fome = fome
    self.saude = saude
    self.idade = idade

  # Alterando valores
  def alteraNome(self, nome):
    self.nome = nome

  def alteraFome(self, fome):
    self.fome = fome

  def alteraSaude(self, saude):
    self.saude = saude

  def alteraIdade(self, idade):
    self.idade = idade

  # Retornando valores
  def get_nome(self):
    return self.nome
  
  def get_fome(self):
    return self.fome
  
  def get_saude(self):
    return self.saude
  
  def get_idade(self):
    return self.idade
  
  def humor(self):
    if((self.saude + self.fome) >= 10):
      print(f'{self.nome} está feliz!!')
    else:
      print(f'{self.nome} está triste... :(')
      
tama1 = Tamaguchi('eno', 5, 5, 2)
print(tama1.get_nome())
print(tama1.get_fome())
print(tama1.get_saude())
print(tama1.get_idade())
tama1.humor()
tama1.alteraFome(2)
tama1.humor()