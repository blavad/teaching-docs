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
<div class="coverModuleName">Programmation C / C++</div>
<div class="coverCourseName"><span class="important">#4 </span>C / C++ avancé</div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/logo-gema.png" />
<div class="coverYear coverFooterRight">2023</div>

<!-- TABLE DES MATIERES -->

---

## Table des matières

<b><span class="important">01 </span> Les conteneurs STL</b>
vector. iterator. map.

<b><span class="important">02 </span> Les fichiers</b>

<b><span class="important">03 </span> C et Unix</b>

<b><span class="important">04 </span> La programmation modulaire en C</b>

<b><span class="important">05 </span> Les pointeurs intelligents</b>

---

<!-- PARTIE 04 : Les conteneurs STL -->

<div class='main'>

# 01

## Les conteneurs STL

</div>

---

## Conteneurs

En C, l'unique type permettent de regrouper des variables de même type au sein d'une même entité est le tableau.

En C++, il existe de nombreux autres conteneurs (vector, list, map, stack, queue, ...).

En C++, on privilégiera toujours l'utilisation de conteneurs STL par rapport à une implémentation manuelle.

<br/>
<br/>
<br/>

**Liste des conteneurs STL :** https://cplusplus.com/reference/stl/

---

## Les tableaux dynamiques - **vector**

**Définition**
Un **vector** est un conteneur séquentiel qui encapsule les tableaux de taille dynamique.

**Usage**

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> vect(5); // un vecteur de 5 entiers

    vect[0] = 1; // accès direct à l’indice 0 pour affecter la valeur 1

    vect.push_back( 6 ); // ajoute l’entier 6 à la fin

    vect.pop_back(); // supprime le dernier élément

    cout << "Le vecteur vect contient " << vect.size() << " entiers : \n";

    cout << "Le 3 ème élément contient la valeur " << vect[2] << "\n";

    return 0;
}
```

---

## Notion d'itérateur - **iterator**

**Définition**
Les **iterator** sont une généralisation des pointeurs : ce sont des objets qui pointent sur d’autres objets. Ils sont utilisés pour **parcourir une série d'objets**.

**Usage**

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> v2(4, 100); // un vecteur de 4 entiers initialisés avec la valeur 100

    cout << "Le vecteur v2 contient " << v2.size() << " entiers : ";

    // utilisation d’un itérateur pour parcourir le vecteur v2
    for (vector<int>::iterator it = v2.begin(); it != v2.end(); ++it) {
        cout << " " << *it;
    }

    return 0;
}
```

---

## La table associative - **map**

**Définition**
Une **map** permet d’associer une clé à une donnée.

**Usage**

```cpp
#include <iostream>
#include <iomanip>
#include <map>
#include <string>
using namespace std;

int main()
{
    map<string, unsigned int> nbJoursMois;

    nbJoursMois["janvier"] = 31;
    nbJoursMois["février"] = 28;
    cout << "La map contient " << nbJoursMois.size() << " elements : \n";

    for (map<string,unsigned int>::iterator it=nbJoursMois.begin(); it!=nbJoursMois.end(); ++it)
    {
        cout << it->first << " -> \t" << it->second << endl;
    }

    cout << "Nombre de jours du mois de janvier : " << nbJoursMois.find("janvier")->second << ’\n’;

}
```

---

<!-- PARTIE 02 : Les fichiers -->

<div class='main'>

# 02

## Les fichiers

</div>
