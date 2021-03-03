## Exercice 1

def traitement_ligne(ligne, sep):
    """Prend une ligne, la découpe selon le caractère sep
    Supprimer le caractère de fin de ligne
    Convertit les champs d'index 0 et 1 en float"""
    ligne_sans_fin = ligne.rstrip()  #supprime la fin de ligne
    ligne_decoupe = ligne_sans_fin.split(sep)
    # masse = ligne_decoupe[0]
    # taille = ligne_decoupe[1]
    # espece = ligne_decoupe[2]
    masse, taille, espece = ligne_decoupe 
    return [ float(masse), float(taille), espece ]
    
    

def lecture(fichier):
    """Ouvre le fichier, Renvoie une liste de ses lignes"""
    f = open(fichier)
    #methode 1
    #lecture de tout le contenu => liste de toutes les lignes
    #methode2
    #liste_lignes = f.readlines()
    # liste_lignes = []
    # for ligne in f:
    #     liste_lignes.append(ligne)
    #methode 3
    f.readline()   # lecture de la ligne 1 => curseur positionné au début de la 2nde
    liste_lignes = [ traitement_ligne(ligne, '\t') for ligne in f ]
    liste_lauriers = []
    for ligne in f:
        masse, taille, espece = traitement_ligne(ligne, '\t') 
        if espece == "laurier rose":
            liste_lauriers.append(ligne)
    f.close()
    return liste_masse, liste_taille
    
    
def somme1(liste):
    s = 0
    for i in range(0, len(liste)):
        s = s + liste[i]
    return s

def somme(liste):
    s = 0
    for v in liste:
        s = s + v
    return s
    
def moyenne(liste):
    return somme(liste) / len(liste)

def copie_fichier_moyennes(source, sortie):
    liste_masse, liste_taille = lecture(source)
    f = open(sortie, 'w')
    g = open(source, 'r')
    contenu = g.read()
    f.write(contenu)
    g.close()
    m_masse = moyenne(liste_masse)
    m_taille = moyenne(liste_taille)
    f.write(str(m_masse) + '\t' + str(m_taille) + '\t' + 'Moyennes')
    f.close()


## Diagramme
import matplotlib.pyplot as plt
from math import log,ceil,sqrt
import numpy as np


def diagramme(fichier):
    masse,taille = lecture(fichier)
    #longueur de la série
    n = len(masse)
    plt.suptitle(fichier)
    plt.subplot(221)
    plt.title('Histogramme des masses')
    #nb de classes = sup(log(n,2)+1) calculé d'après la regle de Sturges
    nclasses = ceil(log(n,2)+1)
    plt.hist(masse,bins=nclasses)
    plt.subplot(222)
    plt.title('Diagramme en boite des masses')
    plt.boxplot(masse)
    plt.subplot(223)
    plt.title('Histogramme des tailles')
    plt.hist(taille,bins=nclasses)
    plt.subplot(224)
    plt.title('Diagramme en boite des tailles')
    plt.boxplot(taille)
    plt.savefig('Diagrammes-%s.png'%(fichier.rstrip('.txt')))
    plt.show()
    
## Regression

def bilan_regression(fichier):
    """La procédure récupère d'abord les listes dans fichier deux listes x et y de flottants de même longueur.
    La procédure calcule les listes x2,y2 et xy respectivement des carrés et des produits terme à terme des éléments de x et de y.
    Puis elle calcule la covariance  les variances  v(x) et v(y), la covariance cov(x,y), le coefficient de corrélation linéaire r(x,y), l'équation de la droite de régression de y en x.
    Elle recopie x,y,x2,y2 et xy en colonnes séparées par des virgules 
    Elle recopie les valeurs sum(x),sum(y),sum(x2),sum(y2),sum(xy) ligne par ligne dans  un fichier regression.txt.
    On complète ce fichier avec la moyenne en x, la moyenne en y, les écarts types en x et y, la cov(x,y), le coefficient de corrélation linéaire, et l'équation de la droite de régression.
    Puis elle affiche un graphique avec le nuage de points (x,y) et la droite de régression de y en x.
    """
    x,y = lecture(fichier)
    # utilisation de listes en compréhensions 
    n = len(x)
    #carrés de x
    x2 = [i**2 for i in x]
    #carrés de y
    y2 = [j**2 for j in y]
    #moyenne de x
    mx = sum(x)/n
    #moyenne de y
    my = sum(y)/n
    #variance de x
    vx = sum(x2)/n-(mx)**2
    #variance de y
    vy = sum(y2)/n-(my)**2
    #xy = [i*j for i,j in zip(x,y)]
    xy = [x[i]*y[i] for i in range(n)]
    #covariance de x et y
    covxy = sum(xy)/n-mx*my
    #coefficient de corrélation linéaire
    rxy = covxy/sqrt(vx*vy)
    #coefficient directeur a de la droite de régression de y en x
    a = covxy/vx
    #ordonnée à l'origie de la droite de régression de y en x
    b = my-a*mx
    # Ecriture dans le fichier regression.csv
    f = open('regression.txt','w')
    f.write('Totaux\n')
    f.write('sum(x) : {:.2f}, sum(y) : {:.2f}, sum(x^2) : {:.2f}, sum(y^2) : {:.2f}, sum(xy) :  {:.2f}\n'.format(sum(x),sum(y),sum(x2),sum(y2),sum(xy)))
    f.write('Moyennes\n')
    # Compléter avec ce qui est demandé
    
    
    
    #
    f.close()
    # Affichage du graphique
    t = np.linspace(min(x),5/4*max(x)-1/4*min(x),1000)
    #fonction affine de la droite de régression de y en x
    #g = lambda u:a*u+b
    #z = g(t)
    z = [a*t[i]+b for i in range(len(t))]
    plt.title('Equation de la droite de régression linéaire : y={:.2f}x+{:.2f}\nCoefficient de corrélation linéaire : {:.2f}'.format(a,b,rxy))
    plt.plot(x,y,'r+',markeredgewidth=2)
    plt.plot(t,z,'b-')
    plt.savefig('regression.png')
    plt.show()
