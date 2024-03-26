class ContaCorrente:
  def __init__(self, nome, numero, saldo = 0):
    self.nome = nome
    self.numero = numero
    self.saldo = saldo

  def alteraNome(self, nome):
    self.nome = nome
 
  def depositar(self, saldo):
    self.saldo = self.saldo + saldo

  def saque(self, saldo):
    self.saldo = self.saldo - saldo

conta1 = ContaCorrente('Vinícius', '1234567', 35)
print(f'O titular {conta1.nome}, do numero {conta1.numero}, tem um saldo de R${conta1.saldo}')
conta1.alteraNome('Keno')
print(f'O titular {conta1.nome}, do numero {conta1.numero}, tem um saldo de R${conta1.saldo}')
conta1.depositar(20)
print(f'O titular {conta1.nome}, do numero {conta1.numero}, tem um saldo de R${conta1.saldo}')
conta1.saque(5)
print(f'O titular {conta1.nome}, do numero {conta1.numero}, tem um saldo de R${conta1.saldo}')
