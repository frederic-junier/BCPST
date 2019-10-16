
# coding: utf-8

# # TP 1 Premiers pas en Python

# ## Installation de l'Ide Pyzo et de la distribution Python Anaconda
# 
# * Le plus simple est d'installer l'environnement de développement (ou Integrated Development Environment)  [Pyzo](http://www.pyzo.org/start.html#quickstart) puis  la distribution Python [Anaconda](https://www.continuum.io/downloads) en suivant le [guide rapide d'installation](http://www.pyzo.org/start.html#quickstart) sur le site de Pyzo. Installez bien Anaconda et non pas Miniconda (sauf sur votre clef USB éventuellement) car Anaconda inclut tous les modules nécessaires et le Jupyter Notebook si pratique que vous êtes en train d'utiliser. Par la suite nous travaillerons plutôt avec l'IDE Pyzo.
# 
# * `pygame` pose problème avec conda et pip. Dans ce cas on se rend sur le site http://www.lfd.uci.edu/~gohlke/pythonlibs/   et on télécharge  le paquet wheel  de pygame qu'on installe avec pip install paquet.whl
# 
# * En cas de problème contactez le professeur par la messagerie de  [l'ENT](http://le-parc.elycee.rhonealpes.fr).

# ## S'exercer à la programmation en Python
# 
# * Le site de référence est [http://www.france-ioi.org](http://www.france-ioi.org), si vous souhaitez progresser, il faut s'entraîner et ce site est la plateforme idéale : créez un compte puis suivez le parcours lycée pour commencer.
# 
# * Pour visualiser ce que fait la machine lors de l'exécution d'un code Python, et mieux comprendre le fonctionnement du langage, un bon outil est [http://pythontutor.com/](http://pythontutor.com/)

# ## Exercice 3  Calculs en Python

# In[1]:


2 + 5


# In[2]:


2*5


# In[3]:


2**5 #exponentiation


# In[2]:


2.2/3.5


# In[6]:


17.0/5.0


# In[15]:


17//5


# In[18]:


get_ipython().run_cell_magic('python', '', 'print(17/5)   #en python2')


# In[21]:


17/5  #en python3


# In[22]:


3//-2


# In[23]:


-(3//2)


# In[24]:


(-3)%2


# In[25]:


3%(-2)


# In[26]:


-(3%2)


# ## Les instructions d'entrée / sortie

# ### La fonction `print`
# 
# * On utilise la fonction `print` pour un affichage sur la sortie standard qui par défaut est l'écran. 
# 
# 

# In[3]:


print(Bonjour)


# Pour afficher du texte, celui-ci doit être contenu dans une chaîne de caratère délimitée par des apostrophes comme 'La mer' ou des guillemets comme "L'océan".

# In[4]:


print('Bonjour')


# On peut aussi afficher la valeur d'une _expression_ obtenue par évaluation d'une combinaison de _littéraux_  (valeurs correspondant aux types de base du langage), d'opérateurs et de variables 

# In[5]:


n = 2000
print(2017 - n)


# On peut passer plusieurs arguments à la fonction `print` en les séparant par une virgule, `print` les affichera par concaténation en utilisant un espace vide par défaut comme séparateur.

# In[6]:


print('Vous avez ', 2017 - n, ' ans')


# Par défaut, `print` effectue un saut de ligne après chaque affichage mais on peut changer ce comportement par défaut en réglant le paramètre optionnel `end=''`.

# In[7]:


print('Ligne 1')
print('Ligne 2')


# In[8]:


print('Colonne 1', end='|')
print('Colonne 2')


# On peut aussi changer le paramètre de séparation par défaut `sep=''`.

# In[9]:


print('Colonne 1', 'Colonne 2', sep='|')


# Pour afficher l'aide sur une fonction en `python`, on peut utiliser la documentation en ligne sur [https://docs.python.org/3/](https://docs.python.org/3/) ou la documentation intégrée avec la fonction `help`.

# In[11]:


help(print)


# ## Exercice 5

# In[5]:


2 * 5
4 * 5
print(3 * 5)


# ### La fonction `input`
# 
# * La fonction `input` récupère un texte un saisi par l'utilisateur après un `prompt` et retourne la saisie sous forme de chaîne de caractères. La fonction prend comme argument optionnel le `prompt` qui doit être une chaîne de caractères.

# ## Exercice 5 compléments
# 
# - Testez le programme ci-dessous.
# 
# - Comment expliquez-vous la réponse de l'interpréteur ?
# 
# - Comment  peut-on corriger ce  programme ?
# 

# In[ ]:


date = input('Entrez votre date de naissance : ')
print('Vous avez  ', 2017 - date, 'ans')


# ## Importation de modules

# On peut importer le module/bibbliothèque `math` en créant juste un point d'accès (on donne les clefs de la bibliothèque).
# C'est malin, mais contraignant car il faut faire précéder chaque nom de fonction de bibliothèque du nom de la bbibliothèque.

# In[7]:


import math


# In[8]:


math.sqrt(4)


# Pour alléger la syntaxe, on peut emprunter une fonction de la bibliothèque et l'importer dans l'espace de nom du programme (quitte à le "polluer" et à créer des conflits de nommage avec des fonctions ou variables existantes ou importées d'autres bibliothèques)

# In[9]:


from math import sqrt


# In[10]:


sqrt(4)


# In[12]:


log(1)


# In[13]:


math.log(1)


# Parfois on importe toutes les fonctions de la bibliothèque (on la déménage à l'intérieur de son programme quitte à l'encombrer inutilement avec des fonctions qui ne nous serviront à rien)

# In[14]:


from math import *


# In[16]:


log(1)


# Une solution intermédiaire est d'utiliser un alias pour la la bibliothèque.

# In[17]:


import matplotlib.pyplot as plt


# In[21]:


get_ipython().magic('matplotlib inline')
plt.plot([0,4],[0,4])


# ## La boucle `for` ou boucle  inconditionnelle 
# 
# Une boucle inconditionnelle permet de répéter un bloc d'instructions lorsqu'on connaît à l'avance le nombre de répétitions. 
# 
# La situation la plus courante est :
#     
#     Pour k allant de 1 à 10 répéter 
#         Bloc d'instructions
#     FinPour
# 
# Sa traduction en `Python` est :
# 
# ~~~python
# # flux parent
# for k in range(1, 11):
#     # bloc d'instructions
# # retour au flux parent
# ~~~
# 
# On remarque l'utilisation `range(1, 11)` alors qu'on attendrait `range(1, 10)`.
# 
# En fait `range(1, 11)` retourne un _itérateur_, qui va parcourir avec un incrément de 1 tous les entiers $n$ tels que $1 \leqslant n < 11$. 
# 
# Il faut bien se souvenir que la borne supérieure de `range(n, m)` est exclue mais il est facile de retenir que le nombre de tours de boucles est  $m - n$.
# 
# Par exemple, pour calculer la somme des tous les entiers consécutifs de 100 à 200, on peut écrire :
# 
# ~~~python
# somme = 0
# for k in range(100, 201):
#     somme = somme + k
# print("La somme est ", somme)
# ~~~
# 
# S'il s'agit juste de répéter `n` fois un bloc d'instructions on utilise le raccourci `range(n)` au lieu de `range(0, n)` ou de `range(1, n + 1)`.
# 
# Par exemple pour dire 100 fois "Merci", on peut écrire :
# 
# ~~~python
# for k in range(100):
#     print("Merci !")
# print("Ouf!")
# ~~~
# 
# La fonction range offre un troisième paramètre optionnel qui permet de changer l'incrément par défaut qui est 1.
# 
# Par exemple, pour pour calculer la somme des tous les entiers pairs consécutifs entre  100 et 200, on peut écrire :
# 
# ~~~python
# sommePair = 0
# for k in range(100, 201, 2):
#     sommePair = sommePair + k
# print("La somme est ", sommePair)
# ~~~
# 
# Enfin, la boucle `for` permet aussi de parcourir des objets itérables comme les chaînes de caractères, les listes, les fichiers etc ...
# 
# Par exemple pour afficher les caractères consécutifs de la chaîne "Bonjour" avec un caractère par ligne, on peut écrire :
# 
# ~~~python
# chaine = "Bonjour"
# for c in chaine:
#     print(c)
# ~~~
# 
# Autre exemple, pour afficher des messages d'invitation personnalisés :
# 
# ~~~python
# for nom in ["Jean-Luc", "Emmanuel", "François", "Marine"]:
#     print("Salut", nom, "je t'invite à mon anniversaire samedi !")
# ~~~

# ## Exercice 6

# In[27]:


for i in range(2,5):
    print(i**2)


# ## L'affectation et le type d'une variable
# 
# Une _variable_ est l'association d'un espace de la mémoire de l'ordinateur, accessible par son nom, et  d'une valeur que l'on y stocke. En Python on définit une variable par une instruction d'affectation, par exemple pour affecter la valeur 12 à la variable de nom `a` on écrit :
# 
# ~~~python
# a = 12
# ~~~
# 
# Un langage de programmation fixe des contraintes pour les nomes de variables. En Python les seuls caractères autorisés sont les caractères non accentués, les chiffres (sauf en première position) et le tiret bas (mais pas le tiret haut).
# 
# ~~~python
# 1var = 13     #nom incorrect
# var1 = 13     #nom correct
# var-1 = 14     #nom incorrect
# var_1 = 14     #nom correct
# ~~~
# 
# Un langage de programmation n'accepte par défaut qu'un nombre fini de types de valeurs, ainsi une variable est caractérisée par son __type__ accessible par la fonction `type` et qu'on peut afficher avec la fonction `print`:
# 
# ~~~python
# type(a)
# ~~~

# ## Exercice 7  Variables et affectations

# In[24]:


a = 3


# In[25]:


b = 4


# In[23]:


a + 1


# In[26]:


(2**a + 12)/b


# In[27]:


a = 851


# In[28]:


a = a + 1


# In[29]:


a


# In[30]:


852 = a


# ## Exercice 8

# In[31]:


from math import pi, floor


# In[32]:


a, b, c = 5, 3**4, 2*pi


# In[33]:


a + b


# In[34]:


a*c/b


# In[35]:


(a - b)/c


# In[36]:


a = a + 2


# In[37]:


a = 5
b = 7
a = b
a + 3


# In[38]:


a, b


# In[39]:


d = c/4


# In[40]:


d


# In[41]:


int(d)


# In[42]:


round(d)


# In[43]:


floor(d)


# In[44]:


int(-d)


# In[45]:


round(-d)


# In[46]:


floor(-d)


# On peut remarquer que `int` tronque la partie décimale et convertit le réel approché en entier et que `floor` retourne la partie entière du réel approché. Quant à `round` elle arrondit à l'entier le plus proche.

# ## Exercice 9

# In[54]:


x = 10
y = 15
z = x + y
x = y
y = z
print(x + y + z)


# ## Exercice 10

# In[ ]:


a = 100
b = 17
c = a - b
a = 2
c = a + b


# In[64]:


(a, b, c)


# In[65]:


a = 3
b = 4
c = a
a = b
b = c


# In[66]:


(a, b, c)


# ## Exercice 11

# In[58]:


a, b = 3, 4


# In[59]:


a + 1


# In[60]:


(2**a + 12)/b


# In[61]:


(a == 2) or (a != 2 and b > 6)


# In[62]:


"j'ai " + str(b**a) + " ans"


# ### Opérateurs 
# 
# Une condition de test doit avoir une  valeur booléenne, ce  peut être le résultat :
# 
# * d'une _comparaison arithmétique_ entre deux valeurs numériques `a` et `b` :
# 
#     - _l'égalité_ dont la syntaxe en `Python` est   `a == b`
#     - _la différence_ dont la syntaxe en `Python` est `a != b`
#     - _l'inégalité_ dont la syntaxe en `Python` est `a < b` ou `a > b` ou `a <= b` ou ` a >= b`
#     
# * d'une _opération logique_ entre  deux valeurs booléennes `x` ou `y` :
#     - la _négation logique_ dont dont la syntaxe en `Python` est   `not x`
#     - le _ou inclusif_  dont la syntaxe en `Python` est   `x or y`
#     - le _et_  dont la syntaxe en `Python` est   `x and y`
#     
# Il existe des règles de priorité : opérateurs arithmétiques prioritaires sur les opérateurs logiques, `not` prioritaire sur `and` qui  est prioritaire sur `or`. Des parenthèses permettent de changer les priorités.

# ## Exercice 11 compléments sur les tests 
# 
# Deviner les valeurs booléennes affichées par le programme ci-dessous puis vérifier en l'exécutant.
# 
# ~~~python
# a = 504
# b = 505
# print(not (a > b))
# print( a == b or a < b)
# print( not ( a > 0 and a < b))
# print((b - a) ** 2 == 1 and a != b - 1)
# print((False or not False) and not(False and True))
# ~~~

# ## Exercice 12 Calculs

# In[ ]:


from math import pi, exp, floor


# In[57]:


x = float(input('Entrez un réel x : '))
print(x**5*exp(pi*floor(x)))


# ## Exercice 12 Moyenne de notes

# In[55]:


n = int(input('Entre le nombre de notes : '))


# In[56]:


total = 0
for k in range(n):
    total += float(input('Entrez la note {:d} '.format(k+1)))
print("Moyenne arrondie au centième : {:02.2f}".format(total/n))
    


# ## Exercice 13

# In[72]:


pttc = float(input('Prix TTC (TVA à 19.6 %) au centime près : \n'))
pht = pttc/1.196
tva = pttc-pht
print('Le prix HT est de {:.2f} et la TVA est de {:.2f}'.format(pht,tva))


# In[73]:


pht = float(input('Entrez un prix  HT au centime près : \n'))
taux = float(input('Entrez un taux de TVA sous la forme 19.6 : \n'))
print('Le prix TTC est de {:.2f}'.format((1+taux/100)*pht))


# ## Exercice 14 Echange de deux variables de type entier

# ### Méthode classique avec variable de stockage

# In[48]:


x = int(input('Entrez la valeur de la variable x : '))


# In[49]:


y = int(input('Entrez la valeur de la variable y : '))


# In[50]:


z = x
x = y
y = z


# In[51]:


x, y


# ### Méthode classique sans variable de stockage

# In[52]:


x = x + y
y = x - y
x = x - y


# In[53]:


x, y


# ### Méthode Pythonique avec affectation parallèle

# In[78]:


a = int(input('Entrez la valeur de la variable a : '))


# In[79]:


b = int(input('Entrez la valeur de la variable b : '))


# In[80]:


a, b = b, a


# In[81]:


a, b


# ## Exercice 15

# In[86]:


c = 1 - 1j


# In[94]:


type(c)


# In[92]:


c.__class__


# In[96]:


type(1j)


# In[88]:


dir(c)


# In[89]:


c.real, c.imag    


# In[97]:


def module(n):
    if type(n) == type(1j):
        return ((n.real)**2 + (n.imag)**2)**(1/2)
    else:
        return None


# In[98]:


module(c)


# In[101]:


def argument(n):
    import math
    if type(n) == type(1j):
        real, imag = n.real, n.imag
        if imag > 0:
            return math.acos(real/module(n))
        else:
            return -math.acos(real/module(n))       
    else:
        return None
    


# In[102]:


argument(c)


# In[103]:


-math.pi/4


# In[108]:


c.conjugate()


# In[109]:


argument(c.conjugate())


# ### Exercice 16 compléments
# 
# * Le programme ci-dessous calcule la somme des `n` premiers entiers de 1 à `n`, la valeur  entière strictement positive de  `n` étant saisie par l'utilisateur. On notera l'utilisation de `k += 1` comme raccourci pour l'incrémentation `k = k + 1`. Recopier et compléter ce programme pour qu'il calcule également le produit des `n` premiers entiers consécutifs $1 \times 2 \times 3 \times \ldots \times n$. Tester pour $n = 100$, que peut-on dire de l'ordre de grandeur du produit ? 
# 
# ~~~python
# n = int(input('Entrez un entier n strictement positif : '))
# somme = 0
# for k in range(1, n + 1):
#     somme += k
# print(somme)
# ~~~
# 
# * Écrire un programme qui affiche les 10 premiers multiples de 2  sous la forme :
# 
#     2 x 1 = 2    
#     2 x 2 = 4    
#     ....    
#     2 x 10 = 20
#     
# * Modifier le programme précédent pour qu'il affiche les tables de mulplications pour les  10 premiers multiples de tous les entiers compris entre 1 et 9
