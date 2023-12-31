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
<div class="coverCourseName"><span class="important">#3 </span>Polymorphisme</div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/ia-school-logo.svg" />
<div class="coverYear coverFooterRight">2023</div>

<!-- TABLE DES MATIERES -->

---

## Table des matières

<b><span class="important">00 </span> Rappel: Héritage</b>
Définition. Spécialisation. Surcharge de méthodes.

<b><span class="important">01 </span> Polymorphisme</b>
Définition. Spécialisation. Surcharge de méthodes.

<b><span class="important">02 </span> Héritage multiple</b>
Héritage multiple. Ordre d'héritage.

<b><span class="important">03 </span> Méthodes de classe</b>
Attribut / méthodes de classe. Décorateur **_@classmethod_**. Mot-clé **cls**.

---

<!-- PARTIE 4 : Héritage -->

<div class="main">

# 00

## Rappel : Héritage

</div>

---

## Héritage

En POO, l'<b class="important">héritage</b> est le concept qui permet de créer une nouvelle classe à partir d'une classe existante.

<div class="flex-horizontal">
<div class="flex">

**Syntaxe UML**
La classe `Bike` hérite de la classe `Vehicule`.
La classe <b class="important">fille</b> est `Bike`.
La classe <b class="important">parente</b> est `Vehicule`.

![height:250px](assets/img/diag-heritage.png)

</div>
<div class="flex">

**Syntaxe python**

```python
class Vehicule: # ici on définit la classe mère
    def __init__(self, wheels, brand):
        self._brand = brand
        self._wheels = wheels

    def accelerate(self):
        print("Go !")

class Bike(Vehicule): # class fille
    def __init__(self):
        super().__init__(2, "Canyon")
```

En héritant de `Vehicule`, la classe `Bike` hérite de ses méthodes.

```python
b = Bike()
b.accelerate()
# Go !
```

</div>
</div>

---

## Classe abstraite

**Définition**
Une <b class="important">classe abstraite</b> est une classe qui comprend **au moins** une méthode **non implémentée**.

<div class="flex-horizontal">
<div class="flex" style="flex:0.4;">

**Syntaxe UML**

![height:250px](assets/img/diag-abstract.png)

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Les méthodes abstraites sont écrites en _italique_. A la main, on <u>souligne</u>.

</div>

</div>
<div class="flex" style="flex:0.6">

**Intérêt**

- Implémenter certains opérationes communes à un groupe d'objets malgré que le concept soit encore _abstrait_

**Syntaxe python**

```python
from abc import ABC, abstractmethod

class Vehicule(ABC):
    def accelerate(self):
        print("Go !")

    def turnLeft(self):
        print("Go left !")

    @abstractmethod
    def isFrenchBrand(self):
        pass
```

</div>
</div>

---

## Interface

**Définition**
Une <b class="important">interface</b> est une classe abstraite particulière. Elle ne contient **aucun attribut** et ses méthodes ne sont **pas implémentées**.

<div class="flex-horizontal">
<div class="flex" style="flex:80">

<div class='flex-horizontal'><div class='flex' style='flex:0.9'>

**Intérêts**

- Définir les opérations sans préciser leur implémentation
- Préciser les conditions et les effets de l'invocation des opérations

</div><div class='flex' style='flex:0.1'>

**Syntaxe UML**
![height:250px](assets/img/diag-interface.png)

</div></div>

<div class="block warning">

<i class="block-icon fas fa-exclamation"></i>

Les **classes abstraites** et les **interfaces** ne seront **jamais instanciées** directement.

</div>

</div>

<div class="flex" style="flex:35">

**Syntaxe python**

```python
from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def turnLeft(self):
        pass

    @abstractmethod
    def isFrenchBrand(self):
        pass
```

</div>
</div>

---

<!-- PARTIE 1 : Polymorphisme -->

<div class="main">

# 01

## Polymorphisme

</div>

---

## Polymorphisme

<div class="flex-horizontal">
<div class="flex">

En POO, le <b class="important">polymorphisme</b> est le concept qui permet de **modifier le comportement** d’une classe fille par rapport à sa classe mère.

