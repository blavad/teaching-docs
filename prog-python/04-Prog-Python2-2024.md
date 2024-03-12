---
marp: true
paginate: true

theme: dav-maths
title: Cours POO - IA School

footer: "Programmation Orientée Objet 2023"
_footer: ""
---

<!-- PARTIE 0 : Présentation du cours -->

<!-- _paginate: skip -->
<!-- _class: cover -->

<div class="coverBlockCenter">
<div class="coverModuleName">Informatique & Programmation</div>
<div class="coverCourseName"><span class="important">#4 </span>Programmation python</div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/logo-gema.png" />
<div class="coverYear coverFooterRight">2024</div>

<!-- TABLE DES MATIERES -->

---

## Table des matières

<b><span class="important">01 </span> Conditions</b>
if. else. elif.

<b><span class="important">02 </span> Boucles</b>
for. while.

<b><span class="important">03 </span> Les fonctions</b>
Définition de fonctions. Paramètres et valeur de retour.

<b><span class="important">04 </span> Packages</b>
Réutiliser le code existant.

---

<!-- PARTIE 03 : Boucle et conditions -->

<div class='main'>

# 01

## Conditions

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

**_Exemple_**

```python
temperature = input("Entrez une valeur : ")
if (temperature >= 100)
{
  print("L'eau bout !")
}
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

<!-- PARTIE 03 : Boucle et conditions -->

<div class='main'>

# 02

## Boucles

</div>

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

**_Exemple_**

```python
secret = "azezesx"
motDePasse = input("Entrez le mot de passe : ")
while (motDePasse != secret or agePersonne <= 3)
{
  print("Accès refusé")
  motDePasse = input("Réessayez : ")
}
```

</div></div>

---

## `break` et `continue`

Utilisation des instructions break et continue.

---

<!-- PARTIE 04 : Packages  -->

<div class='main'>

# 03

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

Une fonction qui ne retourne aucune valeur est généralement appelée **procédure**.

</div>

</div></div>

---

<!-- PARTIE 04 : Packages  -->

<div class='main'>

# 04

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
