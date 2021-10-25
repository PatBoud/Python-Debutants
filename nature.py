# Ce fichier est un module de classes.
# Il est importé dans objet.py .
# Il ne fait rien comme tel.

class animal():
  def __init__(self, espece, nom):
    self.espece = espece
    self.nom = nom
    self.pattes = 0
  
  def getNom(self):
    return self.nom

  def getEspece(self):
    return self.espece
  
  def sonne(self):
    return "(Aucun son)"

  def getPattes(self):
    return self.pattes
  
  def getDetails(self):
    return ""
 

# Classe mammifere, qui hérite de la classe animal
class mammifere(animal):
  def __init__(self, espece, nom, pattes, son):
    super().__init__(espece, nom)
    self.pattes = pattes
    self.son = son

  def sonne(self):
    print(self.son)

# Classe reptile, qui hérite de la classe animal
class reptile(animal):
  def __init__(self, espece, nom, pattes, veneneux):
    super().__init__(espece, nom)
    self.pattes = pattes
    self.veneneux = veneneux

  def getDetails(self):
    if (self.veneneux):
      return "ATTENTION! Vénéneux!"
    else:
      return ("")

# Classe arachnide, qui hérite de la classe animal
class arachnide(animal):
  def __init__(self, espece, nom, pattes, veneneux):
    super().__init__(espece, nom)
    self.pattes = pattes
    self.veneneux = veneneux

  def getDetails(self):
    if (self.veneneux):
      return "Attention! Vénéneux!"