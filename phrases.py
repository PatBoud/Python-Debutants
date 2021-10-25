# Importation du module de hasard
import random

# Listes de mots
listeDObjets = ["une pomme", "un ordinateur", "un bonhomme Playmobil", "un chien", "une louche", "une buche", "des carottes", "une Barbie", "un iPhone 1000", "des épouvantails", "un divan", "une plante", "des chats", "un dinosaure", "un arbre"]
listeDePersonnes = ["Josée", "Louis-Phil", "Patrice", "Rachel", "Sylvie", "Dany", "Caro", "Flavie", "Annabelle", "Malorie", "Félix", "Charles", "Léo"]
listeDeVerbes = ["pettent", "lavent", "bouquinent", "mangent", "rottent", "lancent", "bousculent", "détruisent", "décoiffent", "chicanent", "plantent"]
listeDEndroits = ["à la crèmerie", "à la bibliothèque", "au restaurant", "chez le Diable", "dans un autre Univers", "chez Carey Price", "au sous-sol de Dracula", "sur le toit", "sur un poulet géant", "dans une baleine"]


# Boucle qui va créer 10 phrases
for i in range(0, 10):
  # Sélection de 2 personnes au hasard
  personne1 = random.choice(listeDePersonnes)
  personne2 = random.choice(listeDePersonnes)

  # On s'assure de sélectionner une 2ème personne différente
  # de la première
  while (personne1 == personne2):
    personne2 = random.choice(listeDePersonnes)

  # Sélection des autres morceaux de phrase
  objet = random.choice(listeDObjets)
  verbe = random.choice(listeDeVerbes)
  endroit = random.choice(listeDEndroits)

  laPhrase = personne1 + " et " + personne2 + " " + verbe + " " + objet + " " + endroit + "!"

  print (laPhrase)