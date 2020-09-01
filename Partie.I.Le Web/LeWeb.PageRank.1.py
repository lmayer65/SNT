# Algorithme du PageRank permet de déterminer la popularité d'un site 
# quand un internaute clique de manière aléatoire sur un hyperlien une fois 
# sur l'un d'entre eux

from random import choice
from random import randint

# Répertorie les sites enregistrés par le moteur de recherche
nom = ["A","B","C","D"]

# Taille de la liste nom
szNom = len(nom)

# Répertorie les hyperliens sortants de chaque site (à faire en fonction du graphe)
# 0 correspond au site "A", 1 correspond au site B etc.
hyperliens = [[0,1,3],[2,3],[0,3],[2]]

# Demande du nombre de tests souhaités converti en entier
# Ne pas dépasser 1 millions de tests
nbEtapes = int(input("Nombre de tests souhaités : "))

# Déclaration et initialisation de variables
nbVisites = []              # Nombre de fois où chaque site est visité
for i in range(0,szNom) :
    nbVisites.append(0)     # Crée le tableau souhaité en fonction du nombre de sites
    
page = randint(0,szNom)     # Site actuellement visité, valeur aléatoire au départ

for i in range(nbEtapes) :
    # Permet de sélectionner aléatoirement le futur site visité PARMI 
    # les hyperliens disponibles du site en question
    page = choice(hyperliens[page])
    
    # On incrémente le nombre de fois où le site ainsi visité
    nbVisites[page] = nbVisites[page] + 1
    

# Pourcentage de visite de chaque site et affichage des résultats   
for i in range(0,szNom) :
    nbVisites[i] = 100.0 * nbVisites[i] / nbEtapes  # Conversion implicite en float
    print(nom[i] + " = " + str(nbVisites[i]) + " %") # Affichage des résultats

    