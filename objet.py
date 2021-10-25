# Importation du module de classes contenant les classes d'animaux
from nature import *

# Création d'objets à partir des classes d'animaux
chien1 = mammifere("chien", "Billie", 4, "ouaf!")
chien2 = mammifere("chien", "Rex", 4, "ouaf!")
chat = mammifere("chat", "Rubis", 3, "miaaaaaaaou")
araignee = arachnide("araignée", "LaMort", 8, True)
rat1 = mammifere("rat", "Shaki", 4, "koui koui!")
rat2 = mammifere("rat", "Kora", 4, "koui koui!")
gecko = reptile("gecko", "Paul", 4, False)
serpent = reptile("serpent", "Black", 0, True)

# Création d'une liste d'animaux contenant tous les
# objets animaux créés précédemment.
# Ceci facilitera l'utilisation d'une boucle pour afficher 
# leurs informations.
animaux = [chien1, chien2, chat, araignee, rat1, rat2, gecko, serpent]


print ("========================================")
print ("")

# Boucle dans la liste d'animaux
for anim in animaux:
  print (anim.getNom() + ", " + anim.getEspece() + ", " + str(anim.getPattes()) + " pattes")
  anim.sonne()
  print (anim.getDetails())
  print ("---------------------")