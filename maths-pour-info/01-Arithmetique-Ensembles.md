---
marp: true
paginate: true

theme: dav-maths
title: Arithmétique

footer: "Mathématiques pour l'informatique"
_footer: ''
math: mathjax
---

<!-- PAGE DE COUVERTURE -->
<!-- _paginate: skip -->
<!-- _class: cover -->
<div class='coverBlockCenter'><div class='coverModuleName'>Mathématiques pour l'informatique</div><div class='coverCourseName'><span class='important'>#1 </span>Arithmétique</div><div class='coverAuthor'>par <span class='important'>David Albert</span></div></div><img style="background-color:#fff" class='coverFooterLeft' height='80px' src='./assets/img/logo-gema.png' /><div class='coverYear coverFooterRight'>2023</div>

---

<!-- TABLE DES MATIERES -->

## Table des matières

<b><span class='important'>01 </span>Ensemble et relations</b>
Les ensembles: notations et relations.

<b><span class='important'>02 </span> Divisibilité  </b>
Divisibilité. Partie entière. PGCD / PPCM. Nombres premiers.

<b><span class='important'>03 </span> Congruences</b>
Division euclidienne. Calcul modulaire.

<b><span class='important'>04 </span> Suites</b>
Suites arithmétiques. Démonstration par récurrence.

<!-- FIN TABLE DES MATIERES -->
---

<!-- PARTIE 01 : Ensemble et relations -->

<div class='main'>

# 01

## Ensemble et relations

</div>

---

## Notations


<span style="display: inline-block; width:4rem;">$\emptyset$</span>ensemble vide 

<span style="display: inline-block; width:4rem;">$\mathbb{N}$</span>ensemble des entiers naturels (positifs ou nuls) 

<span style="display: inline-block; width:4rem;">$\mathbb{N}^*$</span>ensemble des entiers naturels strictement positifs

<span style="display: inline-block; width:4rem;">$\mathbb{Z}$ </span>ensemble des entier relatifs

<span style="display: inline-block; width:4rem;">$\mathbb{Q}$ </span>ensemble des nombres rationnels

<span style="display: inline-block; width:4rem;">$\mathbb{R}$ </span>ensemble des nombres réels

<span style="display: inline-block; width:8rem;">$\in et \notin$ </span>appartenance à un ensemble

<span style="display: inline-block; width:4rem;">$\subseteq$ </span>inclusion d'un ensemble dans un sous-ensemble

<span style="display: inline-block; width:4rem;">$\cup$ </span>union de deux ensembles

<span style="display: inline-block; width:4rem;">$\cap$ </span>intersection de deux ensembles


---


## Ensemble
### **Définitions**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Ensemble</b>
</div>


Un **ensemble** est bien défini s’il est donné par une collection d’éléments qui satisfont une propriété caractéristique explicite, c’est-à-dire commune à tous les éléments de l’ensemble et à eux seuls. 

Si une telle propriété est notée $P$, on notera
$$\left\{ x \mid P (x)\right\}$$
l’ensemble correspondant, c’est à dire l’ensemble des x vérifiant la propriété $P$.


</div>

---

## Ensembles $\mathbb{N}, \mathbb{Z}, \mathbb{R}$



---

## Référentiel

Nous supposerons toujours que les éléments constituant nos ensembles font partie d’un **référentiel** (qui peut être, par exemple, les étudiants inscrits à ce cours, les nombres entiers, les nombres réels, les villes de Belgique, ...) et que **la propriété sélectionne** certains éléments de ce référentiel (par exemple, les étudiants inscrits au cours qui mesurent moins d’1m70, les nombres pairs, les nombres réels qui sont irrationnels, les villes de Flandre, ...). 

S’il n’y a pas d’ambiguïté sur le référentiel, on gardera la notation implicite $\left\{x \mid P (x)\right\}$. Si par contre, on souhaite distinguer deux référentiels, par exemple, ceux des entiers $\mathbb{Z}$ et des réels $\mathbb{R}$, on écrira $\left\{x \in \mathbb{Z} \mid x \leq 0\right\}$ et $\left\{x \in \mathbb{R} \mid x \leq 0\right\}$.

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Le référentiel peut être vu comme est un ensemble. 

</div>


---

## Relations ensemblistes
### **Définitions**

