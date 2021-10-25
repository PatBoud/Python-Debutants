# Une question est affichée à l'écran.
print ("")
print("Salut! Quel est ton nom?")

# L'utilisateur entre sa réponse.
# La réponse est placée dans la variable "nom".
nom = input("")

print("")
print("Ah! Bonjour, " + nom + " !")

# Une autre question est affichée à l'écran.
print("Quel âge as-tu? (Entre seulement le nombre!)")

# L'utilisateur entre sa réponse.
# La réponse est placée dans la variable "age", et doit être convertie en nombre entier (int) 
# car elle sera utilisé plus tard dans une boucle.
age = int(input(""))


# Initialisation de variables utilisées pour dessiner un gâteau de fête personnalisé.
bougies = "  "
espaces = ""
dessus = ""
dessous = ""
nbEspacesTotal = 0


# Une boucle est utilisée pour que le gâteau ait autant de bougies que l'âge entré.
# La variable "i" est temporairement utilisée comme compteur.
for i in range(0, age):
  bougies = bougies + "i  "
  espaces = espaces + "   "
  dessus = dessus + "---"
  dessous = dessous + "___"
  nbEspacesTotal = nbEspacesTotal + 3

# Vérification du nombre de lettres dans le nom en utlisant la fonction "len()".
# De plus, utilisation de l'opérateur modulo (%) pour déterminer si il s'agit d'un nombre pair ou impair.
# Si il y a un nombre impair de lettres, on ajoute un espace à la fin.
# Ceci va simplifier le centrage du nom sur le gâteau.
if (len(nom) % 2 != 0):
  nom = nom + " "


# Vérification du nombre d'espaces total pour déterminer si il est pair ou impair.
# Si il est impair, un espace d'ajustement sera ajouté sur la gauche du gâteau
if nbEspacesTotal % 2 != 0:
  espaceAjustement = " "
else:
  espaceAjustement = ""


# Calcul du nombre d'espaces requis avant et après le nom
# pour centrer le nom sur le gâteau.
nbEspacesNom = int((nbEspacesTotal - len(nom)) / 2)

# Une autre boucle est utilisée pour créer ces espaces.
espacesNom = ""
for i in range(0, nbEspacesNom):
  espacesNom = espacesNom + " "


# Affichage du gâteau de fête.
print("")
print("Voici donc à quoi ressemblait ton dernier gâteau de fête!")
print("")
print (bougies)
print ("-" + dessus + "-")
print ("|" + espaces + "|")
print ("|" + espaceAjustement + espacesNom + nom + espacesNom + "|")
print ("|" + espaces + "|")
print ("_" + dessous + "_")
print ("")
print ("")