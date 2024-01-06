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
<div class="coverCourseName"><span class="important">#3 </span>Basiques (2)</div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/ia-school-logo.svg" />
<div class="coverYear coverFooterRight">2023</div>

<!-- TABLE DES MATIERES -->

---

## Table des matières

<b><span class="important">00 </span> Les 5 concepts de la POO</b>
Classes. Objets. Encapsulation. Héritage. Polymorphisme.

<b><span class="important">01 </span> Classes et objets</b>
Classes. Objets. Attributs et méthodes. Instances.

<b><span class="important">02 </span> Constructeur</b>
Constructeur. Constructeur par défaut.

<b><span class="important">03 </span> Encapsulation</b>
Données privées, publiques. Getter / Setter. Mot-clé self.

<b><span class="important">04 </span> Héritage</b>
Héritage. Classe abstraites. Interfaces.

<b><span class="important">05 </span> Built-in functions</b>
Fonctions intégrées : \_\_init\_\_, \_\_str\_\_, \_\_eq\_\_, ...

---

<!-- PARTIE 01 : Instructions de contrôle -->

<div class='main'>

# 01

## Instructions de contrôle

</div>

---

## Instructions de contrôle

### **Conditions (if / else)**

<div class='flex-horizontal'><div class='flex'>

**1. if / else**

```cpp
if (cond) {
    // code si vrai
} else {
    // code si faux
}
```

**2. if / else if / else**

```cpp
if (cond) {
    // code si vrai
} else if (cond2) {
    // code si vrai
} else if (cond3) {
    // code si vrai
} else {
    // code si faux
}
```

</div><div class='flex'>

**_Exemple_**

```cpp
int temperature;
scanf("%d", &temperature);
if (temperature >= 100)
{
  printf("L'eau bout !");
}
```

<div class='block note'>

<i class='block-icon fas fa-info'></i>

La notation **cond** dans les exemples ci-contre représente une expression quelconque qui renvoit un booléen.

_Exemples :_

- `if (true)`
- `if (is_winner)`
- `if (age < 30)`
- `if (age < 20 && name == "Mathéo")`

</div>

</div></div>

---

## Instructions de contrôle

### **Conditions (switch)**

**_Exemple_**

```cpp
  switch (unite)
  {
    case 'i':
      cout << longueur << " in == " << conversion * longueur << " cm\n";
      break;
    case 'c':
      cout << longueur << " cm == " << longueur / conversion << " in\n";
      break;
    default:
      cout << "Désolé, je ne connais pas cette unité " << unite << endl;
      break;
  }
```

_Notes_

- la valeur utilisée par le **_switch()_** doit être un entier, un char ou une énumération.
- on peut utiliser plusieurs **_case_** menant à la même instruction
- !!! Ne pas oublier les **_break_**

---

## Instructions de contrôle

### **Boucles (do / while)**

<div class='flex-horizontal'><div class='flex'>

**1. while ... do ...**

```cpp
while (cond) {
    // ...
    // code ici
    // ...
}
```

**2. do ... while ...**

```cpp
do {
    // ...
    // code ici
    // ...
} while (cond);
```

</div><div class='flex'>

**_Exemple_**

```cpp
while (motDePasse != secret || agePersonne <= 3)
{
  printf("Accès refusé\n");
  scanf("%d %d", &agePersonne, &motDePasse);
}
```

</div></div>

---

## Instructions de contrôle

### **Boucles (for)**

**_for (expression1 ; expression2 ; expression3 ) instructions_**

avec

- `expression1` est la condition de départ (initialisations).
- `expression2` est la condition de fin.
- `expression3` est l’ incrément de boucle.

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Les 5 étapes du déroulement d’une boucle for sont :

1. `expression1` est évaluée avant d'entrer dans le for
2. `expression2` est évaluée
3. si `expression2` est vrai, instructions est exécuté, sinon, on passe après la fin de la boucle et l’exécution de la boucle est finie
4. `expression3` est évaluée après l’exécution de instructions
5. on revient en 2

</div>

---

## Instructions de contrôle

### **Boucles (for)**

**_Exemple 1_**

```cpp
for (int i = 0; i < 100; i++) {
  cout << i << '\n';
}
```

**_Exemple 2_**

```cpp
for (int i = 100; i >= 0; i--) {
  cout << i << '\n';
}
```

---

<!-- PARTIE 02 : Conversion de type -->

<div class='main'>

# 02

## Conversion de type

</div>

---

## Conversion de type (cast)

### **Implicite / explicite**

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Le compilateur ne peut appliquer des opérateurs qu’à des opérandes de même type.

**Exemple :** il n’existe pas d’addition pour : 2 + 1.5 car 2 est un entier et 1.5 est un flottant.

</div>

Il existe deux types de conversions :

1. **sans perte** : int → float (2 devient 2.0)
   ces conversions sont automatiquement réalisées par le compilateur
1. **avec perte** : float → int (1.5 devient 1)
   ces conversions doivent être explicitées par le programmeur

---

## Conversion explicite

### **Conversion explicite**

<div class='flex-horizontal'><div class='flex'>

**Ancien opérateur (C/C++)**
On utilise l’opérateur de **cast** en précisant le type entre parenthèses devant la variable à convertir (C/C++).

</div><div class='flex'>

_Exemple :_

```cpp
float a = 2.5;
int b = (int)a;  // force la variable a en int
```

</div></div>

**Nouveaux opérateurs (C++ uniquement)**

- **static_cast** : opérateur de transtypage à tout faire.
- **const_cast** : opérateur spécialisé et limité au traitement des caractères const et volatile.
- **dynamic_cast** : opérateur spécialisé et limité au traitement des downcast (transtypage descendant dans le cas d’héritage en POO).
- **reinterpret_cast** : opérateur spécialisé dans le traitement des conversions de pointeurs.

_Exemple :_

```cpp
float a = 2.5;
int b = static_cast<int>(a);  // force la variable a en int
```

---

<!-- PARTIE 03 : Pointeurs -->

<div class='main'>

# 03

## Pointeurs

</div>

---

<!-- PARTIE 03 : Tableaux et containers -->

<div class='main'>

# 03

## Tableaux et containers

</div>

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