Soient $A$ et $B$ deux ensembles.

<b class='important'>Appartenance $\in$</b>
Si $x$ est un élément (de l’univers, le plus grand référentiel possible, et supposé connu
de tous...), on écrit $x \in A$ pour signifier que $x$ est un élément de $A$. On note aussi
$x \notin A$ pour signifier que $x$ n’est pas un élément de $A$.  

<b class='important'>Inclusion $\subseteq$</b>
On note l’inclusion de $A$ dans $B$ par $A \subseteq B$. Ceci signifie que tout élément de $A$ est
aussi un élément de $B$. On dit que $A$ est un sous-ensemble ou une partie de $B$

<b class='important'>Egalité $=$</b>
L’égalité de deux ensembles est bien définie. On écrit $A = B$ lorsque $A \subseteq B$ et
$B \subseteq A$. Autrement dit, $A$ et $B$ sont égaux lorsque tout élément de $A$ est aussi dans
$B$ et, inversement, tout élément de $B$ appartient également à $A$.


---

## Relations ensemblistes
### **Définitions**

Soient $A$ et $B$ deux ensembles.

<b class='important'>Union $\cup$</b>
L’union de $A$ et de $B$, notée $A \cup B$, est l’ensemble qui contient à la fois les éléments
de $A$ et de $B$. On a donc $A \cup B = \left\{x \mid x \in A\ ou\ x \in B\right\}$

<b class='important'>Intersection $\cap$</b>
L’intersection de $A$ et de $B$, notée $A \cap B$, est l’ensemble qui contient les éléments qui appartiennent à la fois à A et à B. On a donc $A \cap B = \left\{x \mid x ∈ A\ et\ x ∈ B\right\}$

<b class='important'>La différence $\setminus$ </b>
La différence de deux ensembles $A$ et $B$ (on dit aussi "A moins B"), notée $A \ B$, est l’ensemble qui contient les éléments de A n’appartenant pas à B. On a donc $A \ B = \left\{x \mid x ∈ A\ et\ x /∈ B\right\}$

<b class='important'>L'ensemble des parties</b>
L’ensemble des parties d’un ensemble $A$, noté $P(A)$, est l’ensemble de toutes les
parties de $A$ : $P(A) = \left\{ B : B \subseteq A \right\}$

---
## Relations ensemblistes
### **Propriétés**

Soit $X$ un ensemble et soient $A, B, C ∈ P(X)$. Alors
1. $A \cap B = B \cap A$
2. $A \cup B=B \cup A$
3. $X \setminus (A \cap B) = (X \setminus A) \cup (X \setminus B)$
4. $X \ (A \cup B) = (X \setminus A) \cap (X \setminus B)$
5. $A \cap (B \cap C) = (A \cap B) \cap C$
6. $A \cup (B \cup C) = (A \cup B) \cup C$
7. $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
8. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
9. $A \setminus B = A \cap (X \setminus B)$
10. Si $A \subseteq B$, alors $P(A) \subseteq P(B)$

---

## Ensembles et relations
### **Exercices**

Prouvez les propriétés (1), (2), (5) et (8)



---

<!-- PARTIE 02 : Divisibilité    -->

<div class='main'>

# 02

## Divisibilité 

</div>

---

## Notations


<span style="display: inline-block; width:8rem;">$a \mid b$ </span>a divise b

<span style="display: inline-block; width:8rem;">$\lfloor x \rfloor$ </span>partie entière de $x$

<span style="display: inline-block; width:8rem;">$\{x\}$ </span>partie décimale de $x$

<!-- $\lceil x \rceil$ </span>partie entière de $x$ -->

<span style="display: inline-block; width:8rem;">$PGCD$ </span>plus grand diviseur commun </span>

<span style="display: inline-block; width:8rem;">$PPCM$ </span>plus petit multiple commun </span>

<span style="display: inline-block; width:14rem;">$a ≡ b\ (mod\ N )$ </span>$a$ est congru à $b$ modulo $N$ </span>

---

## Divisibilité

<!-- <div class='block note'>

<i class='block-icon fas fa-info'></i> -->

### **Définition**

Si $a$ et $b$ sont deux entiers, on dit que $a$ divise $b$, ou que $b$ est divisible par $a$, s’il existe un entier $q$ tel que $b = aq$. 

