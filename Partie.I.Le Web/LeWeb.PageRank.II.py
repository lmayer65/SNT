# Algorithme du PageRank permet de déterminer la popularité d'un site 
# quand un internaute clique de manière aléatoire sur un hyperlien une fois 
# sur l'un d'entre eux

from random import choice

# Répertorie les sites (ou pages) du graphe
nom = ["A","B","C","D"]

# nbVisites va stocker le nombre de visites par page, au départ c'est aucune
nbVisites = {"A" : 0 , "B" : 0 , "C" : 0 , "D" : 0 }

# Répertorie les hyperliens sortants de chaque site (à faire en fonction du graphe)
hyperliens = {"A":["A","B","D"] , "B":["C","D"] , "C":["A","D"] , "D":["C"]}


# Demande du nombre de tests souhaités converti en entier
# Ne pas dépasser 1 millions de tests
nbEtapes = int(input("Nombre de tests souhaités : "))

page = choice(nom)     # Site actuellement visité, valeur aléatoire au départ

for i in range(nbEtapes) :
    # Permet de sélectionner aléatoirement le futur site visité PARMI 
    # les hyperliens disponibles du site en question
    page = choice(hyperliens[page])
    
    # On incrémente le nombre de fois où le site ainsi visité
    nbVisites[page] = nbVisites[page] + 1
    

# Pourcentage de visite de chaque site et affichage des résultats   
for i in nom :
    nbVisites[i] = 100.0 * nbVisites[i] / nbEtapes  # Conversion implicite en float
    print(i , " = " , str(nbVisites[i]), " %") # Affichage des résultats
