class Animal:
  
  __tipoAnimal = ["Indefinido", "Gato", "Cachorro", "Pássaro", "Réptil"]
  _identificacao = ""
  
  def __init__(self, tipo=0, socio=0):
    self.__tipo = tipo
    self.__socio = socio
  
  def setIdentificacao(self, identificacao):
    if len(identificacao) != 2:
      print("Id do Animal deve ser de 2 caracteres!")
      return False
    else:
      self._identificacao = identificacao
      return True
  
  def getIdentificacao(self):
    return self._identificacao
  
  __identificacao = property(
    fget = getIdentificacao,
    fset = setIdentificacao)
  
  def getSocio(self):
    return self.__socio
  
  def __cmp__(self, other):
    return self.getIdentificacao() == other.getIdentificacao()
  
  def __str__(self):
    if self.__socio != 0:
      if self.getIdentificacao() != "":
        return str(self.__socio) +"A"+ self.getIdentificacao()
      else:
        return "notID"
    else:
      return self.getIdentificacao()