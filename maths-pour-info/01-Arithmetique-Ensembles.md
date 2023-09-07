---
marp: true
paginate: true

theme: dav-maths
title: Arithmétique

footer: "Mathématiques pour l'informatique"
_footer: ""
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

<b><span class='important'>02 </span> Divisibilité </b>
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

## Ensembles $\emptyset, \mathbb{N}, \mathbb{Z}, \mathbb{R}$

**Ensemble vide $\emptyset$**
Un ensemble qui ne contient aucun élément s'appelle l'ensemble vide et se note $\emptyset$

**Nombres entiers naturels $\mathbb{N}$**
Un nombre entier naturel est un nombre entier qui est positif.
L'ensemble des **nombres entiers naturels** est noté $\mathbb{N}$.
$\mathbb{N} = \left\{0,1,2,3,4...\right\}$

**Nombres entiers relatifs $\mathbb{Z}$**
Un nombre entier relatif est un nombre entier qui est positif ou négatif.
L'ensemble des **nombres entiers relatifs** est noté $\mathbb{Z}$.
$\mathbb{Z} = \left\{..., −3,−2 ,−1, 0 ,1, 2 , 3,...\right\}$

**Nombres réels $\mathbb{R}$**
L'ensemble des **nombres réels** est noté $\mathbb{R}$.
C'est l'ensemble de tous les nombres qui peuvent être représentés par une partie entière et une liste finie ou infinie de décimales.

---

## Ensemble et intervalles

### **Définitions**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Définition - Ensemble</b>
</div>

Un **ensemble** est bien défini s'il est donné par une collection d'éléments qui satisfont une propriété caractéristique explicite, c'est-à-dire commune à tous les éléments de l'ensemble et à eux seuls.

Si une telle propriété est notée $P$, on notera $\left\{ x \mid P (x)\right\}$ l'ensemble correspondant, c'est à dire l'ensemble des x vérifiant la propriété $P$.

</div>

**Exemples :**

- $A = \left\{ x \in \mathbb{N} \mid x > 12 \right\}$ est l'ensemble des entiers strictements supérieurs à $12$.

- $B = \left\{ x \in \mathbb{N} \mid x > 3\ et\ \frac{x}{2} - \lfloor \frac{x}{2} \rfloor \neq 0 \right\}$ est l'ensemble des nombres impaires strictements supérieurs à $3$.

- $\mathcal{C}_{\Omega, r} = \left\{ (x, y) \in \mathbb{R}^2 \mid (x-x_{\Omega})^2 + (y-y_{\Omega})^2  = r^2 \right\}$ est l'ensemble des points du cercle de centre $\Omega = (x_{\Omega},y_{\Omega}) \in \mathbb{R}^2$ et de rayon $r$.

---

## Référentiel

Nous supposerons toujours que les éléments constituant nos ensembles font partie d'un **référentiel** (qui peut être, par exemple, les étudiants inscrits à ce cours, les nombres entiers, les nombres réels, les villes de Belgique, ...) et que **la propriété sélectionne** certains éléments de ce référentiel (par exemple, les étudiants inscrits au cours qui mesurent moins d'1m70, les nombres pairs, les nombres réels qui sont irrationnels, les villes de Flandre, ...).

S'il n'y a pas d'ambiguïté sur le référentiel, on gardera la notation implicite $\left\{x \mid P (x)\right\}$. Si par contre, on souhaite distinguer deux référentiels, par exemple, ceux des entiers $\mathbb{Z}$ et des réels $\mathbb{R}$, on écrira $\left\{x \in \mathbb{Z} \mid x \leq 0\right\}$ et $\left\{x \in \mathbb{R} \mid x \leq 0\right\}$.

**Exemple**
Soit $A=\left\{0,1,2\right\}$, $B=\{-51, 23, -1, -6, 10\}$ et $\mathbb{N}$, trois référentiels distincts.

