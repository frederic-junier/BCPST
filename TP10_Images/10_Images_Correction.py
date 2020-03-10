from PIL import Image
import numpy as np

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
            ##pixels_res[i, j] = pixels[i, largeur - 1 -  j]   #Proposoition Frederic 
    img_res = Image.fromarray(pixels_res)
    img_res.save("miroir"+fichier)
    img_res.show()

# Version 2 : slicing   
def miroir(fichier):
    """prend en entrée un fichier image et retourne l'image de l'image
     obtenue par une réflexion par rapport à l'axe vertical droit
    """
    im=Image.open(fichier)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res = np.zeros_like(pixels)
    for j in range(largeur):
        pixels_res[:,j,:] = pixels[:, largeur - 1 -  j,:]
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
    #pixels_res = np.zeros_like(pixels) #Proposition Frederic 
    for j in range(largeur):
        for i in range(hauteur):
            pixels_res[i, j] = int(np.sum(pixels[i,j,:]*coeff)/np.sum(coeff))
    img_res = Image.fromarray(pixels_res)
    img_res.save("gris_"+imsource)
    img_res.show()
     
def gris2(imsource, coeff):  #Proposition Frederic 
    """ coeff est une liste composée de 3 éléments """
    im = Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur = pixels.shape[:2]
    somme_coef = np.sum(coeff)
    for j in range(largeur):
        for i in range(hauteur):
            pixels[i, j] = int(np.sum(pixels[i,j,:] * coeff)/somme_coef)
    img_res = Image.fromarray(pixels)
    img_res.save("gris"+imsource)
    img_res.show() 
    
## Exercice 10.2

def negatif(imsource):
    """prend en entrée un fichier image et retourne son négatif
    """
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res = np.zeros_like(pixels)
    pixels_res = 255-pixels
    img_res = Image.fromarray(pixels_res)
    img_res.save("negatif_"+imsource)
    img_res.show()

def negatif2(imsource):#Proposition Frederic
    """ Retourne le négatif d'une image """
    im = Image.open(imsource)
    pixels = np.array(im)
    img_res = Image.fromarray(255 - pixels)
    img_res.save("negatif"+imsource)
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
    for i in range(hauteur):
        for j in range(largeur):
            [r, g, b] = pixels[i,j,:]
            pixels_res_rouge[i, j] = [r, 0, 0]
            pixels_res_vert[i, j] = [0, g, 0]
            pixels_res_bleu[i, j] = [0, 0, b]
    img_res_r = Image.fromarray(pixels_res_rouge)
    img_res_r.save("rouge_"+imsource)
    img_res_r.show()
    img_res_v = Image.fromarray(pixels_res_vert)
    img_res_v.save("vert_"+imsource)
    img_res_v.show()
    img_res_b = Image.fromarray(pixels_res_bleu)
    img_res_b.save("bleu_"+imsource)
    img_res_b.show()  


# version 2 : slicing    
def monochrome(imsource):
    """prend en entrée un fichier image et retourne une version monochome pour chacune des couleurs
    """
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res_rouge = np.zeros_like(pixels)
    pixels_res_vert = np.zeros_like(pixels)
    pixels_res_bleu = np.zeros_like(pixels)
    # Rouge
    pixels_res_rouge[:,:,0] = pixels[:,:,0]
    img_res_r = Image.fromarray(pixels_res_rouge)
    img_res_r.save("rouge_"+imsource)
    img_res_r.show()
    # Vert
    pixels_res_vert[:,:,1] = pixels[:,:,1]
    img_res_v = Image.fromarray(pixels_res_vert)
    img_res_v.save("vert_"+imsource)
    img_res_v.show()
    # Bleu
    pixels_res_bleu[:,:,2] = pixels[:,:,2]
    img_res_b = Image.fromarray(pixels_res_bleu)
    img_res_b.save("bleu_"+imsource)
    img_res_b.show()
    
## Exercice 10.4  

def maxmin(x):
    return int(max(0,min(x,255)))
    
def maxminmat(matrice):
    taille=matrice.shape
    res=np.zeros_like(matrice)
    if len(taille)==3:
        for i in range(taille[0]):
            for j in range(taille[1]):
                for k in range(taille[2]):
                    res[i,j,k]=maxmin(matrice[i,j,k])
    else:
        for i in range(taille[0]):   #<= typo corrigée
            for j in range(taille[1]): #<= typo corrigée
                res[i,j]=maxmin(matrice[i,j])
    return res
    

## Exercice 10.5

def luminosite1(imsource,unite):
    im=Image.open(imsource)
    pixels = np.array(im)
    pixels = pixels.astype(int)
    
    pixels_res= maxminmat(pixels+unite)
    
    pixels_res=pixels_res.astype(np.uint8)
    img_res = Image.fromarray(pixels_res)
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

def filtre_f(x,p):
    return int(255*f(x/255))

def filtre_g(x,p):
    return int(255*g(x/255))

# Fonction lum_contraste

def lum_contraste(imsource,fonction,parametre):
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res = np.zeros_like(pixels)
    if len(pixels.shape)==3:
        for i in range(hauteur):
            for j in range(largeur):
                for k in range(3):
                    pixels_res[i,j,k] = maxmin(fonction(pixels[i,j,k],parametre))
    else:
        for i in range(hauteur):
            for j in range(largeur):
                pixels_res[i,j] = maxmin(fonction(pixels[i,j],parametre))
    img_res = Image.fromarray(pixels_res)
    img_res.save("lum_cont"+imsource)
    img_res.show()
    
