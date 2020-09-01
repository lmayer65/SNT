# Simulation d'une autorisation d'acès à un réseau social en fonction
# d'un identifiant et d'un mot de passe

DataBase ={"Fred":"theone","Elisa":"puppet"}

pseudo = input("entrer le pseudo  : ")
passWord = input("Entrer le mot de passe : ")

# Vérifie si le duo identifiant / mot de passe est bien dans le dictionnaire.
if DataBase.get(pseudo) == passWord :
    print("Accès autorisé")
else:
    print("Accès refusé")
    