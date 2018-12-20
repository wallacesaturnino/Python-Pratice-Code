class Pessoa:
  
  __listaVinculo = ["Indefinido", "Sócio", "Dependente", "Convidado"]
  __identificacao = ""
  
  def __init__(self, vinculo=0, socio=0):
    self.__vinculo = vinculo
    self.__socio = socio
    self.__dependentes = []
    self.__animais = []

  def getVinculo(self):
    return self.__listaVinculo[self.__vinculo]

  def setVinculo(self, vinculo):
    self.__vinculo = vinculo
  
  vinculo = property(
    fset = setVinculo,
    fget = getVinculo)
  
  def setIdentificacao(self, identificacao):
    if self.getVinculo() == "Indefinido":
      print("Não é permitido identificar pessoa sem vínculo")
      return False
    elif self.getVinculo() == "Sócio":
      if len(identificacao) != 8:
        print("Id do sócio deve ser de 8 caracteres!")
        return False
      else:
        self.__identificacao = identificacao
        return True
    elif self.getVinculo() == "Dependente":
      if len(identificacao) != 4:
        print("Id do dependente deve ser de 4 caracteres!")
        return False
      else:
        self.__identificacao = identificacao
        return True
    elif self.getVinculo() == "Convidado":
      if len(identificacao) != 14:
        print("Id do convidado deve ser de um CPF de 11 caracteres!")
        return False
      else:
        self.__identificacao = identificacao
        return True
    else:
      return False
  
  def getIdentificacao(self):
    return self.__identificacao
  
  identificacao = property(
    fset = setIdentificacao,
    fget = getIdentificacao)
  
  def adicionarDependente(self, dependente):
    if len(self.__dependentes) < 10:
      self.__dependentes.append(dependente)
      return True
    else:
      return False
  
  def adicionarAnimal(self, animal):
    if len(self.__animais) < 5:
      self.__animais.append(animal)
      return True
    else:
      return False
  
  def consultarDependentes(self):
    return self.__dependentes
  
  def consultarAnimais(self):
    return self.__animais
  
  def removerAnimal(self, animal):
    if animal in self.__animais:
      self.__animais.remove(animal)
      return True
    else:
      return False
  
  def removerDependente(self, dependente):
    if dependente in self.__dependentes:
      self.__dependentes.remove(dependente)
      return True
    else:
      return False
  
  def getSocio(self):
    return self.__socio
  
  def __str__(self):
    if self.__vinculo == 0:
      return "Indefinido"
    elif self.__vinculo == 1:
      if self.getIdentificacao() != "":
       return self.getIdentificacao()
      else:
        return "notID"
    elif self.__vinculo == 2:
      if self.__socio != 0:
        if self.getIdentificacao() != "":
          return str(self.__socio) + "D" + self.getIdentificacao()
        else:
          return "notID"
      else:
        return self.getIdentificacao()
    else:
      if self.__socio != 0:
        if self.getIdentificacao() != "":
          return str(self.__socio) + "C" + self.getIdentificacao()
        else:
          return "notID"
      else:
        return self.getIdentificacao()

  def __cmp__(self, other):
    return self.getIdentificacao == other.getIdentificacao