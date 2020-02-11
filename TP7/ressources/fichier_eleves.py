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
