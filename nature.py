# Ce fichier est un module de classes.
# Il est importé dans objet.py .
# Il ne fait rien comme tel.

class animal():
  # Constructeur
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
  # Constructeur
  def __init__(self, espece, nom, pattes, son):
    # Appel du constructeur de la classe parent
    super().__init__(espece, nom)

    # Définition des variables privées à partir des valeurs
    # reçues en paramètres au constructeur
    self.pattes = pattes
    self.son = son

  def sonne(self):
    print(self.son)


# Classe reptile, qui hérite de la classe animal
class reptile(animal):
  # Constructeur
  def __init__(self, espece, nom, pattes, veneneux):
    # Appel du constructeur de la classe parent
    super().__init__(espece, nom)

    # Définition des variables privées à partir des valeurs
    # reçues en paramètres au constructeur
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
    # Appel du constructeur de la classe parent
    super().__init__(espece, nom)

    # Définition des variables privées à partir des valeurs
    # reçues en paramètres au constructeur
    self.pattes = pattes
    self.veneneux = veneneux

  def getDetails(self):
    if (self.veneneux):
      return "ATTENTION! Vénéneux!"
    else:
      return ("")