---
marp: true
paginate: true

theme: custom
title: Cours POO - IA School

backgroundColor: "#eee"
color: "#070219"
backgroundSize: cover
backgroundImage: url(./assets/img/bg1.png)
_backgroundImage: url(./assets/img/POO-cover-bg.png)
footer: 'Programmation Orientée Objet 2023'
_footer: ''
style: pre.mermaid { all: unset; }

---

<!-- PARTIE 0 : Présentation du cours -->

<!-- _paginate: skip -->

<div class="coverBlockCenter">
<div class="coverModuleName">Programmation Orientée Objet en Python</div>
<div class="coverCourseName"><span class="important">#2 </span>Encapsulation</div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/ia-school-logo.svg" />
<div class="coverYear coverFooterRight">2023</div>



<!-- TABLE DES MATIERES -->
--- 

## Table des matières 

<b><span class="important">01 </span> Classes et objets</b>
Classes. Objets. Attributs et méthodes. Instances.


<b><span class="important">02 </span> Encapsulation</b>
Données privées, publiques.


<b><span class="important">03 </span> Constructeur / Destructeur</b>
Constructeur par défaut. Constructeur par recopie.

<b><span class="important">04 </span>Le mot clé: <span class="important">self</span></b>


---
<!-- PARTIE 1 : OBJETS ET CLASSES -->

<div class="main">

# 01 

## Classes et objets

</div>

---

## Les classes

Une <b class="important">classe</b> est un **type de données** composite  constitué:
- de données que l’on appelle <b class="important">attributs</b> (variables primitives ou objets)
- de <b class="important">méthodes</b> permettant de traiter ces données et des données extérieures à la classe

<div class="flex-horizontal">
<div class="flex">

<b class="important">Syntaxe UML</b>

![height:300px](assets/img/class-citroenC3.png)

</div>
<div class="flex">

<b class="important">Syntaxe python</b>

```python
class CitroenC3:
    def __init__(self):
        self._id = 0
        self._currentSpeed = 0 
        self._maxSpeed = 210
        self._year = 2010
    
    def accelerate(self):
        pass

    def turnLeft(self, deg):
        pass

    def turnRight(self, deg):
        pass
```

</div>
</div>


--- 
## Les objets

Un <b class="important">objet</b> est une **variable** dont le type est une classe particulière. On dit qu'un objet est une <b class="important">instance de classe</b>. 


<div class="flex-horizontal">
<div class="flex">

<b class="important">Syntaxe UML</b>

<!-- ![width:300px](assets/img/class-ex.png) -->

</div>
<div class="flex">

<b class="important">Syntaxe python</b>
Pour instancier un objet en python on fait appel au constructeur.

```python 
voitureDidier : CitroenC3 = CitroenC3()
#------------   ---------   -----------
#   objet        classe     constructeur
```

<div class="block note">
    
<i class="block-icon fas fa-lightbulb"></i> 

Dans un même programme il y a généralement plusieurs instances d'une même classe.

</div>

</div>
</div>



---

## Objets et classes

<b class="important">Différence classe et objet</b>

Il n’existe qu’une classe CitroenC3 mais il peut exister de nombreuses instances de cette classe.
```python 
voitureDidier : CitroenC3 = CitroenC3()
#------------   ---------   -----------
#   objet        classe     constructeur
```

<div class="block note">
    
<i class="block-icon fas fa-lightbulb"></i> 

# Pour mieux comprendre

**Classe =** Le moule pour fabriquer des objets = type de données contenant des données (attributes) et des fonctions (méthodes)

**Objet =** une instance de classe (l’objet une fois créé) = une donnée spécifique

</div>

---
<!-- PARTIE 2 : ENCAPSULATION -->

<div class="main">

# 02 

## Encapsulation

</div>

---
## Encapsulation 
<b class="important">Princpe</b>

<!-- _backgroundImage: url(./assets/img/bg4.png) -->

<div class="flex-horizontal">
<div class="flex">

Usage simple et visible 

![width:500px](assets/img/POO-Encapsulation-visible.drawio.png)

</div>

<div class="flex">

Fonctionnement complexe et caché

![width:500px](assets/img/POO-Encapsulation-hidden.drawio.png)

</div>
</div>


---

## Encapsulation

<b class="important">Visibilité des données</b>

Lors de la conception d’un programme orienté-objet, le programmeur doit:
- identifier les objets et les données appartenant à chaque objet
- les droits d’accès qu’ont les autres objets sur ces données

L’encapsulation de données dans un objet permet de cacher ou non leur existence aux autres objets du programme. Une donnée peut être déclarée en accès :

- **public** : les autres objets peuvent accéder à la valeur de cette donnée ainsi que la modifier

- **privé** : les autres objets n’ont pas le droit d’accéder directement à la valeur de cette donnée (ni de la modifier). En revanche, ils peuvent le faire indirectement par des méthodes publiques de l’objet concerné



---

## Encapsulation

<b class="important">Bonnes pratiques</b>

- ne rendre publique que le stricte minimum
  - les fonctions nécessaires à l’usage (`accelerate`, `turnLeft`, `turnRight`)
  - et pas plus (`increaseSpeed`, `turnLeftWheel`) 
- suivre le principe de **responsabilité unique** - **S** de **S**OLID
    - exemple [Animal / AnimalDB](https://gist.github.com/dmmeteo/f630fa04c7a79d3c132b9e9e5d037bfd) 
- n’utiliser que des **attributs privés** donc, si c’est raisonnable de penser qu’on a besoin:
    - de lire leur valeur depuis l’extérieur, on utilise un **getter**
    - de modifier leur valeur depuis l’extérieur, on utilise un **setter**




---

## Encapsulation

<b class="important">Syntaxe python</b>


---
<!-- PARTIE 3 : ENCAPSULATION -->

<div class="main">

# 03

## Constructeur

</div>

---
<!-- PARTIE 4 : SELF -->

<div class="main">

# 04

## Le mot clé : **self**

</div>