def lum_contraste2(imsource,fonction): #Proposition Frederic
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur = pixels.shape[:2]
    if len(pixels.shape) == 3:
        for i in range(hauteur):
            for j in range(largeur):
                for k in range(3):
                    pixels[i,j,k] = maxmin(fonction(pixels[i,j,k]))
    else:
        for i in range(hauteur):
            for j in range(largeur):
                pixels[i,j] = maxmin(fonction(pixels[i,j]))
    img_res = Image.fromarray(pixels)
    img_res.save("lum_cont" + fonction.__name__ + imsource)
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
        som_matrice=1
    else:
        som_matrice=np.sum(matrice)
    if len(pixels.shape)==3:
        pixel=[0,0,0]
        for k in range(3):
            pixel[k]=maxmin(np.sum(pixels[i-rayonbloc:i+rayonbloc+1, j-rayonbloc:j+rayonbloc+1,k]*matrice)//som_matrice)
    else :
        pixel=maxmin(np.sum(pixels[i-rayonbloc:i+rayonbloc+1, j-rayonbloc:j+rayonbloc+1]*matrice)//som_matrice)
    return pixel
    

def applique_filtre(imsource, matrice):
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res = np.zeros_like(pixels)
    rayonbloc=len(matrice)//2
    for i in range(rayonbloc,hauteur-rayonbloc):
        for j in range(rayonbloc,largeur-rayonbloc):
            pixels_res[i,j]=moyenne_bloc(pixels,i,j,matrice)
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
        for j in range(0,largeur-taillebloc+1,taillebloc):
            for k in range(3):
                couleur = np.mean(pixels[i:i+taillebloc,j:j+taillebloc,k])
                for x in range(taillebloc):
                    for y in range(taillebloc):
                        pixels_res[i+x,j+y,k] = couleur
    pixels_res=pixels_res.astype(np.uint8)
    img_res = Image.fromarray(pixels_res)
    img_res.save("pixel_"+imsource)
    img_res.show()
    

## Exercice 10.9

def test_seuil(x,s):
    if x <= s:
        return 0
    return 255
        

def seuil(imsource,s):
    im=Image.open(imsource)
    pixels = np.array(im)
    if len(pixels.shape)==3:
        print("convertir en niveau de gris")
    else:
        hauteur, largeur =pixels.shape
        pixels_res = np.zeros_like(pixels)
        for i in range(hauteur):
            for j in range(largeur):
                pixels_res[i,j]=test_seuil(pixels[i,j],s)
    img_res = Image.fromarray(pixels_res)
    img_res.save("seuil_"+imsource)
    img_res.show()       

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
        for i in range(1,hauteur-1):
            for j in range(1,largeur-1):
                pb = pixels[i+1, j] # pixel en bas
                pt = pixels[i-1, j] # pixel en haut
                pr = pixels[i, j+1] # pixel de droite
                pl = pixels[i, j-1] # pixel de gauche
                if ((pb-pt)**2+(pr-pl)**2)**(1/2) > s :
                    pixels_res[i, j] = 0
                else:
                    pixels_res[i, j] = 255
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
    for i in range(largeur):
        for j in range(hauteur):
            for k in range(3):
                pixels_res[i,j,k] = pixels[j,hauteur-1-i,k]
    img_res = Image.fromarray(pixels_res)
    img_res.save("quart_"+imsource)
    img_res.show()
    
## Exercice 10.12

def reduction(imsource, coef):
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    hfinal, lfinal=hauteur//coef,largeur//coef
    pixels_res = np.zeros((hfinal, lfinal,3),dtype='uint8')
    for i in range(hfinal):
        for j in range(lfinal):
            pixels_res[i, j] = pixels[i * coef, j * coef]
    img_res = Image.fromarray(pixels_res)
    img_res.save("reduc_"+imsource)
    img_res.show()
    
## Exercice 10.13


# Décrypte
def decode(v):
    return (v%(2**4))*2**4
    
def decrypte(imsource):
    im=Image.open(imsource)
    pixels = np.array(im)
    hauteur, largeur =pixels.shape[:2]
    pixels_res = np.zeros_like(pixels)
    for i in range(hauteur):
        for j in range(largeur):
            pixels_res[i,j]=decode(pixels[i,j])
    img_res = Image.fromarray(pixels_res)
    img_res.save("decrypte_"+imsource)
    img_res.show()
    
# Crypte
def code(v1,v2):
    return (v1 // 2**4)*2**4+v2//2**4
    
def cache(anodin, secret):
    im1=Image.open(anodin)
    pixelsanodin = np.array(im1)
    im2=Image.open(secret)
    pixelsecret = np.array(im2)
    hauteur, largeur =pixelsanodin.shape[:2]
    pixels_res = np.zeros_like(pixelsanodin)
    for i in range(hauteur):
        for y in range(largeur):
            pixel_res[i,j]=code(pixelsanodin[i,j],pixelsecret[i,j])
    img_res = Image.fromarray(pixels_res)
    img_res.save("mystery.png")
    img_res.show()
    
