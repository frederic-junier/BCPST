
# coding: utf-8

# # Tests (Instructions conditionnelles) 

# ## Exercice 3.1 IMC

# In[10]:


taille = float(input("Entrez votre taille en mètres : "))
print("Pour une taille de {} mètres, la masse pour un IMC normal doit être" 
      "comprise entre {:.2f} et {:.2f} ".format(taille, 18.5*taille**2, 25*taille**2))


# In[13]:


from math import sqrt
masse = float(input("Entrez votre masse en kilos : "))
print("Pour une masse de {} kilos, la taille pour un IMC normal doit être "
      "comprise entre {:.2f} et {:.2f} ".format(masse, sqrt(masse/25), sqrt(masse/18.5)))


# In[14]:


taille = float(input("Entrez votre taille en mètres : "))
masse = float(input("Entrez votre masse en kilos : "))
imc = masse/taille**2
if 18.5 <= imc <= 25:
    print("IMC normal")
elif imc < 18.5:
    print("IMC anormal : sous-poids")
else:
    print("IMC anormal : surpoids")


# ## Exercice bonus Suite croissante, algorithme de tri sur une instance de trois nombres

#     Version par énumération des 3*2*1 = 6 arrangements

# In[ ]:


a = float(input('Entrez un réel a : '))
b = float(input('Entrez un réel b : '))
c = float(input('Entrez un réel c : ')) 
if a <= c <= b:
    c, b = b,c 
elif b <= a <= c:
    a, b = b, a
elif b <= c <= a:
    a, b, c = b, c , a
elif c <= a <= b:
    a, b, c = c, a, b
elif c <= b <= a:
    a, c = c, a    


# Version tri par sélection

# In[16]:


a = float(input('Entrez un réel a : '))
b = float(input('Entrez un réel b : '))
c = float(input('Entrez un réel c : ')) 
#on met dans a le minimum de a et b
if a > b:
   a, b = b, a
#on met dans a le minimum de a et c
if a > c:
   a, c = c, a
#desormais a contient le minimum de a, b et c
#on met dans b le minimum de b et c
if b > c:
   b, c = c, b


# In[17]:


a, b, c


# Version tri par insertion

# In[ ]:


a = float(input('Entrez un réel a : '))
b = float(input('Entrez un réel b : '))
c = float(input('Entrez un réel c : '))
#on prend le deuxième élément (b) et on l'insère dans la liste
#déjà triée (a tout seul)
if a > b:
   a, b = b, a
#on recommence avec c en l'insérant dans la liste a, b déjà triée
if a < c < b:
   b, c= c, b
elif c < a < b:
   a, b, c = c, a, b
print(a, b, c,sep='<=')


# ## Exercice 3.3 Une première fonction

# In[2]:


def mystere(x):
    """Aide sur la fonction mystere"""
    if x>15:
        print('super')
    print('peut mieux faire')


# In[3]:


help(mystere)


# In[20]:


mystere(14)


# In[21]:


mystere(16)


# IL s'agit de remarquer ici que vu  l'identation (le décallage) le commande `print('peut mieux faire')` est exécutée, peu importe que le test ait renvoyé True ou False.

# In[1]:


def mystere2(x):
    """Aide sur la fonction mystere"""
    if x>15:
        print('super')
    else:
        print('peut mieux faire')
    return None


# In[2]:


mystere2(18)


# In[3]:


message = mystere2(18)


# In[5]:


print(message)


# In[6]:


def mystere3(x):
    """Aide sur la fonction mystere"""
    if x>15:
        return('super')
    else:
        return('peut mieux faire')


# In[7]:


mystere3(18)


# In[8]:


message = mystere3(18)


# In[9]:


message


# In[10]:


def mystere4(x):
    """Aide sur la fonction mystere"""
    if x>15:
        return('super')
    return('peut mieux faire')


# In[10]:


def carre(x):    
    return x**2


# In[11]:


carre(3)


# In[12]:


a = carre(3)


# In[13]:


print(a)


# ## Exercice 3.4 Echange conditionnel de valeurs

# In[23]:


a = float(input('Entrez un premier réel a : '))
b = float(input('Entrez un second  réel b : '))
if a > b:
    a, b = b, a
print('a = ', a,' b = ', b)


# ## Exercice 3.5 Maximum et suites monotones

# In[1]:


def max2(a,b):
    """retourne le maximum de deux entiers a et b"""
    if b > a:
        return b
    return a

def max3V0(a, b, c):
    if b >= a and b >= c:
        return b       
    elif c >= a and c >= b:
        return c
    return a  

def max3V1(a, b, c):
    if b > a:
        a, b = b, a
    if c > a:
        a, c = c, a
    return a    