Cela permet d’utiliser l’héritage comme:

- mécanisme de **spécialisation** d'un concept.
- mécanisme d’**extension du système**.

</br>

<div class='block note'>
<div class='block-icon'>
<i class='fas fa-info'></i>
</div>

1. On définit une **interface commune** à une famille d'objets (la classe de base).

2. On écrit les **détails d'implémentations** des classes spécialisées.

</div>

</div>
<div class="flex" style="flex:0.5;">

<h4 style="text-align:center; font-style:italic;">Polymorphisme</h4>
<p style="text-align:center;; font-style:italic;">"qui peut prendre plusieurs formes"</p>

![width:100%](assets/img/metamorphe.png)

<!-- ![bg right:40% contain 90%](https://www.pokepedia.fr/images/c/c2/Sprite_0132_HOME.png) -->
</div>
</div>

---

## Polymorphisme en pratique (1)

<div class="flex-horizontal">
<div class="flex">

![width:500px](assets/img/diag-poly1.png)

</div>
<div class="flex">

On surcharge la méthode `accelerate`.

```python
class Vehicule:
    def accelerate(self):
        raise NotImplementedError("The method is abstract")

class MotorlessVehicule(Vehicule):
    def accelerate(self):
        print("Go cleanly !")

class Bike(MotorlessVehicule):
    def accelerate(self):
        print("Go cleanly by bike!")

class Bike(MotorlessVehicule):
    def accelerate(self):
        print("Go cleanly by skate!")
```

L'implémentation d'`accelerate` n'est pas la même pour un vélo et un skateboard.

</div>
</div>

---

## Polymorphisme en pratique (2)

Nous pouvons appeler la méthode `accelerate` d'un objet sans nous soucier de son type intrinsèque.

```python
vehicules : list[Vehicule] = []
vehicules.append(Car())
vehicules.append(Skateboard())

for v in vehicules:
    v.accelerate()

# OUTPUT
# Go cleanly by bike!
# Go cleanly by skate!
```

---

<!-- _class: sm-font-size -->

## Surcharger une méthode

Pour un fonctionnement ...

**Cas 1 : ... identique à la classe mère**
On ne fait rien. Le mécanisme d'héritage se chargera d'appeler la bonne fonction.

```python
class A:
    def method(self):
        print('A')

class B(A):
    pass

b = B()
b.method() # A
```

**Cas 2 : ... différent de la classe mère**
On réimplémente la méthode dans la classe fille.

```python
class C(A):
    def method(self):
        print('C')

c = C()
c.method() # C
```

---

<!-- _class: sm-font-size -->

## Surcharger une méthode

Pour un fonctionnement ...

**Cas 3 : ... avec des fonctionnalités en plus de celles de la classe mère**
On utilise le mot-clé <b class='important'>super</b> pour appeler la méthode mère de façon intelligente.

```python
class D(C):
    def method(self):
        super().method()
        print('D')

d = D()
d.method() # C D
```

**Cas 4 : ... identique à une classe parente spécifique**
On appel la méthode d'une classe parente comme ci-dessous.

```python
class E(C):
    def method(self):
        A.method(self)
        print('E')

e = E()
e.method() # A E
```

---

## Spécialisation / Généralisation

### **En pratique**

<div class='flex-horizontal'><div class='flex'>

#### Spécialisation

**En pratique**
C'est ce que l'on fait quand on a besoin d'une nouvelle brique logicielle très proche d'une existante. On spécialise la brique existante.

**Exemple**
On a une classe **Client** et on souhaiterait avoir une fonctionnalité supplémentaire pour un type de client particulier (les **ClientPremium**) sans avoir à modifier le système actuel. On spécialise la classe **Client** en y ajoutant la fonctionnalité.

</div><div class='flex'>

#### Généralisation

**En pratique**
C'est ce que l'on fait quand on remarque que l'utilisation de plusieurs briques logicielles est proche et que l'on veut les utiliser de façon interchangeable.

**Exemple**
On a une classe **Client** et une classe **Administrateur** et on se rend compte que certains comportements sont identiques. On généralise le concept d'**Utilisateur** en créant une interface / classe abstraite dont héritent **Client** et **Administrateur**.

</div></div>

---

<!-- PARTIE 2 : Héritage multiple -->

<div class="main">

# 02

## Héritage multiple

</div>

---

<!-- _class: sm-font-size -->

## Héritage multiple

**Python permet d'hériter de plusieurs classes.**
`class Fille(Parent1, Parent2, Parent3)`

Afin de pouvoir déboguer lors d'erreurs avec l'héritage multiple, il est possible de connaître l'ordre d'héritage. Pour cela, on utilise la méthode `__mro__`.

```python
class A():
    pass

class B():
    pass

class C(A, B):
    pass

if __name__ == '__main__':
    # Attention, __mro__ est un attribut de classe.
    # Il doit donc etre recupere depuis la classe
    print(C.__mro__)
```

L'exécution de ce code renvoit

```bash
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <type 'object'>)
```

---

## Order d'héritage

<div class="flex-horizontal">
<div class="flex">

**Exercice**

```python
class A():
    pass

class B():
    pass

class C(A):
    pass

class D(B,A):
    pass

class E(D,A):
    pass

class F(E, D):
    pass

class G(F, C):
    pass
```

</div>
<div class="flex">

**Question 1 :** Qu'affiche ce programme ?

```python
print(C.__mro__)
```

**Question 2 :** Qu'affiche ce programme ?

```python
print(D.__mro__)
```

**Question 3 :** Qu'affiche ce programme ?

```python
print(E.__mro__)
```

**Question 4 :** Qu'affiche ce programme ?

```python
print(G.__mro__)
```

</div>
</div>

---

## Order d'héritage

<div class="flex-horizontal">
<div class="flex">

**Exercice**

```python
class A():
    pass

class B():
    pass

class C(A):
    pass

class D(B,A):
    pass

class E(D,A):
    pass

class F(E, D):
    pass

class G(F, C):
    pass
```

</div>
<div class="flex">

**Réponse 1 :**

```
(<class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

**Réponse 2 :**

```
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

**Réponse 3 :**

```
(<class '__main__.E'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>,
<class 'object'>)
```

**Réponse 4 :**

```
(<class '__main__.G'>, <class '__main__.F'>, <class '__main__.E'>, <class '__main__.D'>,
<class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

</div>
</div>

---

<!-- PARTIE 4 : Attributs et méthodes de classes -->

<div class="main">

# 03

## Méthodes de classe

</div>

---

## Définition

**Avant propos**
Jusqu'à présent nous avons utilisé des **méthodes d'instances**. Celles-ci sont propres à un objet et manipulent les données de ce dernier (**= attributs d'instances**).

<b class="important">Méthodes de classe</b>
Maintenant, nous allons voir comment utiliser des **méthodes de classe**. Celles-ci manipulent des données communes à toutes les instances d'une même classe (**= les attributs de classes**). Les méthodes de classe sont définies grâce au décorateur `@classmethod` et prennent en 1er argument le paramètre `cls` (une référence vers la classe).

**Exemples d'usages**

- Stocker des constantes de classe
- Garder un compteur du nombre d'instances
- Créer un constructeur alternatif
- Profiling (nombre de passage et temps dans passé dans chaque fonction)

---

## Exemple

```python
class Counter:
    count = 0                   # attribut de classe

    def __init__(self, name):
        self.name = name        # attribut d'instance

    @classmethod
    def add(cls, num):          # méthode de classe
        cls.count += num


if __name__ == '__main__':
    c1 = Counter("Counter #1")
    c2 = Counter("Counter #2")

    print(Counter.count, c1.count, c2.count)
    # output : 0 0 0

    Counter.add(5)
    print(Counter.count, c1.count, c2.count)
    # output : 5 5 5

    c1.add(5)
    print(Counter.count, c1.count, c2.count)
    # output : 10 10 10

    c2.add(-10)
    print(Counter.count, c1.count, c2.count)
    # output : 0 0 0
```

<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });

window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>