On note $a|b$.

On dit encore que $a$ est un ***diviseur*** de $b$, ou que $b$ est un ***multiple*** de a.


<!-- </div> -->
 
---

## Divisibilité

### **Propriétés**
1. Si $a$ et $b$ sont deux entiers avec $b \ne 0$, $b$ divise $a$ si et seulement si la fraction $\frac{a}{b}$ est un entier.
1. Tous les entiers divisent 0 et sont divisibles par 1.
1. Un entier $n$ est toujours divisible par $1$, $−1$, $n$ et $−n$.
1. Si $a|b$, et $b|c$, alors $a|c$.
1. Si $a|b_1, b_2, ... , b_n$, alors $a|b_1c_1+b_2c_2+. . .+b_nc_n$, quels que soient les entiers $c_1, c_2, . . . , c_n$.
1. Si $a$ divise $b$ et $b \ne 0$, alors $|a| \le |b|$.
1. Si $a$ divise $b$ et $b$ divise $a$, alors $a = ±b$.
1. Si $a$ et b sont deux entiers tels que $a^n |b^n$ pour un entier $n > 1$, alors $a|b$.

---

## Divisibilité
### **Exercices**

**Exercice 1 :** Démontrez la propriété (4). 

**Exercice 2 :** Soient $x$ et $y$ des entiers. Montrer que $2x + 3y$ est divisible par $7$ si et seulement
si $5x + 4y$ l’est.

<!-- Solution : Supposons que 7 divise 2x + 3y, alors il divise 6 (2x + 3y) − 7 (x + 2y) = 5x + 4y.
R´eciproquement si 7 divise 5x + 4y, il divise 6 (5x + 4y) − 7 (4x + 3y) = 2x + 3y. -->

**Exercice 3 :** Pour quels entiers $n$ strictement positifs, le nombre $n^2 + 1$ divise-t-il $n + 1$ ?
<!-- Solution : Si n2 + 1 divise n + 1, comme tout est positif, on doit avoir n2 + 1 6 n + 1, ce qui
n’est v´erifi´e que pour n = 1. On v´erifie ensuite que n = 1 est bien solution. -->




---

## Parties entières
### **Définitions**


<div class='block note'>
<div class='block-icon'>
    <i class='far fa-heart' style="padding-right:1rem;"></i>
    <b >Partie entière</b>
</div>

<!-- # Définition II.1 : Partie entière -->
Si $x$ est un réel, on appelle **partie entière** de $x$, et on note $[x]$, le plus grand entier inférieur ou égal à $x$. 

Ainsi, on a $[x] \le x < [x] + 1$.

</div>


<div class='block note'>
<div class='block-icon'>
    <i class='fas fa-info' style="padding-right:1rem;"></i>
    <b>Remarque</b>
</div>

On définit aussi la **partie décimale** de $x$, comme la différence $x − [x]$.

</div>

---

## Parties entières

### **Propriétés**

1. Pour tout réel $x$, on a $x − 1 < [x] \le x$
1. $[−x] = −[x] − 1$ sauf si $x$ est entier, auquel cas $[−x] = −[x]$.
1. Si $x$ et $y$ sont deux réels, $[x] + [y] \le [x + y] \le [x] + [y] + 1$.
1. Si $m > 0$ est un entier, alors il y a exactement $[\frac{x}{m}]$ multiples de $m$ compris entre 1 et $x$.

---

## Parties entières
### **Exercices**
**Exercice 1 :** Démontrez les propriétés (1), ...

**Exercice 2 :** Donnez les parties entières des nombres suivants: $0,53$ ; $123,2453927$ ; $-1,25$ ; $-4150,67$ ; $\frac{2}{3} - \frac{23}{9}$ ; $\frac{2023}{0,6}$


---

## PGCD / PPCM
### **Définitions**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>PGCD</b>
</div>

Soient $a, b \in \mathbb{Z^*}$. L’ensemble des diviseurs communs de $a$ et de $b$ est fini et non vide. Il possède donc un plus grand élément appelé **plus grand commun diviseur (PGCD)** de $a$ et $b$ et noté $PGCD(a, b)$.

<div class='block no-icon'>
<!-- <i class='block-icon fas fa-info'></i> -->

Lorsque $PGCD(a, b) = 1$, on dit que $a$ et $b$ sont **premiers entre eux**.

</div>

</div>

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>PPCM</b>
</div>


Soient $a, b \in \mathbb{Z^*}$. L’ensemble des diviseurs communs de $a$ et de $b$ est fini et non vide. 
$a$ et $b$ possèdent un plus petit multiple commun positif, on l’appelle le **plus petit commun multiple (PPCM)** de $a$ et de $b$ et on le note $PPCM(a, b)$.

</div>

---

## PGCD / PPCM
### **Propriétés**

1. Si $d = PGCD(a, b)$, alors $n$ divise $a$ et $b$ si et seulement si $n$ divise $d$.
1. Si $m = PPCM (a, b)$, alors $n$ est un multiple $a$ et de $b$ si et seulement si $n$ est un multiple de $m$.
1. Si $a$, $b$ et $n$ sont des entiers non nuls et $n > 0$, alors $PGCD(na, nb) = nPGCD (a, b)$. 
Si de plus $n$ divise $a$ et $b$, alors $PGCD(\frac{a}{n}, \frac{b}{n}) = \frac{1}{n} PGCD(a, b)$.
1. Si $d = PGCD(a, b)$, on peut écrire $a = da'$ et $b = db'$ pour $a'$ et $b'$ des nombres premiers entre eux.
1. Si $a$ et $b$ sont des entiers, l'égalité $PGCD(a, b) = PGCD(a, a + b)$ est toujours vérifiée lorsqu’elle a un sens. En particulier, le PGCD de deux nombres consécutifs est $1$, et plus généralement, le PGCD de $a$ et de $a + n$ est un diviseur positif de $n$.
1. Plus généralement, si $x$, $y$, $a$, $b$, $a'$ et $b'$ sont des entiers alors : 
$$PGCD(x, y) \times | PGCD(ax + by, a'x + b'y) | \times (ab' − ba'
) PGCD(x, y)$$
En particulier si $|ab' − ba'| = 1$, alors $PGCD(x, y) = PGCD(ax + by, a'x + b'y)$.



---

## PGCD / PPCM
### **Exercices**


**Exercice 1 :** Démontrez les propriétés (1), ...

**Exercice 2 :** Soit $a, b \in \mathbb{Z^*}$. Montrez que $\forall n \in \mathbb{N^*}$, on a $PGCD(a^n, b^n) = PGCD(a, b)^n$

**Exercice 3 (Théorème de Bézout) :** Si $a$ et $b$ sont des entiers premiers entre eux, alors il existe des entiers $u$ et $v$ tels que $au + bv = 1$.

**Exercice 4 (Lemme de Gauss) :** Si des entiers $a$, $b$ et $c$ sont tels que $a$ divise $bc$ et $a$ premier avec $b$, alors $a$ divise $c$

---

## Nombres premiers
### **Définitions**

---

## Nombres premiers
### **Propriétés**

---

## Nombres premiers
### **Exercices**

**Exercice :** Démontrez les propriétés (1), ...

**Exercice :** Démontrez les propriétés (1), ...


---

<!-- PARTIE 03 : Congruences -->

<div class='main'>

# 03

## Congruences

</div>


---

 ## Notation

 $\equiv$ Congruences


---

## Exercices



<b class='important'>Division euclidienne</b>
**Exercice :** Démontrez les propriétés (1), ...



<b class='important'>Congruences</b>
**Exercice :** Démontrez les propriétés (1), ...


---


<!-- PARTIE 04 : Suites -->

<div class='main'>

# 04

## Suites

</div>

---

## Notations


<span style="display: inline-block; width:4rem;">$u_n$ </span>notation utilisé pour les suites 


<span style="display: inline-block; width:4rem;">$\sum$ </span>symbole de sommation

<span style="display: inline-block; width:4rem;">$\prod$ </span>symbole de produit


---

## Démonstration par récurrence
**Exemple**
Montrer que pour tout $n \in \mathbb{N}^*$, on a :

$$(i)\ \ \ \ \sum_{i=1}^{n}i = \frac{n(n+1)}{2}$$ 

$$(ii)\ \ \ \ \sum_{i=1}^{n}i^2 = \frac{n(n+1)(2n+1)}{6}$$ 



---







<script type='module'>
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });
window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>