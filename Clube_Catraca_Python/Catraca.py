class Catraca:
  
  def cod(self):
    return "XPTO"
  
  def __init__(self, clube):
    self.__clube = clube
  
  def identificarPessoa(self, pessoa):
    if pessoa.getVinculo() == "Sócio":
      if pessoa in self.__clube.consultarSocio():
        return self.cod() +""+ str(pessoa)
      else:
        return str(pessoa)
    else:
      if pessoa.getSocio() in self.__clube.consultarSocio():
        return self.cod() +""+ str(pessoa)
      else:
        return str(pessoa)
  
  def identificarAnimal(self, animal):
    if animal.getSocio() in self.__clube.consultarSocio():
      return self.cod() +""+ str(animal)
    else:
      return str(animal)
  
  def entradaPessoa(self, pessoa):
    if self.identificarPessoa(pessoa) == self.cod() +""+ str(pessoa) and self.__clube.adicionarVisitante(pessoa):
      return True
    else:
      return False

  def entradaAnimal(self, animal):
    if self.identificarAnimal(animal) == self.cod() +""+ str(animal) and self.__clube.adicionarAnimal(animal):
      return True
    else:
      return False
  
  def saidaPessoa(self, pessoa):
    return self.__clube.removerVisitante(pessoa)
  
  def saidaAnimal(self, animal):
    return self.__clube.removerAnimal(animal)