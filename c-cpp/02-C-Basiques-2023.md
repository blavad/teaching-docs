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
<div class="coverCourseName"><span class="important">#2 </span>Basiques (1)</div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/ia-school-logo.svg" />
<div class="coverYear coverFooterRight">2023</div>

<!-- TABLE DES MATIERES -->

---

## Table des matières

<b><span class="important">01 </span> Entrées / Sorties</b>
cin. cout. scanf. printf.

<b><span class="important">02 </span> Types de variable</b>
Entiers. Nombres à virgule flottante.

<b><span class="important">03 </span> Déclaration de variables</b>
Affectation de base. Convention de nommage.

<b><span class="important">04 </span> Porter des variables</b>
Portée d'une variable. Espace de noms.

<b><span class="important">05 </span> Opérateurs de base</b>
Opérateurs arithmétiques. Opérateurs logiques. Priorité.

---

<!-- PARTIE 01 : Entrées / Sorties -->

<div class='main'>

# 01

## Entrées / Sorties

</div>

---

## Entrées et Sorties

Pour lire des entrées saisies au clavier (depuis l’entrée standard **stdin**), on utilisera :

- `scanf()` en C ou C++
- `cin` en C++

Pour afficher des résultats à l’écran (sur la sortie standard **stdout**), on utilisera :

- `printf()` en C ou C++
- `cout` en C++

<br/>

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Il existe d’autres types d’entrées/sorties (fichier, réseau, base de données, ...) pour les programmes. Nous les verrons plus tard.

</div>

---

## Entrées et Sorties

### **Exemple**

<div class='flex-horizontal'><div class='flex'>

**Exemple C++**

```cpp
#include <iostream>

int main (int argc, char **argv)
{
    int i;
    std::cout << "Entrez un entier : ";
    std::cin >> i;
    std::cout << "i = " << i << std::endl;

    return 0;
}
```

</div><div class='flex'>

**Exemple C**

```c
#include <iostream>

int main (int argc, char **argv)
{
    int i;
    printf("Entrez un entier : ");
    scanf("%d", &i);
    printf("La value de i est %d", i);

    return 0;
}
```

</div></div>

---

<!-- PARTIE 02 : Types de variables -->

<div class='main'>

# 02

## Types de variables

</div>

---

## Types de variables

### **Types entiers**

Les types entiers :

- **bool** : false ou true → booléen (seulement en C++ )
- **unsigned char** : 0 à 255 → entier très court (1 octet ou 8 bits)
- **char** : -128 à 127 → idem mais en entier relatif
- **unsigned short** : $0$ à $2^{16}$ → entier court (2 octets ou 16 bits)
- **short** : $-2^{15}$ à $2^{15}-1$ → idem mais en entier relatif
- **unsigned int** : $0$ à $2^{32}-1$ → entier sur 4 octets
- **int** : $-2^{31}$ à $2^{31}-1$ → idem mais en entier relatif
- **unsigned long** : $0$ à $2^{32}-1$ → entier sur 4 octets ou plus
- **long** : $-2^{31}$ à $2^{31}-1$ → idem mais en entier relatif
- **unsigned long long** : 0 à $2^{64}-1$ → entier sur 8 octets
- **long long** : $-2^{63}$ à $2^{63}-1$ → idem mais en entier relatif

---

## Types de variables

### **Types à virgule flottante**

Les types à virgule flottante :

- **float** : environ 6 chiffres de précision et un exposant qui va jusqu’à $±10^{±38}$
  → Codage IEEE754 sur 4 octets
- **double** : environ 10 chiffres de précision et un exposant qui va jusqu’à $±10^{±308}$
  → Codage IEEE754 sur 8 octets
- **long double** −→ Codé sur 10 octets

---

## Types de variables

### **Les constantes**

Les constantes :

- celles définies pour le préprocesseur. Il n’y a aucun typage de la constante.

```cpp
#define PI 3.1415 /* en C traditionnel */
```

- celles définies pour le compilateur : c’est une variable typée en lecture seule.

```cpp
const double PI = 3.1415; // en C++ et en C ISO
```

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Par convention, les noms des constantes sont en majuscules.

Exemple : `MAX_PLAYERS`, `HEIGHT`, `WIDTH`, etc..

</div>

---

<!-- PARTIE 03 : Convention de nommage -->

<div class='main'>

# 03

## Déclaration de variables

</div>

---

## Qu'est-ce qu'une variable ?

<div class='block note'>

<i class='block-icon fas fa-info'></i>

## Définition

