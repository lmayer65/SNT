#source : http://ressources.unisciel.fr/sillages/informatique/dijkstra/co/Dijkstra_5.html


adjacenceMatrice = [[0 ,4 ,1 ,0 ,3 ,0 ],
                    [4 ,0 ,10,1 ,0 ,0 ],
                    [1 ,10,0 ,5 ,1 ,0 ],
                    [0 ,1 ,5 ,0 ,3 ,1 ],
                    [3 ,0 ,1 ,3 ,0 ,1 ],
                    [0 ,0 ,0 ,1 ,1 ,0 ]]


def algorithmDijkstra(am,s,a) :
    
    # En additionnant toutes les valeurs + 1 , on est sûr que tous les autres
    # chemins seront plus courts
    infini = sum(sum(ligne) for ligne in am) + 1
    nb_sommets = len(am)
    
    s_connu = {s : [0,[s]]}
    s_inconnu = {k : [infini,''] for k in range(nb_sommets) if k!= s}
    
    for suivant in range(nb_sommets) :
        if am[s][suivant] :
            s_inconnu[suivant] = [am[s][suivant],s]
            
    print('Dans le graphe d\'origine {} de matrice d\'adjacence : '.format(s))
    for ligne in am:
        print(ligne)
        
    print()
    print('Plus court chemin de ',s,' à ',a)
    
    while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu) :
        u = min(s_inconnu, key = s_inconnu.get)
        longueur_u, precedent_u = s_inconnu[u]
        
        for v in range(nb_sommets) :
            if am[u][v] and v in s_inconnu :
                d = longueur_u + am[u][v]
                if d < s_inconnu[v][0] :
                    s_inconnu[v] = [d,u]
                    
        s_connu[u] = [longueur_u, s_connu[precedent_u][1] + [u] ] 
        
        del s_inconnu[u]
        print('longueur',longueur_u,':',' -> '.join(map(str,s_connu[u][1]))) 
        
        # Si on est arrivé à destination
        if u == a :
            break

        
    return s_connu

# On passe le sommet de départ puis le sommet d'arrivée
algorithmDijkstra(adjacenceMatrice,0,5)