def max3V2(a, b, c):
    a = max2(a, b)
    a = max2(a, c)
    return a 

def max3V3(a, b, c):
    a = max2(a, b)
    return max2(a, c)
            
def max3(a,b,c):
    """retourne le maximum de trois entiers a et b"""
    return max2(max2(a, b), c)

def monotone(x,y,z):
    """retourne True si x<=y<=z ou z<=y<=x et False sinon"""
    return x <= y <= z or z <= y<= x

def monotone2(x,y,z):
    """retourne True si x<=y<=z ou z<=y<=x et False sinon"""
    if x <= y <= z or z <= y<= x:
        return True
    return False


# In[12]:


help(max2)


# In[13]:


max2.__doc__


# In[14]:


max2.__name__


# # Boucles

# ## Exercice 3.6

# In[25]:


def mystere(n):
    u = 0
    for i in range(1, n + 1):
        u = 3*u + 2
    return u


# Cette fonction retourne le terme de rang $n$ de la suite arithmético-géométrique définie par $\begin{cases} u_{0} = 0 \\ u_{n+1}=3u_{n}+2 \end{cases}$.

# ## Exercice 3.7

# Soit $n \in \mathbb{N}^*$. On considère les deux sommes suivantes :
# $$S_n=\sum_{k=1}^n \dfrac{1}{k^2}\qquad\qquad I_n=\sum_{k=1}^n \dfrac{1}{(2k+1)^2}$$
# Pour tout $n \in \mathbb{N}^*$ on a $S_{n+1}=S_{n}+\frac{1}{(n+1)^{2}}$   et    $I_{n+1}=I_{n}+\dfrac{1}{(2n+3)^2}$.
# 
# Pour tout $n \geqslant 2$ on a $S_{n}=S_{n-1}+\frac{1}{n^{2}}$   et    $I_{n}=I_{n-1}+\dfrac{1}{(2n+1)^2}$.

# In[27]:


def S(n):
    somme = 1
    for k in range(2, n + 1):
        somme += 1/k**2
    return somme

def I(n):
    somme = 1/9
    for k in range(2, n + 1):
        somme += 1/(2*k + 1)**2
    return somme


# In[28]:


S(100)


# In[29]:


I(100)


# ## Exercice 3.8

# In[15]:


# Question 1
def puissance(x,n):
    """retourne x**n sans l'opérateur **"""
    p = 1
    for i in range(n):
        p *= x
    return p

def puissancen(n):
    """retourne la fonction x -> x**n"""
    return lambda x : puissance(x, n)
    
# Question 2
def factorielle(n):
    """retourne 1x2x3x...x(n-1)xn"""
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

def factoriellerec(n):
    """Factorielle récursive"""
    if n == 0:
        return 1
    return n*factoriellerec(n - 1)

def puissancerec(a, n):
    if n == 0:
        return 1
    return a*puissancerec(a, n - 1)


# In[32]:


puissance(5, 20)


# In[36]:


factorielle(10)


# In[38]:


factoriellerec(10)


# In[33]:


puissancen(5)


# In[35]:


f = puissancen(2)
for k in range(10):
    print(f(k), end='-')


# # Boucle while

# ## Exercice 3.9

# In[4]:


secret = "0000"
essai = 1
while essai <= 3 and input("Entrez votre code secret : ") != secret:
    print("Code faux")
    essai += 1
if essai == 4:
    print("Carte inutilisable.")
else:
    print("Code bon.")


# Attention à bien placer le test sur le nombre d'essai avant le test du code saisi sinon un essai supplementaire est possible.
# 
# Le `and` est _paresseux_, si son premier opérande est faux, les opérandes suivants ne sont pas évalués.

# In[ ]:


secret = "0000"
for essai in range(3):
    if input("Entrez votre code secret : ") == secret:
        print("Code bon.")
        break
    print("Code faux")
else:
    print("Carte inutilisable.")


# Dans la version ci-dessus on utilise une boucle `for` avec un `break` pour sortir de la boucle si le code correct est saisi et un `else` après le bloc du `for` qui n'est exécuté que s'il n'y a pas eu de sortie de boucle par un  `break` (donc ssi aucun code correct n'a été saisi en 3 essais).

# ## Exercice 3.10

# La suite définie par $S_n=\displaystyle \sum_{k=1}^n \frac{1}{k}$ est croissante et a pour limite $+\infty$.
# 
# Pour tout entier $n \geqslant 1$, $S_{n+1}=S_{n}+\frac{1}{n+1}$

# In[5]:


def seuilharmonique(M):
    """Retourne le + petit entier n tel que sum(k, 1, n, 1/k) >= M"""
    s, k = 1., 1
    while s < M:
        k += 1
        s += 1./k
    return k  


# # Boucles imbriquées

# ## Exercice 3.11

# In[7]:


def imbriquee(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
        print("*")
    print("*")


# In[8]:


imbriquee(2)


# ## Exercice 3.12

# $\displaystyle\sum_{i = 1}^{n}\sum_{j=1}^{n} ij$

# In[11]:


def rectangle(n):
    s = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            s += i*j
    return s


# In[12]:


rectangle(100)


# $\displaystyle\sum_{i = 1}^{n - 1}\sum_{j=i + 1}^{n} i + j$

# In[1]:


def triangle(n):
    s = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            s += i + j
    return s


# In[2]:


triangle(100)


# $\displaystyle\sum_{j = 2}^{n}\sum_{i=1}^{j-1} i + j$

# In[3]:


def triangle2(n):
    s = 0
    for j in range(2, n + 1):
        for i in range(1, j):
            s += i + j
    return s


# In[4]:


triangle2(100)


# # D'autres exercices 

# ## Exercice 3.13 Somme des carrés

# In[19]:


def sommecarrefor(n):
    s = 0
    for k in range(1, n + 1):
        s += k**2
    return s


# In[20]:


def sommecarrewhile(n):
    s = 0
    k = 0
    while k < n:
        k += 1
        s += k**2
    return s


# In[21]:


[sommecarrefor(n) for n in range(0, 10)]


# In[22]:


[sommecarrewhile(n) for n in range(0, 10)]


# In[41]:


def sommecarre_int(n):
    """Somme des carrés avec typage int"""
    return n*(n + 1)*(2*n + 1)//6


# In[29]:


[sommecarre_int(n) for n in range(0, 10)]


# In[40]:


def sommecarre_float(n):
    """Somme des carrés avec typage float"""
    return n*(n + 1)*(2*n + 1)/6


# Les deux fonctions ci-dessus utilisant la formule explicite $\displaystyle \sum_{k=1}^{n}\frac{1}{k^{2}}=\frac{n(n+1)(2n+1)}{6}$ diffèrent à partir de $10^{6}$ car la première retourne un entier (valeur exacte) et l'autre un flottant (représentation approchée d'un flottant).

# In[39]:


[sommecarre_float(10**n) == sommecarre_int(10**n) for n in range(0, 20)]


# ## Exercice 3.14

# In[ ]:


def approx_expoV0(x,n):
    """retourne 1+x+x^2/2!+....+x^n/n!"""
    somme,terme, puissance, factorielle = 1,1,1,1
    for i in range(1,n+1):
        puissance = puissance * x
        factorielle = factorielle * i
        terme = puissance/factorielle
        somme += terme
    return round(somme,3) #on peut régler la précision de l'arrondi


# In[42]:


def approx_expo(x,n):
    """retourne 1+x+x^2/2!+....+x^n/n!"""
    somme,terme = 1,1
    for i in range(1,n+1):
        terme = terme*x/i
        somme += terme
    return round(somme,3) #on peut régler la précision de l'arrondi


# In[43]:


approx_expo(4, 17)


# ## Exercice 3.15

# In[3]:


from random import randint

def devinette(n):
    cible = randint(1, n)
    ## choisit la cible au hasard entre 1 et n
    reponse = int(input("Votre essai ? "))
    ## affiche "Votre essai ?", attend que l'utilisateur rentre une
    ## valeur validée par entrée et convertit cette valeur en entier.
    if reponse == cible:
        print("Gagné !")
    else:
        print("Perdu !")
        print("La réponse était", cible)


# In[ ]:


def devinette_while(n):
    cible = randint(1, n)
    ## choisit la cible au hasard entre 1 et n
    reponse = int(input("Votre essai ? "))
    ## affiche "Votre essai ?", attend que l'utilisateur rentre une
    ## valeur validée par entrée et convertit cette valeur en entier.
    while reponse != cible:
        if reponse < cible:
            print("Plus grand!")
        else:
            print("Plus petit")
        reponse = int(input("Votre essai ? "))
    print("Gagné !")


# In[7]:


def devinette_while2(n):
    cible = randint(1, n)
    nbessai = 1
    ## choisit la cible au hasaard entre 1 et n
    reponse = int(input("Votre essai ? "))
    ## affiche "Votre essai ?", attend que l'utilisateur rentre une
    ## valeur validée par entrée et convertit cette valeur en entier.
    while reponse != cible:
        if reponse < cible:
            print("Plus grand!")
        else:
            print("Plus petit")
        nbessai += 1
        reponse = int(input("Votre essai ? "))
    print("Gagné en {} essais!".format(nbessai))


# In[8]:


def devinette_while3(n):
    cible = randint(1, n)
    nbessai = 1
    ## choisit la cible au hasaard entre 1 et n
    reponse = int(input("Votre essai ? "))
    ## affiche "Votre essai ?", attend que l'utilisateur rentre une
    ## valeur validée par entrée et convertit cette valeur en entier.
    while reponse != cible:
        if reponse < cible:
            print("Plus grand!")
        elif reponse > cible:
            print("Plus petit")
        nbessai += 1
        reponse = int(input("Votre essai ? "))
    print("Gagné en {} essais!".format(nbessai))


# In[4]:


def devinette_while4(n):
    cible = randint(1, n)
    nbessai = 1
    ## choisit la cible au hasaard entre 1 et n
    essaimax = int(input("Nombre maximum d'essais ? "))    
    ## affiche "Votre essai ?", attend que l'utilisateur rentre une
    ## valeur validée par entrée et convertit cette valeur en entier.
    trouve = False
    while not trouve and nbessai <= essaimax:
        reponse = int(input("Votre essai ? "))
        if reponse < cible:
            print("Plus grand!")
        elif reponse > cible:
            print("Plus petit")
        else:
            trouve = True
            print("Gagné en {} essais!".format(nbessai))
        nbessai += 1
    if not trouve:
        print("Perdu")
        print("Le nombre à deviner était {}".format(cible))
    


# In[2]:


def devinette_for3(n):
    cible = randint(1, n)
    nbessai = 1
    ## choisit la cible au hasaard entre 1 et n
    essaimax = int(input("Nombre maximum d'essais ? "))    
    ## affiche "Votre essai ?", attend que l'utilisateur rentre une
    ## valeur validée par entrée et convertit cette valeur en entier.
    for k in range(essaimax):
        reponse = int(input("Votre essai ? "))
        if reponse < cible:
            print("Plus grand!")
        elif reponse > cible:
            print("Plus petit")
        else:           
            print("Gagné en {} essais!".format(nbessai))
            break
    else:
        print("Perdu")
        print("Le nombre à deviner était {}".format(cible))


# In[59]:


def devinette_rec(n):
    
    def jeudevine(nbessai):
        """Fonction devinette recursive avec nombre d'essais maximum"""
        if nbessai > essaimax:
            print("Perdu")
            print("Le nombre à deviner était {}".format(cible))
        else:        
            reponse = int(input("Votre essai ? "))
            if reponse == cible:
                print("Gagné en {} essais!".format(nbessai))                
            else:
                if reponse < cible:
                    print("Plus grand!")
                else:
                    print("Plus petit")
                jeudevine(nbessai + 1)
                
    cible = randint(1, n)    
    ## choisit la cible au hasard entre 1 et n
    essaimax = int(input("Nombre maximum d'essais ? "))
    jeudevine(1)          


# In[60]:


devinette_rec(100)


# ## Exercice 3.16 Test de primalité

# In[111]:


def est_premier(n):
    # le plus grand diviseur premier de n distinct de n est <= sqrt(n)
    for diviseur in range(2, int(sqrt(n)) + 1):
        if n%diviseur == 0:
            return False
    return True if n > 1 else False
        


# In[110]:


[(n, est_premier(n)) for n in range(1, 101)]


# In[112]:


est_premier(51552127)


# La fonction implémentée effectue au plus $\sqrt{n}$ divisions si $n$ est premier

# ## Exercice 3.17 Quel jour sommes-nous ?

# In[92]:


def bissextile(n):
    return (n%100 != 0 and n%4 == 0) or n%400 == 0


# In[93]:


bissextile(2012), bissextile(2100), bissextile(2000), bissextile(2015)


# In[98]:


def premierjanvier(n):
    """Retourne le jour de la semaine codé de 0 pour lundi à 6 pour dimanchedu premier janvier de l'année n
    sachant que le premier janvier 2013 était un mardi.
    Fonctionne jusqu'au 1er janvier 1583 (debut du calendrier grégorien)."""
    semaine = ["lundi", "mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    jour = 1
    if n > 2013:
        courant, fin = 2013, n
        increment = 1
    elif n < 2013:
        courant, fin = 2012, n - 1
        increment = -1
    else:
        courant, fin = 2013, 2013
    while courant != fin:
        if bissextile(courant):
            jour = (jour + 366*increment)%7
        else:
            jour = (jour + 365*increment)%7
        courant += increment
    return semaine[jour]


# In[99]:


premierjanvier(1950),premierjanvier(2050)


# In[105]:


def joursemaine(jour, mois, annee):
    """Retourne le jour de la semaine  d'une date du calendrier grégorien. 
    Fonctionne jusqu'au 1er novembre 1582 (debut du calendrier grégorien).""" 
    semaine = ["lundi", "mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    #nombre de jours par mois dans une année normale
    jourmois = [31,28,31,30,31,30,31,31,30,31,30,31]
    if bissextile(annee):
        jourmois[1] += 1
    rangjour = 0
    for k in range(1, mois):
        rangjour += jourmois[k - 1]
    rangjour += jour
    #index du jour de la semaine du premier janvier
    premier = semaine.index(premierjanvier(annee)) 
    return semaine[(premier  + rangjour - 1)%7]


# In[103]:


joursemaine(12,7,1998)


# In[104]:


joursemaine(8,5,1945)


# ## Exercice bonus Suite de Fibonacci

# In[46]:


def fibo(n):
    """Retourne le terme de rang n de la suite de Fibonacci"""
    (a, b) = (1, 1)
    for k in range(1, n):
        (a, b) = (b, a + b)
    return a


# In[47]:


fibo(10)


# In[48]:


[fibo(n+1)/fibo(n) for n in range(0, 101, 10)]


# On retrouve que le quotient de deux termes successifs de la suite de Fibonacci tend vers le _nombre d'or_ $\frac{1+\sqrt{5}}{2}$.

# ## Exercice bonus

# On considère la suite définie par : $u_0=1   \text{ et }  \forall n \in \mathbb{N},\ u_{n+1}=\sqrt{u_n^2+\dfrac{1}{2^n}}.$

# In[73]:


from math import sqrt

def terme(n):
    """calcul du terme de rang n de la suite définie par u(0)=1 et u(n)=sqrt(u(n-1)**2+1/2**(n-1)"""
    # initialisation de la variable u contenant le terme u(n)
    u = 1
    p = 1 #puissance de 2
    for i in range(n):
        # attention i désigne l'indice du terme précédent        
        u = sqrt(u**2 + 1/p)
        p = 2*p
    return u


# In[74]:


[terme(10**k) for k in range(0, 5)]


# On peut conjecturer que la suite $\left(u_{n}\right)$ converge vers $\sqrt{3}$

# In[62]:


def seuil(e):
    """retourne le plus petit entier n tel que abs(u(n)-l)<=e"""
    n,u = 0,1
    l = sqrt(3)
    while abs(u-l)>e:
        u = sqrt(u**2+1/2**n)
        n += 1
    return n


# ## Exercice bonus  Suite de Syracuse

# In[75]:


def syracuse(u,n):
    """affiche les n premiers termes (de 0 à n-1) de la suite de syracuse de valeur initiale u(0)=u"""
    #affichage du terme de rang 0
    print('u(%s)=%s'%(0,u),end='')
    for i in range(1,n):
        if u%2 == 0:
            u = u//2
        else:
            u = 3*u + 1
        #affichage du terme de rang i
        print(',u(%s)=%s'%(i,u),end='')


# In[76]:


syracuse(5, 9)


# In[77]:


def first1syracuse(u):
    """affiche le rang du premier 1 dans la suite de syracuse de valeur initiale u(0)=u"""
    # i contient le rang du terme
    i = 0
    while u != 1:
        i += 1        
        if u%2 == 0:
            u = u//2
        else:
            u = 3*u + 1
    return i


# In[78]:


def maxsyracuse(u):
    """affiche la plus grande valeur atteinte jusqu'à l'apparition du premier 1 dans la suite de syracuse telle que u(0)=u"""
    # i pour le rang, m pour le maximum 
    i, m = 0, u
    while u != 1:
        i += 1        
        if u%2 == 0:
            u = u//2
        else:
            u = 3*u + 1
        if u > m:
            m = u
    return m

def maxpremier1(n):
    """Pour une suite de Syracuse telle que 1<=u(0)<=n, retourne la plus grande valeur de first1syracuse(u) ainsi que la valeur de u(0) correspondante"""
    u, m = 1, 0 # initialisation du rang maximal et du u(0) correspondant
    for v in range(2,n+1):
        rang = first1syracuse(v)
        if rang > m:
            u, m = v, rang
    return m,u

def maxpremier1liste(n):
    """idem mais affiche la liste des u(0) pour lesquels ce maximum est atteint"""
    L,m = [1],0
    for v in range(2,n+1):
        rang = first1syracuse(v)
        if rang > m:
            L= [v]
            m = rang
        elif rang == m:
            L.append(v)
    return m,L


# In[79]:


maxpremier1liste(55)