En informatique, les variables sont des symboles qui associent un nom (**l'identifiant**) à une **valeur**. Dans la plupart des langages, **les variables peuvent changer de valeur au cours du temps**.

De plus, les variables ont un **type** de valeur (int, bool, double, ...).

</div>

En C / C++, la déclaration d'une variable se fait avec l'opérateur d'allocation `=`

**Exemples :**

```cpp
char letter = 'A';                  # variable de type entier (char)

int age = 23;                       # variable de type entier (int)

float moyenne = 10.8;               # variable de type flottant (float)

string prenom = "Jonathan";         # variable de type chaîne de caractères (string)
```

---

## Convention de nommage

**Nommage des variables**
Par convention, un nom de variable commence par une lettre minuscule puis les différents mots sont repérés en mettant en majuscule la première lettre.

_Exemples :_ `distance`, `distanceMax`, `consigneCourante`, `etatBoutonGaucheSouris`, `nbreDEssais`

**Nommage des constantes**
Par convention, un nom de constante est en majuscule.

_Exemple :_ `MAX_PLAYERS`, `HEIGHT`, `WIDTH`, ...

**Mots réservés**
Les mots réservés sont les mots prédéfinis du langage C.
Ils ne peuvent pas être réutilisés pour des identifiants.

_Exemples :_ `for`, `do`, `while`,`if`, `return`, `void`, `extern`, `break`, `static`, ...

---

<!-- PARTIE 04 : Portée des variables -->

<div class='main'>

# 04

## Portée des variables

</div>

---

## Portée d'une variable

La portée (scope) d’un identifiant (variables, fonctions, ...) est l’étendue au sein de laquelle cet identifiant est lié.

En C/C++, la portée peut être globale (en dehors de tout bloc {}) ou locale (au bloc {}).

```cpp
int uneVariableGlobale; // initialisée par défaut à 0

int main(int argc, char* argv[])
{
    int uneVariableLocale; // non initialisée par défaut
    {
        int uneAutreVariableLocale; // non initialisée par défaut
    }
    // la variable i est locale bloc for :
    for(int i=0;i<10;i++) cout << i;
    return 0;
}
```

<div class='block warning'>

<i class='block-icon fas fa-exclamation'></i>

Des variables déclarées dans des blocs différents peuvent porter le même nom.

</div>

---

## Espace de noms

---

<!-- PARTIE 05 : Opérateurs de base -->

<div class='main'>

# 05

## Opérateurs de base

</div>

---

## Opérateurs arithmétiques

Permettre d’effectuer des calculs mathématiques sur et entre les variables.

| Opérateur |         Nom          |  Usage  |
| :-------: | :------------------: | :-----: |
|     +     |       addition       | `a + b` |
|     -     |     soustraction     | `a + b` |
|    \*     |    multiplication    | `a * b` |
|     /     |       division       | `a / b` |
|     %     | reste de la division | `a % b` |

Ou encore d’effectuer opérations bits à bits sur les représentations binaires des variables.

| Opérateur |        Nom        |   Usage   |
| :-------: | :---------------: | :-------: |
|    <<     | décalage à gauche | `a << 3`  |
|    >>     | décalage à droite | `a >> 10` |
|     ~     |  complément à 1   |   `~a`    |

---

## Opérateurs logiques

Permettre de comparer et réaliser des tests logiques entre des valeurs.

| Opérateur |     Nom     |  Exemple   |
| :-------: | :---------: | :--------: |
|    ==     |   égalité   |  `a == b`  |
|    !=     | différence  |  `a != b`  |
|  < et <=  | infériorité |  `a < b`   |
|  > et >=  | supériorité |  `a >= b`  |
|    &&     |     ET      |  `a && b`  |
|   \|\|    |     OU      | `a \|\| b` |
|    ^^     | OU EXCLUSIF |  `a ^^ b`  |
|     !     |     NON     |    `!a`    |

---

## Opérateurs d’affectation

Pour mémoriser le résultat d'une opération dans une variable, on utilise l'opérateur d'affectation `=`.

| Opérateur |          Nom          |    Exemple     | Equivalence |
| :-------: | :-------------------: | :------------: | :---------: |
|     =     | affectation classique | `a = (3 == 4)` |      -      |
|    ++     |  incrémentation de 1  |     `a++`      | `a = a + 1` |
|    --     |  décrementation de 1  |     `a--`      | `a = a - 1` |
|    +=     |      additition       |    `a += b`    | `a = a + b` |
|    -=     |     soustraction      |    `a -= b`    | `a = a - b` |
|    \*=    |    multiplication     |    `a *= b`    | `a = a * b` |
|    /=     |       division        |    `a /= b`    | `a = a / b` |
|   \|\|    | reste de la division  |    `a %= b`    | `a = a % b` |

---

## Priorité des opérateurs

<div class='flex-horizontal'><div class='flex'>

|     Opérateurs      |             Description             |
| :-----------------: | :---------------------------------: |
|         ::          |         résolution de porté         |
| . -> [] () sizeof() | référence et sélection, parenthèses |
|    ! ~ ++ -- - +    |          unaires préfixés           |
|       \* / %        |           multiplicatifs            |
|         + -         |              additions              |
|        >> <<        |              décalages              |
|      < <= > >=      |          relations d'ordre          |
|       = = !=        |               égalité               |
|       && \|\|       |               logique               |
|         ? :         |       conditionnel (ternaire)       |
|     = += -= \*=     |             affectation             |

</div><div class='flex'>

<div class='block note'>

<i class='block-icon fas fa-info'></i>

# Note

On peut dans tous les cas forcer une évaluation allant contre les priorités définies en utilisant le parenthésage des expressions à évaluer en premier.

</div>

</div></div>
