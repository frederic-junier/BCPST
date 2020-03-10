from PIL import Image
import numpy as np

## Exemple du cours

def miroir(fichier):
    """prend en entrée un fichier image et retourne l'image de l'image
     obtenue par une réflexion par rapport à l'axe vertical droit
    """
    im=Image.open(fichier)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res = np.zeros_like(pixels)
    for j in range(largeur):
        for i in range(hauteur):
            pixels_res[i, j,:] = pixels[i, largeur - 1 -  j,:]
    img_res = Image.fromarray(pixels_res)
    img_res.save("miroir"+fichier)
    img_res.show()
    
## Exercice 10.1

def gris(imsource, coeff):
    """ coeff est une liste composée de 3 éléments """
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res = np.zeros([hauteur,largeur],dtype="uint8")
    # à compléter
    
    img_res = Image.fromarray(pixels_res)
    img_res.save("gris_"+imsource)
    img_res.show()
    
## Exercice 10.2

def negatif(imsource):
    """prend en entrée un fichier image et retourne son négatif
    """
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res = np.zeros_like(pixels)
    # à compléter
    
    img_res = Image.fromarray(pixels_res)
    img_res.save("negatif_"+imsource)
    img_res.show()
    
## Exercice 10.3

def monochrome(imsource):
    """prend en entrée un fichier image et retourne une version monochome pour chacune des couleurs
    """
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res_rouge = np.zeros_like(pixels)
    pixels_res_vert = np.zeros_like(pixels)
    pixels_res_bleu = np.zeros_like(pixels)
    # à compléter
    
## Exercice 10.4




## Exercice 10.5

def luminosite1(imsource,unite):
    im=Image.open(imsource)
    pixels = np.array(im)
    pixels = pixels.astype(int)
    # à compléter
    
    
    pixels_res=pixels_res.astype(np.uint8)
    img_res = Image.fromarray(pixels_res)
    img_res.save("lum1_"+imsource)
    img_res.show()
    
## Exercice 10.6

# Liste des fonctions

def filtre_puissance(x,p):
    return int(255*(x/255)**p)
    
def f(x):
    return 3*x**2-2*x**3
    
def g(x):
    return (x**3)*(6*x**2 -15*x + 10)
 
# Fonction lum_contraste
    
def lum_contraste(imsource,fonction,parametre):
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res = np.zeros_like(pixels)
    if len(pixels.shape)==3:
        # à compléter
        
        
    else:
        # à compléter
        
        
    img_res = Image.fromarray(pixels_res)
    img_res.save("lum_cont"+imsource)
    img_res.show()
    
## Exercice 10.7

# Matrices filtre

def flou(k):
    return np.ones((2*k+1,2*k+1),dtype="uint8")

flou_bis = np.array([[1, 2, 1],
                 [2, 4, 2],
                 [1, 2, 1]])
                 
A = np.array([[-1, -2, -1],
                    [-2, 16, -2],
                    [-1, -2, -1]])
     
B = np.array([[0, 1, 0],
     [1, 1, 1],
     [0, 1, 0]])
     
accentue = np.array([[-1,1,-1,1,-1],
     [1,-1, -2, -1,1],
     [-1,-2, 16, -2,-1],
     [1,-1, -2, -1,1],
     [-1,1,-1,1,-1]])

# Filtre de repoussage (emboss)
C = np.array([[2, 1, 0],
     [1, 1, -1],
     [0, -1, -2]])
     
D = np.array([[-2, -1, 0],
     [-1, 1, 1],
     [0, 1, 2]])

# Détection de bords
E = np.array([[-1/9, -1/9, -1/9],
     [-1/9, 8/9, -1/9],
     [-1/9, -1/9, -1/9]])
     
F = np.array([[0, -1, 0],
     [-1, 4, -1],
     [0, -1, 0]])
    
G = np.array([[1, 0, -1],
     [1, 0, -1],
     [1, 0, -1]])
     
H = np.array([[-1, -2, -1],
     [0, 0, 0],
     [1, 2, 1]])

# Moyenne bloc

def moyenne_bloc(pixels, i, j, matrice):
    rayonbloc=len(matrice)//2
    if np.sum(matrice)==0:
        # à compléter
    else:
        # à compléter
    if len(pixels.shape)==3:
        pixel=[0,0,0]
        # à compléter
        
        
        
    return pixel
    

def applique_filtre(imsource, matrice):
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res = np.zeros_like(pixels)
    rayonbloc=len(matrice)//2
    # à compléter
    
    
    img_res = Image.fromarray(pixels_res)
    img_res.save("filtre"+imsource)
    img_res.show()
    
## Exercice 10.8

def pixelisation(imsource,taillebloc):
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels = pixels.astype(int)
    pixels_res = np.zeros_like(pixels)
    for i in range(0,hauteur-taillebloc+1,taillebloc):
        # à compléter
        
        
        
    pixels_res=pixels_res.astype(np.uint8)
    img_res = Image.fromarray(pixels_res)
    img_res.save("pixel_"+imsource)
    img_res.show()
    
## Exercice 10.9




## Exercice 10.10

def contour(imsource,s):
    im=Image.open(imsource)
    pixels = np.array(im)
    pixels = pixels.astype(float)
    if len(pixels.shape)==3:
        print("convertir en niveau de gris")
    else:
        hauteur, largeur =pixels.shape
        pixels_res = np.zeros_like(pixels)
        # à compléter
        
    pixels_res=pixels_res.astype(np.uint8)
    img_res = Image.fromarray(pixels_res)
    img_res.save("contour_"+imsource)
    img_res.show()
    

## Exercice 10.11

def quart_tour_direct(imsource):
    """prend en entrée un fichier image et retourne l'image de l'image 
    obtenue par un quart de tour direct de centre le coin supérieur 
    gauche de l'image source"""
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res = np.zeros((largeur,hauteur,3),dtype='uint8')
    # à compléter
    
    
    img_res = Image.fromarray(pixels_res)
    img_res.save("quart_"+imsource)
    img_res.show()
    
## Exercice 10.12



## Exercice 10.13


