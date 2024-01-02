---
marp: true
paginate: true

theme: dav-default
title: Cours POO - IA School

footer: "Programmation Orientée Objet 2023"
_footer: ""
---

<!-- PARTIE 0 : Présentation du cours -->

<!-- _paginate: skip -->
<!-- _class: cover -->

<div class="coverBlockCenter">
<div class="coverModuleName">Programmation Orientée Objet en Python</div>
<div class="coverCourseName"><span class="important">#0 </span>Programmation python</div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/ia-school-logo.svg" />
<div class="coverYear coverFooterRight">2023</div>

<!-- TABLE DES MATIERES -->

---

## Table des matières

<b><span class="important">01 </span> Types primitifs</b>
Booléens. Entiers. Flottants. Chaîne de caractères.

<b><span class="important">02 </span> Types composites</b>
Listes. Dictionnaire. Ensembles. Classes.

<b><span class="important">03 </span>Variables</b>
Déclaration d'une variable. Portée des variables.

<b><span class="important">04 </span> Conditions et boucles</b>
Conditions. Boucles.

<b><span class="important">05 </span> Les fonctions</b>
Définition de fonctions. Paramètres et valeur de retour.

<b><span class="important">06 </span> Packages</b>
Réutiliser le code existant.

---

<!-- PARTIE 01 : Type de données -->

<div class='main'>

# 01

## Type de données

</div>

---

## Les booléens

<div class='flex-horizontal'><div class='flex'>

**Valeurs :** `True`, `False`

**PEP 483 :** `bool`

**Représentation en machine**
| False | True |
|:---:|:---:|
| 0 | 1 |

**Opérateurs booléens**

`and`, `or`, `not`

</div><div class='flex'>

</div></div>

---

## Les entiers

<div class='flex-horizontal'><div class='flex'>

**Valeurs :** ..., -3, -2, -1, 0, 1, 2, 3, 4, ...

**PEP 483 :** `int`

**Représentation en machine**
La représentation des entiers en machine correspond sur la représentation des nombres entiers en base 2.

</div><div class='flex'>

**Opérateurs de comparaison**

- égalité : `==`
- inégalité : `!=`
- infériorité : `<`, `<=`
- supériorité : `>`, `>=`

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Les opérateurs de comparaisons retournent un booléen (`True` ou `False`).

</div>

</div></div>

---

## Les flottants

<div class='flex-horizontal'><div class='flex'>

