class property:
  @property
  def saldo(self):
    return self._saldo
    
@saldo.setter
def saldo(self, saldo):
  if (saldo < 0):
    print("o saldo não pode ser negativo")
  else:
    self._saldo = saldo
