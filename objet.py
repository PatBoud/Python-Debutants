# Importation du module de classes contenant les classes d'animaux
from nature import *

# Importation de la méthode time.sleep(), pour ralentir un peu l'exécution
# en ajoutant des délais pendant l'affichage de la liste
from time import sleep

# Création d'objets à partir des classes d'animaux
chien1 = mammifere("chien", "Billie", 4, "ouaf!")
chien2 = mammifere("chien", "Rex", 4, "ouaf!")
chat = mammifere("chat", "Rubis", 3, "miaaaaaaaou")
rat1 = mammifere("rat", "Shaki", 4, "koui koui!")
rat2 = mammifere("rat", "Kora", 4, "koui koui!")
araignee = arachnide("araignée", "LaMort", 8, True)
gecko = reptile("gecko", "Paul", 4, False)
lezard = reptile("lézard", "Bob", 4, False)
serpent = reptile("serpent", "Black", 0, True)

# Création d'une liste d'animaux contenant tous les
# objets animaux créés précédemment.
# Ceci facilitera l'utilisation d'une boucle pour afficher 
# leurs informations.
animaux = [chien1, chien2, lezard, chat, araignee, rat1, rat2, gecko, serpent]

print ("")
print ("========================================")
print ("            LISTE D'ANIMAUX             ")
print ("========================================")
print ("")

# Boucle dans la liste des objets animaux pour afficher leurs informations.
# Dans chaque cycle de la boucle, "anim" représente l'élément actuel dans la liste.
# On obtient les informations de chacun en invoquant les méthodes .getNom(), getEspece() et getPattes() .
for anim in animaux:
  print (anim.getNom() + ", " + anim.getEspece() + ", " + str(anim.getPattes()) + " pattes")
  anim.sonne()
  if (anim.getDetails() != ""):
    print (anim.getDetails())
  print ("-------------------------------")
  # Délais de 0.25 seconde)
  sleep(0.25)

print ("")
print ("========================================")
print ("            Fin de la liste             ")
print ("========================================")
print ("")