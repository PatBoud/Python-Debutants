# Ce programme démontre l'utilisation de fonctions
#

# --------------------------------------------------------------------------------------------------
# Fonction qui retourne le nombre le plus grand parmi la liste fournie en paramètre.
# Cette liste est stockée dans la variable "nombres".
def plusGrand(nombres):
  # Il nous faut un point de départ avant de faire des comparaisons.
  # Déterminons que le plus grand nombre est le tout premier élément de la liste de nombres.
  # nombres[0] représente ce premier élément.  nombres[4] représenterait le 5ème élément.
  plusGrandNombre = nombres[0]

  # Boucle dans la liste de nombres
  for nb in nombres:
    # Si le nombre actuel est plus grand que le plus grand nombre trouvé jusqu'à maintenant...
    if (nb > plusGrandNombre):
      # ... le nombre actuel devient donc le plus grand nombre connu.
      plusGrandNombre = nb

  # Le plus grand nombre a été trouvé.
  # La fonction retourne maintenant celui-ci.
  return (plusGrandNombre)



# --------------------------------------------------------------------------------------------------
# Fonction qui retourne le nombre le plus petit parmi la liste fournie en paramètre.
# Cette liste est stockée dans la variable "nombres".
def plusPetit(nombres):
  # Il nous faut un point de départ avant de faire des comparaisons.
  # Déterminons que le plus petit nombre est le tout premier élément de la liste de nombres.
  # nombres[0] représente ce premier élément.  nombres[4] représenterait le 5ème élément.
  plusPetitNombre = nombres[0]

  # Boucle dans la liste de nombres
  for nb in nombres:
    # Si le nombre actuel est plus petit que le plus petit nombre trouvé jusqu'à maintenant...
    if (nb < plusPetitNombre):
      # ... le nombre actuel devient donc le plus petit nombre connu.
      plusPetitNombre = nb

  # Le plus petit nombre a été trouvé.
  # La fonction retourne maintenant celui-ci.
  return (plusPetitNombre)


# --------------------------------------------------------------------------------------------------
# Fonction qui reçoit une liste de nombres en paramètre.
# Elle appelle ensuite les fonctions plusGrand() et plusPetit() pour connaitre ces nombres.
# Elle affiche ensuite un rapport contenant la liste des nombres et indique quels sont 
# le plus petit et le plus grand.
def afficheRapport(nombres):
  petitNombre = plusPetit(nombres)
  grandNombre = plusGrand(nombres)

  print ("Voici la liste des nombres:")
  print (nombres)
  print ("Le plus petit nombre est: " + str(petitNombre))
  print ("Le plus grand nombre est: " + str(grandNombre))



# =================================================================================================
# Programme principal:
# Démontre diverses façons d'appeler les fonctions définies ci-haut.
# =================================================================================================


# 1.
# La fonction plusGrand() est appelée en fournissant directement une liste de nombres en paramètre
# et le résultat est retourné dans la variable "grandNombre"
grandNombre = plusGrand([10,21,45,176,123,47,96,101])
print ("")
print ("1. Le plus grand nombre est: " + str(grandNombre))


# 2.
# Une variable "listeDeNombres" est d'abord créée, et contient une liste de nombres.
# La fonction plusGrand() est appelée en fournissant cette variable en paramètre
# et le résultat est retourné dans la variable "grandNombre"
listeDeNombres = [114, 45, 32, 97, 42, 64, 28, 75, 101, 17]
grandNombre = plusGrand(listeDeNombres)
print ("")
print ("2. Le plus grand nombre est: " + str(grandNombre))

# Puisque la liste de nombres est dans une variable (la variable listeDeNombres), il devient ainsi facile 
# d'appeler la fonction plusPetit() pour connaître le plus petit nombre de la même liste
petitNombre = plusPetit(listeDeNombres)
print ("2. Le plus petit nombre est: " + str(petitNombre))



# 3.
# Nous réutilisons la variable "listeDeNombres" créée précédemment.
# La fonction afficheRapport() est appelée. Consultez sa définition pour savoir ce qu'elle fait.
print ("")
print ("3. Affichage du rapport")
afficheRapport(listeDeNombres)