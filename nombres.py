# Ce programme démontre l'utilisation de fonctions
#

# Fonction qui retourne le nombre le plus grand parmi la liste fournie en paramètre.
# Cette liste est stockée dans la variable "nombres".
def lePlusGrand(nombres):
  plusGrandNombre = 0

  # Boucle dans la liste de nombres
  for nb in nombres:
    # Si le nombre actuel est plus grand que le plus grand nombre trouvé jusqu'à maintenant...
    if (nb > plusGrandNombre):
      # ... le nombre actuel devient donc le plus grand nombre connu.
      plusGrandNombre = nb

  # Le plus grand nombre a été trouvé.
  # La fonction retourne maintenant celui-ci.
  return (plusGrandNombre)



# Programme principal

print ("Affichage du plus grand nombre à partir d'une liste")

# La fonction lePlusGrand() est appelée et le résultat est retourné dans la variable "grandNombre"
grandNombre = lePlusGrand([10,21,45,176,123,47,96,101])

print ("Le plus grand nombre est: " + str(grandNombre))

