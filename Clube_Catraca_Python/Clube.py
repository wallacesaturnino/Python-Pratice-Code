class Clube:
  
  __socios = []
  __visitantes = []
  __animais = []
  __lotacaoPessoa = 0
  __lotacaoAnimal = 0
  
  def capacidadePessoa(self):
    return 1000
  
  def capacidadeAnimal(self):
    return 100
  
  def adicionarVisitante(self, visitante):
    if self.__lotacaoPessoa < self.capacidadePessoa():
      self.__visitantes.append(visitante)
      self.__lotacaoPessoa = self.__lotacaoPessoa + 1
      return True
    else:
      return False
  
  def removerVisitante(self, visitante):
    if visitante in self.__visitantes:
      self.__visitantes.remove(visitante)
      return True
    else:
      return False
  
  def consultarVisitantes(self):
    return self.__visitantes
  
  def adicionarAnimal(self, animal):
    if self.__lotacaoAnimal < self.capacidadeAnimal():
      self.__animais.append(animal)
      self.__lotacaoAnimal = self.__lotacaoAnimal + 1
      return True
    else:
      return False
  
  def removerAnimal(self, animal):
    if animal in self.__animais:
      self.__animais.remove(animal)
      return True
    else:
      return False
  
  def consultarAnimais(self):
    return self.__animais
  
  def adicionarSocio(self, socio):
    if socio not in self.__socios:
      self.__socios.append(socio)
      return True
    else:
      return False
  
  def removerSocio(self, socio):
    if socio in self.__socios:
      self.__socios.remove(socio)
      return True
    else:
      return False
  
  def consultarSocio(self):
    return self.__socios