On a $\left\{x \in A \mid x < 0\right\} \ne \left\{x \in B \mid x < 0\right\} \ne \left\{x \in \mathbb{Z} \mid x < 0\right\}$

En effet,
$(i)\ \left\{x \in A \mid x < 0\right\} = \emptyset$
$(ii)\ \left\{x \in B \mid x < 0\right\} = \{-51, -1, -6\}$
$(iii)\ \left\{x \in \mathbb{Z} \mid x < 0\right\} = \{..., -4, -3, -2, -1\}$

---

## Ensembles et intervalles

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Définition - Intervalle</b>
</div>

Un **intervalle de $\mathbb{R}$** est une partie $I$ de $\mathbb{R}$ vérifiant la propriété suivante:

$$\forall x,y \in I,\ \forall z \in \mathbb{R};\ si\ x \le z \le y\ alors\ z \in I$$

</div>

On démontre alors qu'un intervalle est forcément un ensemble du type suivant :

<div class='flex-horizontal'><div class='flex'>

- L'ensemble vide $\emptyset$
- $\left\{ a \right\} = [a,a]$
- $\mathbb{R} = ]-\infty,+\infty[$
- $\{x \in \mathbb{R} \mid a \leq x \leq b \} = [a , b]$ <i class='important' style="font-size:0.85rem">(fermé borné)</i>
- $\{x \in \mathbb{R} \mid a < x < b \} = ]a, b[$ <i class='important' style="font-size:0.85rem">(ouvert borné)</i>
- $\{x \in \mathbb{R} \mid a < x \leq b \} = ]a, b]$ <i class='important' style="font-size:0.85rem">(borné, ouvert à gauche)</i>
- $\{x \in \mathbb{R} \mid a \leq x < b \} = [a, b[$ <i class='important' style="font-size:0.85rem">(borné, ouvert à droite)</i>

</div><div class='flex'>

- $\left\{x \in \mathbb{R} \mid x < a\right\} = ]-\infty, a[$ <i class='important' style="font-size:0.85rem">(non borné, fermé à gauche)</i>
- $\left\{x \in \mathbb{R} \mid x \leq a\right\} = ]-\infty, a]$ <i class='important' style="font-size:0.85rem">(non borné, fermé à droite)</i>
- $\left\{x \in \mathbb{R} \mid x > a \right\} = ]a, +\infty[$ <i class='important' style="font-size:0.85rem">(non borné, ouvert à gauche)</i>
- $\left\{x \in \mathbb{R} \mid x \geq a\right\} = [a, +\infty[$ <i class='important' style="font-size:0.85rem">(non borné, ouvert à droite)</i>

</div></div>

---

## Relations ensemblistes

### **Définitions**

Soient $A$ et $B$ deux ensembles.

<b class='important'>Appartenance $\in$</b>
Si $x$ est un élément (de l'univers, le plus grand référentiel possible, et supposé connu
de tous...), on écrit $x \in A$ pour signifier que $x$ est un élément de $A$. On note aussi
$x \notin A$ pour signifier que $x$ n'est pas un élément de $A$.

<b class='important'>Inclusion $\subseteq$</b>
On note l'inclusion de $A$ dans $B$ par $A \subseteq B$. Ceci signifie que tout élément de $A$ est
aussi un élément de $B$. On dit que $A$ est un sous-ensemble ou une partie de $B$

<b class='important'>Egalité $=$</b>
L'égalité de deux ensembles est bien définie. On écrit $A = B$ lorsque $A \subseteq B$ et
$B \subseteq A$. Autrement dit, $A$ et $B$ sont égaux lorsque tout élément de $A$ est aussi dans
$B$ et, inversement, tout élément de $B$ appartient également à $A$.

---

## Relations ensemblistes

### **Définitions**

Soient $A$ et $B$ deux ensembles.

<b class='important'>Union $\cup$</b>
L'union de $A$ et de $B$, notée $A \cup B$, est l'ensemble qui contient à la fois les éléments
de $A$ et de $B$. On a donc $A \cup B = \left\{x \mid x \in A\ ou\ x \in B\right\}$

<b class='important'>Intersection $\cap$</b>
L'intersection de $A$ et de $B$, notée $A \cap B$, est l'ensemble qui contient les éléments qui appartiennent à la fois à A et à B. On a donc $A \cap B = \left\{x \mid x ∈ A\ et\ x ∈ B\right\}$

<b class='important'>La différence $\setminus$ </b>
La différence de deux ensembles $A$ et $B$ (on dit aussi "A moins B"), notée $A \ B$, est l'ensemble qui contient les éléments de A n'appartenant pas à B. On a donc $A \ B = \left\{x \mid x ∈ A\ et\ x /∈ B\right\}$

<b class='important'>L'ensemble des parties</b>
L'ensemble des parties d'un ensemble $A$, noté $P(A)$, est l'ensemble de toutes les
parties de $A$ : $P(A) = \left\{ B : B \subseteq A \right\}$

---

## Relations ensemblistes

### **Propriétés**

Soit $X$ un ensemble et soient $A, B, C ∈ P(X)$. Alors

1. $A \cap B = B \cap A$
2. $A \cup B=B \cup A$
3. $X \setminus (A \cap B) = (X \setminus A) \cup (X \setminus B)$
4. $X \setminus (A \cup B) = (X \setminus A) \cap (X \setminus B)$
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

<span style="display: inline-block; width:14rem;">$a  \equiv  b\ (mod\ N )$ </span>$a$ est congru à $b$ modulo $N$ </span>

---

## Divisibilité

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Définition - Divisibilité</b>
</div>

On dit que $a$ est un **diviseur** de $b$ (et on note $a \mid b$) si le reste de la division euclidienne de $b$ par $a$ est nul (égal à 0). On a donc : $b = a \times q$

On dit alors que $a$ **divise** $b$, que _b_ est **divisible** par $a$ ou que $b$ est un **multiple** de $a$.

</div>
<div class='block'>
<div class='block-icon'>
<i class='fas fa-info' style='padding-right:1rem;'></i>
<b>Critère de divisibilité</b>
</div>

Un nombre entier est divisible par :

- 2 lorsque son chiffre des unités est 0, 2, 4, 6 ou 8
- 3 lorsque la somme de ses chiffres est divisible par 3
- 4 lorsque le nombre formé par ses deux derniers chiffres est divisible par 4
- 5 lorsque son chiffre des unités est 0 ou 5
- 9 lorsque la somme de ses chiffres est divisible par 9
- 10 lorsque son chiffre des unités est 0

</div>

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
si $5x + 4y$ l'est.

<!-- Solution : Supposons que 7 divise 2x + 3y, alors il divise 6 (2x + 3y) − 7 (x + 2y) = 5x + 4y.
R´eciproquement si 7 divise 5x + 4y, il divise 6 (5x + 4y) − 7 (4x + 3y) = 2x + 3y. -->

**Exercice 3 :** Pour quels entiers $n$ strictement positifs, le nombre $n^2 + 1$ divise-t-il $n + 1$ ?

<!-- Solution : Si n2 + 1 divise n + 1, comme tout est positif, on doit avoir n2 + 1 6 n + 1, ce qui
n'est v´erifi´e que pour n = 1. On v´erifie ensuite que n = 1 est bien solution. -->

---

## Parties entières

### **Définitions**

<div class='block note'>
<div class='block-icon'>
    <i class='far fa-heart' style="padding-right:1rem;"></i>
    <b>Définition - Partie entière</b>
</div>

<!-- # Définition II.1 : Partie entière -->

Si $x$ est un réel, on appelle **partie entière** de $x$, et on note $\lfloor x \rfloor$, le plus grand entier inférieur ou égal à $x$.

Ainsi, on a $\lfloor x \rfloor \le x < \lfloor x \rfloor + 1$.

</div>

<div class='block'>
<div class='block-icon'>
    <i class='fas fa-info' style="padding-right:1rem;"></i>
    <b>Remarque</b>
</div>

On définit aussi la **partie décimale** de $x$, comme la différence $x − \lfloor x \rfloor$.

</div>

---

## Parties entières

### **Propriétés**

1. Pour tout réel $x$, on a $x − 1 < \lfloor x \rfloor \le x$
1. $\lfloor -x \rfloor = −\lfloor x \rfloor − 1$ sauf si $x$ est entier, auquel cas $\lfloor -x \rfloor = −\lfloor x \rfloor$.
1. Si $x$ et $y$ sont deux réels, $\lfloor x \rfloor + \lfloor y \rfloor \le \lfloor x + y\rfloor \le \lfloor x \rfloor + \lfloor y \rfloor + 1$.
1. Si $m > 0$ est un entier, alors il y a exactement $\lfloor \frac{x}{m} \rfloor$ multiples de $m$ compris entre 1 et $x$.

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

Soient $a, b \in \mathbb{Z^*}$. L'ensemble des diviseurs communs de $a$ et de $b$ est fini et non vide.

Il possède donc un plus grand élément appelé **plus grand commun diviseur (PGCD)** de $a$ et $b$ et noté $PGCD(a, b)$.

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

Soient $a, b \in \mathbb{Z^*}$. L'ensemble des diviseurs communs de $a$ et de $b$ est fini et non vide.

$a$ et $b$ possèdent un plus petit multiple commun positif, on l'appelle le **plus petit commun multiple (PPCM)** de $a$ et de $b$ et on le note $PPCM(a, b)$.

</div>

---

## PGCD / PPCM

### **Propriétés**

1. Si $d = PGCD(a, b)$, alors $n$ divise $a$ et $b$ si et seulement si $n$ divise $d$.
1. Si $m = PPCM (a, b)$, alors $n$ est un multiple $a$ et de $b$ si et seulement si $n$ est un multiple de $m$.
1. Si $a$, $b$ et $n$ sont des entiers non nuls et $n > 0$, alors $PGCD(na, nb) = nPGCD (a, b)$.
   Si de plus $n$ divise $a$ et $b$, alors $PGCD(\frac{a}{n}, \frac{b}{n}) = \frac{1}{n} PGCD(a, b)$.
1. Si $d = PGCD(a, b)$, on peut écrire $a = da'$ et $b = db'$ pour $a'$ et $b'$ des nombres premiers entre eux.
1. Si $a$ et $b$ sont des entiers, l'égalité $PGCD(a, b) = PGCD(a, a + b)$ est toujours vérifiée lorsqu'elle a un sens. En particulier, le PGCD de deux nombres consécutifs est $1$, et plus généralement, le PGCD de $a$ et de $a + n$ est un diviseur positif de $n$.
1. Plus généralement, si $x$, $y$, $a$, $b$, $a'$ et $b'$ sont des entiers alors :
   $$
   PGCD(x, y) \times | PGCD(ax + by, a'x + b'y) | \times (ab' − ba'
   ) PGCD(x, y)
   $$
   En particulier si $|ab' − ba'| = 1$, alors $PGCD(x, y) = PGCD(ax + by, a'x + b'y)$.

---

## PGCD / PPCM

### **Exercices**

**Exercice 0 :** Déterminer les valeurs suivantes: $PGCD(20, 36)$, $PGCD(36, 60)$ et $PGCD(116, 78)$

**Exercice 1 :** Démontrez les propriétés (1), ...

**Exercice 2 :** Soit $a, b \in \mathbb{Z^*}$. Montrez que $\forall n \in \mathbb{N^*}$, on a $PGCD(a^n, b^n) = PGCD(a, b)^n$

**Exercice 3 (Théorème de Bézout) :** Si $a$ et $b$ sont des entiers premiers entre eux, alors il existe des entiers $u$ et $v$ tels que $au + bv = 1$.

**Exercice 4 (Lemme de Gauss) :** Si des entiers $a$, $b$ et $c$ sont tels que $a$ divise $bc$ et $a$ premier avec $b$, alors $a$ divise $c$

---

## Nombres premiers

### **Définitions**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i><b>Définition - Nombre premier</b>
</div>

Un nombre entier positif est **premier** s'il admet **exactement deux diviseurs : 1 et lui-même**.

</div>

Les entiers $2$, $3$, $5$, $7$, $11$, $13$ sont les premiers nombres premiers.
Le nombre $6$, n'est pas premier: il admet 2 et 3 comme autres diviseurs

<div class='block warning'>
<div class='block-icon'>
<i class='fas fa-exclamation-triangle' style='padding-right:1rem;'></i>
<b>Remarques</b>
</div>

<i class='fas fa-arrow-right'></i> **0 n'est pas premier** car il admet **une infinité de diviseurs**.

<i class='fas fa-arrow-right'></i> **1 n'est pas premier** car il possède **un seul diviseur** : lui-même.

<i class='fas fa-arrow-right'></i> 2 est le seul nombre premier pair car tous les nombres pairs sont divisibles par 2.

</div>

---

## Nombres premiers

### **Propriétés**

1. Il existe une infinité de nombres premiers.

---

## Décomposition en facteurs premiers

### **Théorème**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Théorème - Décomposition en facteurs premiers</b>
</div>

Tout entier $n > 1$ se décompose d'une seule et unique manière en un produit de nombres premiers.

Autrement dit, pour tout entier $n > 1$, il existe des nombres premiers deux à deux distincts $p_1, . . . , p_k$ et des entiers strictement positifs $\alpha_1, . . . , \alpha_k$, tels que :

$$n = p_{1}^{\alpha_1}p_{2}^{\alpha_2} ... p_{k}^{\alpha_k}$$

</div>

Le théorème reste bien vrai pour $n = 1$.
Pour cela on remarquera que $p_{1}^{\alpha_1}p_{2}^{\alpha_2} ... p_{k}^{\alpha_k} = 1 \times p_{1}^{\alpha_1}p_{2}^{\alpha_2} ... p_{k}^{\alpha_k}$ et on choisira $k = 0$.

---

## Décomposition en facteurs premiers

### **Exemples**

**Exemple 1**: Décomposer $84$ en produits de facteurs premiers.

<!-- $$\begin{aligned} 84 &= 42 \times 2 \\
&= 21 \times 2 \times 2 \ (car\ 42 = 21 \times 2)\\
&= 7 \times 3 \times 2 \times 2 \ (car\ 21 = 7 \times 3) \\
&= 2^2 \times 3 \times 7 \\
\end{aligned}$$ -->

</br>
</br>
</br>
</br>

**Exemple 2**: Décomposer $2520$ en produits de facteurs premiers.

---

## Décomposition en facteurs premiers

<div class='block'>
<div class='block-icon'>
Proposition
</div>

Si la décomposition en facteurs premiers de l'entier $n \ge 1$ est $n=p_1^{\alpha_1}p_2^{\alpha_2}...p_k^{\alpha_k}$, alors les diviseurs positifs de $n$ sont les entiers de la forme $p_1^{\beta_1}p_2^{\beta_2}...p_k^{\beta_k}$, avec $0 \le \beta_i \le \alpha_i$ pour tout $0 \le i \le k$

</div>

Par conséquence, soient $a$ et $b$ tels que:
$$a=p_1^{\alpha_1}p_2^{\alpha_2}...p_k^{\alpha_k}\ \ \ et \ \ \ b = p_1^{\beta_1}p_2^{\beta_2}...p_k^{\beta_k}$$

où les $p_i$ sont deux à deux distincts, mais les $\alpha_i$ et $\beta_i$ sont éventuellement nuls, on a:

$$(i)\ PGCD(a,b) = p_1^{\min(\alpha_1, \beta_1)}p_2^{\min(\alpha_2, \beta_2)}...p_k^{\min(\alpha_k, \beta_k)}$$

$$(ii)\ PPCM(a,b) = p_1^{\max(\alpha_1, \beta_1)}p_2^{\max(\alpha_2, \beta_2)}...p_k^{\max(\alpha_k, \beta_k)}$$

---

## Décomposition en facteurs premiers

### **Exercices**

**Exercice :** Montrez que $PGCD(a,b) \times PPCM(a, b) = ab$

---

<!-- PARTIE 03 : Congruences -->

<div class='main'>

# 03

## Congruences

</div>

---

## Notation

<span style="display: inline-block; width:14rem;">$DIV(a, b)$ </span>quotient de la division euvlidienne de $a$ par $b$

<span style="display: inline-block; width:14rem;">$MOD(a, b)$ </span>reste (ou module) de la division euvlidienne de$a$ par $b$

<span style="display: inline-block; width:14rem;">$a = \overline{a_ka_{k-1}...a_1}^b$ </span>décomposition en base _b_ de $a$

<span style="display: inline-block; width:8rem;">$\equiv$ </span>a divise b

---

## Division euclidienne

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Théorème - Division euclidienne</b>
</div>

Soient $a \in \mathbb{Z}$ et $b \in \mathbb{Z^*}$. Alors $a$ se décompose de façon unique sous la forme:

$$a = bq + r,\ avec\ q \in \mathbb{Z}\ et\ r \in \left\{0, ..., |d| -1 \right\}$$

Les entiers $q$ et $r$ sont appelés respectivement **quotient** et **reste** de la division euclidienne de $a$ par $b$.

</div>

**Remarque :** Ainsi $a$ est divisible par $b$ si et seulement si $r = 0$.

**Démonstration :**

---

## Division entière et module

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Définition</b>
</div>

Soient $a \in \mathbb{Z}$ et $b \in \mathbb{Z^*}$. On note respectivement $DIV(a, b)$ et $MOD(a, b)$ le quotient et le reste de la division euclidienne de a par b.

</div>

---

## Décomposition en base **_b_**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Théorème - Décomposition en base <i>b</i></b>
</div>

Soit $b$ une base entière, c'est-à-dire un
naturel tel que $b \ge 2$. Alors tout entier $a \in \mathbb{N}^*$ se décompose de façon unique
sous la forme:

$$a = a_0 + a_1b + a_2b^2+...+a_kb^k$$

où $k$ est un entier, les $a_i$ sont des entiers compris entre $0$ et $b − 1$ et où $a_k \neq 0$.

</div>

**Notation :** On notera $a = \overline{a_k a_{k−1} ... a_0}^b$, l'écriture en base _b_ de $a$

**Exemples :**
$4 = \overline{100}^2 = \overline{11}^3 = \overline{4}^5 = \overline{4}^{10}$
$7 = \overline{111}^2 = \overline{21}^3 = \overline{12}^5 = \overline{7}^{10}$

---

## Tableau des bases classiques

<div class='flex-horizontal'><div class='flex'>

| b=10 (décimale) | b=2 (binaire) | b=3 (ternaire) | b=8 (octale) | b=16 (hexadécimale) |
| :-------------: | :-----------: | :------------: | :----------: | :-----------------: |
|        0        |       0       |       0        |      0       |          0          |
|        1        |       1       |       1        |      1       |          1          |
|        2        |      10       |       2        |      2       |          2          |
|        3        |      11       |       10       |      3       |          3          |
|        4        |      100      |       11       |      4       |          4          |
|        5        |      101      |       12       |      5       |          5          |
|        6        |      110      |       20       |      6       |          6          |
|        7        |      111      |       21       |      7       |          7          |
|        8        |     1000      |       22       |      10      |          8          |
|        9        |     1001      |      100       |      11      |          9          |
|       10        |     1010      |      101       |      12      |          A          |
|       11        |     1011      |      102       |      13      |          B          |

</div><div class='flex'>

</div></div>

---

## Tableau des bases classiques (suite)

<div class='flex-horizontal'><div class='flex'>

| b=10 (décimale) | b=2 (binaire) | b=3 (ternaire) | b=8 (octale) | b=16 (hexadécimale) |
| :-------------: | :-----------: | :------------: | :----------: | :-----------------: |
|       12        |     1100      |      110       |      14      |          C          |
|       13        |     1101      |      111       |      15      |          D          |
|       14        |     1110      |      112       |      16      |          E          |
|       15        |     1111      |      120       |      17      |          F          |
|       16        |     10000     |      121       |      20      |         10          |
|       17        |     10001     |      122       |      21      |         11          |
|       18        |     10010     |      200       |      22      |         12          |
|       19        |     10011     |      201       |      23      |         13          |
|       20        |     10100     |      202       |      24      |         14          |
|       ...       |      ...      |      ...       |     ...      |         ...         |
|       100       |    1100100    |     10201      |     144      |         64          |
|      1000       |  1111101000   |    1101001     |     1750     |         3E8         |

</div><div class='flex'>

</div></div>

---

## Décomposition en base _b_

**Proposition 1 :** Soit $n, b \in \mathbb{N}^*$ avec $b \ge 2$. Le nombre de chiffres de la représentation de $n$ en base $b$ est égal à $\lfloor \log_b(n)\rfloor + 1$.

**Démonstration :**

---

## Décomposition en base _b_

### **Exercices**

<b class='important'>Division euclidienne</b>
**Exercice :** Démontrez les propriétés (1), ...

<b class='important'>Congruences</b>
**Exercice :** Démontrez les propriétés (1), ...

---

## Congruences

### **Avant propos**

---

## Congruences

### **Définitions**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Définition - Congruence</b>
</div>

Soit $n \in \mathbb{N}^*$.
On dit que deux nombres entiers $a,b \in \mathbb{Z}$ $a$ et $b$ sont **congrus modulo $n$** ($n \in \mathbb{N}^*$) si et seulement si $a − b$ est divisible par $n$.

On note $a \equiv b \left[n\right]$.

</div>

**Propriétés**

1. $a \equiv 0[n] \Leftrightarrow$ $n$ divise $a$
1. $a \equiv b[n] \Leftrightarrow$ $a$ et $b$ ont le même reste dans la division euclidienne par $n$
1. Si $a \equiv b[n]$ et $b \equiv c[n]$, alors $a \equiv c[n]

---

## Congruences

### **Propriétés**

Soient $a,a',b,b' \in \mathbb{Z}$ tels que $a \equiv a'[n]$ et $b \equiv b'[n]$.

Alors :

1. $a+b \equiv a'+b'[n]$ et $a−b \equiv a'−b'[n]$
1. $ab \equiv a'b'[n]$
1. $\forall k \in \mathbb{Z}, \text{on a } ka \equiv ka'[n]$
1. $r$ est le reste de la division euclidienne de $a$ par $a'$ si et seulement si :

$$
\begin{equation}
  \begin{cases}
    r \equiv a[a']\\
    r < |a'|
  \end{cases}
\end{equation}
$$

---

## Congruences

### **Exercices**

**Exercice :** Déterminez le reste de la division euclidienne de $2024^{2024}$ par $5$.

<!-- **Solution :**
$2024 \equiv -1[5]$ car $2024 - (-1) = 2025$ est divisible par $5$.
Donc $2024^{2024} \equiv (-1)^{2024}[5] \equiv 1[5]$
Or $−1 \equiv 4[5]$ donc $2009^{2009} \equiv 4[5]$
Comme $0 \le 4 < 5$, le reste de la division euclidienne de $2009^{2009}$ par 5 est 4. -->

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
