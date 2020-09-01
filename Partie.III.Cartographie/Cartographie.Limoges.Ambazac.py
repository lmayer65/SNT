from pyroutelib3 import Router
import folium

""" Ce site trouve le chemin le plus court entre deux endroits """

# Site pour les coordonnées décimales  https://www.coordonnees-gps.fr/
# Moyen de transport : car foot cycle 
# https://pypi.org/project/pyroutelib3/
# Rester dans un département ! memoryflood sinon


router = Router("car")
depart = router.findNode(45.835424, 1.264485)        # Coordonnées de Limoges
arrivee = router.findNode(45.958226,1.401928)        # Coordonnées d'Ambazac
status, route = router.doRoute(depart, arrivee)

if status == "success":
    routeLatLons = list(map(router.nodeLatLon, route))

# Coordonnées de la ville de départ (ici Limoges)
c= folium.Map(location=[45.835424, 1.264485],zoom_start=10) 

# Le chemin à suivre est marqué par des petits cercles noirs
for coord in routeLatLons:
    coord=list(coord)
    folium.CircleMarker(coord,radius=1).add_to(c) 

c.save("Cartographie.MonItinéraire.html")
