#!/usr/bin/env python
# coding: utf-8

# In[8]:


from PIL import Image    # Importe la bibliothÃ¨que gÃ©rant les images
import matplotlib.pyplot as plt   # Importe la bibliothÃ¨que permettant ici d'afficher les images


         
# Affiche l'image de base et celle transformÃ©e
def showImages(img1,img2) :
    # Permet de créer une sous_fenÃªtre, le 3eme arg est la place de l'image
    plt.subplot(1,2,1)
    plt.title("Image de base")
    plt.imshow(img1,cmap ='gray')
    plt.subplot(1,2,2)
    plt.title("Image modifiée")
    plt.imshow(img2,cmap ='gray')

    

# Chargement de l'image à partir du répertoire de Jupyter
# BIEN MONTER L'IMAGE DANS LE REPERTOIRE #
imgBase = Image.open("perceval.jpg") # Lien vers l'image 
width,height = imgBase.size          # Détermine la largeur et hauteur de l'image en pixels

imgNew = Image.new("RGB",(width,height))    # Création d'une image RGB vierge pour recueillir
                                            # les modifications apportées

for i in range(width):          # Double boucle permettant de parcourir 
    for j in range(height):     # chaque pixel de l'image
        
        red,green,blue = imgBase.getpixel((i,j))   # Récupère le code RVB du pixel
        
        #######################################################################
        ############### Transformation de l'image ici  ########################
        #######################################################################
        
        
        ########################################################################    
        
        imgNew.putpixel((i,j),(red,green,blue))  # Modification du pixel en question

# Affiche les deux images
showImages(imgBase,imgNew)


# In[ ]:




