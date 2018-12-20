from Clube import Clube
from Catraca import Catraca
from Pessoa import Pessoa
from Animal import Animal

class Main:
  
  clube = Clube()
  ctr = Catraca(clube)

  sc1 = Pessoa(1)
  sc2 = Pessoa(1)
  sc1.setIdentificacao("socio001")
  sc2.setIdentificacao("socio002")
  
  clube.adicionarSocio(sc1)
  clube.adicionarSocio(sc2)
  
  dp1 = Pessoa(2, sc1)
  dp1.setIdentificacao("dp01")

  an1 = Animal(1, sc1)
  an1.setIdentificacao("a1")

  if ctr.entradaPessoa(sc1):
    print("Pessoa: "+str(sc1)+" entrou no clube")
    
  if ctr.entradaPessoa(dp1):
    print("Pessoa: "+str(dp1)+" entrou no clube")
  
  if ctr.entradaAnimal(an1):
    print("Animal: "+str(an1)+" entrou no clube")
  
  print("\nLista de visitantes no clube:")
  for v in clube.consultarVisitantes():
    print(" - "+str(v))
  
  print("\nLista de animais no clube")
  for a in clube.consultarAnimais():
    print(" - "+str(a))
  
  if ctr.saidaPessoa(sc1):
    print("\nPessoa: "+str(sc1)+" Saiu do clube.")
  else:
    print("\nPessoa: "+str(sc1)+" Não entrou no clube hoje.")
  
  print("\nLista de visitantes no clube:")
  for v in clube.consultarVisitantes():
    print(" - "+str(v))
  
  print("\nLista de animais no clube")
  for a in clube.consultarAnimais():
    print(" - "+str(a))