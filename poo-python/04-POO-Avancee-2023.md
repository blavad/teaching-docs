---
marp: true
paginate: true

theme: dav-default
title: Cours POO - IA School

footer: 'Programmation Orientée Objet 2023'
_footer: ''
---

<!-- PARTIE 0 : Présentation du cours -->

<!-- _paginate: skip -->
<!-- _class: cover -->

<div class="coverBlockCenter">
<div class="coverModuleName">Programmation Orientée Objet en Python</div>
<div class="coverCourseName"><span class="important">#4 </span>POO Avancée</div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/ia-school-logo.svg" />
<div class="coverYear coverFooterRight">2023</div>


<!-- TABLE DES MATIERES -->
--- 

## Table des matières 

<b><span class="important">01 </span> SOLID principles</b>
Définition et explications.

<b><span class="important">02 </span> Design patterns</b>
Quelques exemples.

<b><span class="important">03 </span> Mieux coder en python</b>
Documentation. Gestion des erreurs. Tests unitaires.

---

<!-- PARTIE 01 : SOLID principles -->

<div class='main'>

# 01

## SOLID principles*

</div>

<div style="position:absolute;bottom:10%">
*cette section reprend les exemples de <a href="https://gist.github.com/dmmeteo"><b class='important'>@dmmeteo</b></a> 
</div>

---

## **S**ingle responsability 

**Explication**
Chaque classe / composant logiciel doit avoir une responsable unique. 

<div class='flex-horizontal'><div class='flex'>
<h4 class="success">
<i class='fas fa-check'></i>
GOOD
</h2>

```python
class Animal:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
```

</div><div class='flex'>
<h4 class="error">
<i class='fas fa-xmark'></i>
BAD
</h2>


```python
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass
```

<i class='fas fa-arrow-up'></i> Ici, la classe `Animal` a deux responsabilités: gérer la base de données et gérer les attributs.

</div></div>

---

## **O**pen-Closed


**Explication**
Chaque entité logiciel (classe, module, fonction) doit être ouverte à l'extension mais fermée à la modification. 

<div class='flex-horizontal'><div class='flex'>
<h4 class="success">
<i class='fas fa-check'></i>
GOOD
</h2>

```python
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
            return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2
```

</div><div class='flex'>
<h4 class="error">
<i class='fas fa-xmark'></i>
BAD
</h2>


```python
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
            if self.customer == 'fav':
                return self.price * 0.2
            if self.customer == 'vip':
                return self.price * 0.4
```

<i class='fas fa-arrow-up'></i> Ici, au moindre souhait d'ajouter un nouveau type de remise, on devrai toucher le code existant !

---

## Substitution de **L**iskov


**Explication**
Une sous-classe doit être substituable à sa super-classe. Le but est de s'assurer qu'une sous-classe peut prendre la place de sa super-classe sans erreur. 

<div class='flex-horizontal'><div class='flex'>
<h4 class="success">
<i class='fas fa-check'></i>
GOOD
</h2>

```python
def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())
        
animal_leg_count(animals)
```

</div><div class='flex'>
<h4 class="error">
<i class='fas fa-xmark'></i>
BAD
</h2>


```python
def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))
        
animal_leg_count(animals)
```

<i class='fas fa-arrow-up'></i> Ici, le type de classe est vérifié, le principe de substitution de Liskov est donc violé !

---

## Séparation des **I**nterfaces

**Explication**
Fournir des interfaces simples et spécifiques. Ne pas contraindre la personne qui voudra étendre notre logiciel de dépendre d'interfaces qu'il n'utilise pas.

<div class='flex-horizontal'><div class='flex'>
<h4 class="success">
<i class='fas fa-check'></i>
GOOD
</h2>

```python
class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass
```

</div><div class='flex'>
<h4 class="error">
<i class='fas fa-xmark'></i>
BAD
</h2>


```python
class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError
```

<i class='fas fa-arrow-left'></i> Ici, on pourra utiliser une combinaison de plusieurs interfaces pour créer des formes particulières: demi cercle, triancle rectangle, ...


---

## Inversion des **D**épendances

**Explication**
La dépendance doit porter sur les abstractions et non sur les concrétions.

<div class='flex-horizontal'><div class='flex'>
<h4 class="success">
<i class='fas fa-check'></i>
GOOD
</h2>

```python
class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError

class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection
    
    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url, options: dict):
        self.http_connection.request(url, 'POST')

class XMLHttpService(Connection):
    xhr = XMLHttpRequest()
    def request(self, url: str, options:dict):
        self.xhr.open()
        self.xhr.send()
```

</div><div class='flex'>
<h4 class="error">
<i class='fas fa-xmark'></i>
BAD
</h2>


```python
class XMLHttpService(XMLHttpRequestService):
    pass

class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service
    
    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url, options: dict):
        self.xml_http_service.request(url, 'POST')

```

<i class='fas fa-arrow-up'></i> Ici, la classe de haut-niveau (http) dépend d'une implémentation spécifique pour le bas niveau et non d'une abstraction.


---

<!-- PARTIE 02 : Design patterns -->

<div class='main'>

# 02

## Design patterns

</div>


---

## Introduction

Les <b class='important'>patrons de conception</b> (design patterns) sont des solutions classiques à des problèmes récurrents de la conception de logiciels. 

Chaque patron est une sorte de plan ou de schéma que vous pouvez personnaliser afin de résoudre un problème récurrent dans votre code. 

Dans ce cours, nous présenterons 4 patrons de conception classiques.

<div class='block note'>

<i class='block-icon fas fa-info'></i>

# <b class='important'><a href="https://refactoring.guru/fr/design-patterns">Refactoring Guru</a></b> contient les explications de 22 patrons de conceptions classiques et leur utilisation.

</div>

---

## Singleton

---

## Factory Method

---

## Strategy

---

## Builder

---

## Adapter

---

## State

---

## Observer


---

## Patron de méthode

https://refactoring.guru/fr/design-patterns/template-method