**Valeurs :** Permet de s'approcher d'une représentation des **nombres réels** (bien qu'incomplète).

**PEP 483 :** `float`

**Représentation en machine**
https://fr.wikipedia.org/wiki/Virgule_flottante

</div><div class='flex'>

**Opérateurs de comparaison**

- égalité : `==`
- inégalité : `!=`
- infériorité : `<`, `<=`
- supériorité : `>`, `>=`

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Les opérateurs de comparaisons retournent un booléen (`True` ou `False`).

</div>

</div></div>

---

## Les caractères

<div class='flex-horizontal'><div class='flex'>

**Valeurs :** `'A'`, `'B'`, `'C'`, `';'`, `'!'`, `'0'`, `'1'`, ...

**Représentation en machine**

- [**Code ASCII**](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange)
- [**unicode**](https://fr.wikipedia.org/wiki/Unicode)

<div class='block warning'>

<i class='block-icon fas fa-exclamation'></i>

Le type caractère unique n'existe pas en tant que tel en python. Chaque caractère déclaré est interpréter par python comme une chaîne de caractère (cf ci-dessous).

</div>

</div><div class='flex'>

**Table ASCII**

![height:500px](./assets/img/ascii.jpg)

</div></div>

---

## Les chaînes de caractères

**Définition :** Une liste de caractères.

**Exemples :**
`"Brice"`, `"la vie est belle !"`, `"#0$£ù%&-"`

**PEP 483 :** `string`

**Opérateurs de bases**

- assigner une variable : `my_str = "bidule"`
- accès au 3ème caractère : `my_str[2]`
- accès au dernier caractère : `my_str[-1]`
- sous-chaîne : `my_str[:2]`, `my_str[1:]`, `my_str[1:2]`, `my_str[::2]`
- longueur de la chaîne : `len(my_str)`
- changer la casse : `my_str.capitalize()`, `my_str.upper()`, `my_str.lower()`
- vérifier la casse : `my_str.islower()`, `my_str.isupper()`

---

<!-- PARTIE 02 : Types composites -->

<div class='main'>

# 02

## Types composites

</div>

---

## Les listes

**Définition :** Une liste ordonnée de données.

**Exemples :**
`[0, 21, 13, 7, 100]`, `[]`, `[True, True, False]`, ...

**PEP 483 :** `list`

**Opérateurs de bases**

- assigner une variable : `l = []`
- accès au 3ème caractère : `l[2]`
- accès au dernier caractère : `l[-1]`
- sous-listes : `l[:2]`, `l[1:]`, `l[1:2]`, `l[::2]`
- ajout d'un élément à la fin : `l.append(3)`
- supprimer du 3ème élément : `l.remove(2)`
- tri d'une liste : `sorted(l)`

---

## Les dictionnaires

**Définition :** Un dictionnaire est une structure de données qui assimile des clés à des valeurs.

**Exemples :**
`{"nom" : "Fred", "age" : 20 }`, `{}`, `{True : "eat", False : [0, 1, 2]}`, ...

**PEP 483 :** `dict`

**Opérateurs de bases**

- assigner une variable : `d = {}`
- accès à une valeur (depuis sa clé) : `d[key]`
- ajout d'un élément à la fin : `d[key] = value`
- supprimer du 3ème élément : `del d[key]`
- accès aux clés : `d.keys()`
- accès aux valeurs : `d.values()`

---

<!-- PARTIE 01 : Nom section -->

<div class='main'>

# 03

## Variables

</div>

---

## Qu'est-ce qu'une variable ?

<div class='block note'>

<i class='block-icon fas fa-info'></i>

## Définition

En informatique, les variables sont des symboles qui associent un nom (**l'identifiant**) à une **valeur**. Dans la plupart des langages, **les variables peuvent changer de valeur au cours du temps**.

De plus, **les variables ont un type** de valeur.

</div>

En python, la déclaration d'une variable se fait avec l'opérateur d'allocation `=`

**Exemples :**

```python
prenom = "Jonathan"          # variable de type chaîne de caractères (str)
age = 23                     # variable de type entier (int)
moyenne = 10.8               # variable de type flottant (float)
notes = [16, 12, 13, 9]      # variable de type liste d'entiers (list[int])
```

---

## Portée des variables

**Portée des variables (globale / locale)**

```python
var1 = 10 # var1 est globale

def foo(var2): # var2 est locale
    var3 = 30 # var3 est locale
    if (var3 > 0):
        var4 = 40
        print(var1, var2, var3, var4) # 10, 20, 30, 40

    print(var1, var2, var3, var4) # 10, 20, 30, Erreur

foo(20)
print(var1, var2, var3, var4) # 10, Erreur, Erreur, Erreur


```

---

## Portée des variables

**Visibilité des variables**

```python
def foo():

    level1 = 10

    def bar():
        level2 = 20

        def tutu():
            level3 = 30

            print("from tutu:", level1, level2, level3)

        print("from bar: ", level1, level2) # level3 NOT visible
        tutu()

    print("from foo: ", level1) # level2 or level3 NOT visible here
    bar()
```

---

<!-- PARTIE 03 : Boucle et conditions -->

<div class='main'>

# 04

## Boucle et conditions

</div>

---

## Conditions

<div class='flex-horizontal'><div class='flex'>

**1. if / else**

```python
if (cond):
    # code si vrai
else:
    # code si faux
```

**2. if / else if / else**

```python
if (cond):
    # code si vrai
elif (cond2):
    # code si vrai
else:
    # code si faux
```

</div><div class='flex'>

<div class='block note'>

<i class='block-icon fas fa-info'></i>

La notation **cond** dans les exemples ci-contre représente une expression quelconque qui renvoit un booléen.

_Exemples :_

- `if True:`
- `if is_winner:`
- `if (age < 30):`
- `if (age < 20 and name == "Mathéo"):`
- `if "John" in names:`

</div>

</div></div>

---

## Boucles

<div class='flex-horizontal'><div class='flex'>

**1. for**

```python
for i in range(10):
    # ...
    # code ici
    # ...
```

**2. while**

```python
while (cond):
    # ...
    # code ici
    # ...
```

</div><div class='flex'>

</div></div>

---

<!-- PARTIE 04 : Packages  -->

<div class='main'>

# 05

## Fonctions

</div>

---

## Déclarer une fonction

Une fonction est définit grâce :

- au mot-clé `def` en python
- à un identifiant
- à des paramètres (optionnels)
- à un type de retour et une valeur de retour

_Exemple 1: Calcul de l'aire d'un rectangle_

```python
def aire_rectangle(longueur: int, largeur: int) -> int:
    return longueur * largeur
```

<div class='flex-horizontal'><div class='flex'>

_Exemple 2: Affichage des données d'une classe_

```python
def display_user_data(user: User) -> None:
    print("--- User Data ---")
    print("name=", user.name)
    print("age=", user.age)
```

</div><div class='flex'>

<br/>
<br/>

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Une fonction qui ne retourne aucune valeur est généralement appelée **méthode**.

</div>

</div></div>

---

<!-- PARTIE 04 : Packages  -->

<div class='main'>

# 06

## Packages & modules

</div>

---

## Réutiliser du code

En plus d'être simple et intuitif, le langage de programmation Python possède l'avantage d'avoir une très large communauté.

Ainsi, pas besoin de tout réimplémenter. Si vous avez besoin d'une fonctionnalité, quelqu'un l'aura probablement déjà implémenté et partagé avant vous.

<div class='block note'>

Un **module** est une collection de fonctions et méthodes qui peuvent être réutilisés dans une autre partie du code.

Un **package** est un ensemble de modules munis d'une documentation et conçus pour des besoins spécifiques.

_Exemples de package python :_ numpy, pandas, plotly, Django, Flask, PyTorch, Scikit Learn, ...

</div>

---

## Importer des fonctions & méthodes

**Importer tout un module**

```python
# Importer la library math
import math

# Retourne la racine carré de 9
print(math.sqrt(9))
```

**Importer une fonction spécifique d'un module**

```python
# Importer une fonction de la library math
from math import sqrt

# Retourne la racine carré de 9
print(sqrt(9))
```

---

## Notes de fin

Le cours actuel n'est pas un cours de programmation en python mais un cours de programmation orientée objet (POO avec python).

Ce document est un bref récapitulatif de certaines notions qui doivent être maîtrisées pour la bonne compréhension du cours de POO.

Pour revoir les bases du langage python, vous pouvez suivre le cours OpenClassroom ci-dessous (gratuit) :

https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python

Pour approfondir le cours actuel de programmation orientée objet avec python, vous pouvez suivre le cours OpenClassroom ci-dessous (gratuit) :

https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python
