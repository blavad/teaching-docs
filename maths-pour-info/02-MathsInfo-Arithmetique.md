---
marp: true
paginate: true

theme: dav-maths
title: Arithmétique modulaire

footer: "Arithmétique modulaire"
_footer: ""
math: mathjax
---

<!-- PAGE DE COUVERTURE -->
<!-- _paginate: skip -->
<!-- _class: cover -->
<div class='coverBlockCenter'><div class='coverModuleName'>Mathématiques pour l'informatique</div><div class='coverCourseName'><span class='important'>#2 </span>Arithmétique modulaire</div><div class='coverAuthor'>par <span class='important'>David Albert</span></div></div><img style="background-color:#ffffff" class='coverFooterLeft' height='60px' src='assets/img/logo-gema.png' /><div class='coverYear coverFooterRight'>2023</div>

---

<!-- TABLE DES MATIERES -->

## Table des matières

<b><span class='important'>00 </span> Notations </b>

<b><span class='important'>01 </span> Division euclidienne </b>
Division euclidienne. Divisibilité. Partie entière. PGCD / PPCM.

<b><span class='important'>02 </span> Nombres premiers </b>
Nombres premiers. Décomposition en facteurs premiers.

<b><span class='important'>03 </span> Décomposition en base _b_ </b>
Nombres binaires, ternaire, octale, décimale, hexadécimale.

<b><span class='important'>04 </span> Congruences</b>
Définition et propriétés.

<!-- FIN TABLE DES MATIERES -->

---

## **00** Notations

<!-- _class: bg2 -->

<span style="display: inline-block; width:8rem;">$a \mid b$ </span>a divise b

<span style="display: inline-block; width:8rem;">$\lfloor x \rfloor$ </span>partie entière de $x$

<!-- <span style="display: inline-block; width:8rem;">$\{x\}$ </span>partie décimale de $x$ -->

<!-- $\lceil x \rceil$ </span>partie entière de $x$ -->

<span style="display: inline-block; width:8rem;">$PGCD$ </span>plus grand diviseur commun </span>

<span style="display: inline-block; width:8rem;">$PPCM$ </span>plus petit multiple commun </span>

<span style="display: inline-block; width:14rem;">$a  \equiv  b\ (mod\ N )$ </span>$a$ est congru à $b$ modulo $N$ </span>

<span style="display: inline-block; width:14rem;">$DIV(a, b)$ </span>quotient de la division euvlidienne de $a$ par $b$

<span style="display: inline-block; width:14rem;">$MOD(a, b)$ </span>reste (ou module) de la division euvlidienne de$a$ par $b$

<span style="display: inline-block; width:14rem;">$a = \overline{a_ka_{k-1}...a_1}^b$ </span>décomposition en base _b_ de $a$

---

<!-- PARTIE 02 : Division euclidienne    -->

<div class='main'>

# 01

## Division euclidienne

</div>

---

## Division euclidienne

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Théorème - Division euclidienne</b>
</div>

Soient $a \in \mathbb{Z}$ et $b \in \mathbb{Z^*}$. Alors $a$ se décompose de façon unique sous la forme:

$$a = bq + r,\ avec\ q \in \mathbb{Z}\ et\ r \in \left\{0, ..., |d| -1 \right\}$$

Les entiers $q$ et $r$ sont appelés respectivement **quotient** et **reste** de la **division euclidienne** de $a$ par $b$.

</div>

<div class='block'>
<div class='block-icon'>
<i class='fas fa-edit' style='padding-right:1rem;'></i>
<b>Notation</b>
</div>

Soient $a \in \mathbb{Z}$ et $b \in \mathbb{Z^*}$. On note $DIV(a, b)$ (respectivement $MOD(a, b)$) le **quotient** (respectivement le **reste**) de la division euclidienne de a par b.

</div>

**Exemple :** Soient $a = 7$ et $b = 3$.

On a $\underbrace{7}_{a} = \underbrace{3}_{b} \times \underbrace{2}_{q} + \underbrace{1}_{r}$ l'unique décomposition de $a=7$ quand $b=3$.

---

## Divisibilité

<!-- _class: bg2 -->

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Définition - Divisibilité</b>
</div>

On dit que $b$ est un **diviseur** de $a$ (et on note $b \mid a$) si le reste de la division euclidienne de $a$ par $b$ est nul (égal à 0). On a donc : $a = b \times q$

On dit alors que $b$ **divise** $a$, que **$a$ est divisible par $b$** ou que **$a$ est un multiple de $b$**.

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
1. Si $a \mid b$, et $b \mid c$, alors $a \mid c$.
1. Si $a \mid b_1, b_2, ... , b_n$, alors $a \mid b_1c_1+b_2c_2+. . .+b_nc_n$, quels que soient les entiers $c_1, c_2, . . . , c_n$.
1. Si $a$ divise $b$ et $b \ne 0$, alors $|a| \le |b|$.
1. Si $a$ divise $b$ et $b$ divise $a$, alors $a = ±b$.
1. Si $a$ et b sont deux entiers tels que $a^n |b^n$ pour un entier $n > 1$, alors $a|b$.

---

## Divisibilité

### **Exercices**

Démontrez la propriété (3), (4) et (8).

<!-- (3) $\forall n \in \mathbb{Z},\ n = -1 \times (-n) = 1 \times n$ -->

<!-- (4) $a \mid b \Rightarrow a=bq\text{ avec }q \in \mathbb{Z}$ et $b \mid c \Rightarrow b=cq'\text{ avec }q' \in \mathbb{Z}$

Donc $a = bq = cq'q = cq''$ avec $q''=qq' \in \mathbb{Z}$ -->

<!-- (8) $a \mid b \Rightarrow a=bq\text{ avec }q \in \mathbb{Z}$

Donc $a^n = (bq)^n = \underbrace{bqbq...bq}_{\text{n fois}}=b^nq^n=b^nq'$ avec $q'=q^n \in \mathbb{Z}$ car $n > 1$. -->

---

## Parties entières

<!-- _class: bg2 -->

### **Définitions**

<div class='block note'>
<div class='block-icon'>
    <i class='far fa-heart' style="padding-right:1rem;"></i>
    <b>Définition - Partie entière</b>
</div>

<!-- # Définition II.1 : Partie entière -->

Si $x$ est un réel, on appelle **partie entière** de $x$, et on note $\lfloor x \rfloor$, le plus grand entier inférieur ou égal à $x$.

Mathématiquement, on a $\lfloor x \rfloor \le x < \lfloor x \rfloor + 1$.

</div>

<div class='block'>
<div class='block-icon'>
    <i class='fas fa-info' style="padding-right:1rem;"></i>
    <b>Remarque - Partie décimale</b>
</div>

On définit aussi la **partie décimale** de $x$, comme la différence $x − \lfloor x \rfloor$.

<!-- On notera parfois $\{x\} = x − \lfloor x \rfloor$ -->

</div>

**Exemples :**

- $\lfloor 2,5 \rfloor = 2$
- $\lfloor \pi \rfloor = 2$
- $\lfloor -1,632 \rfloor = -2$
- $\lfloor -\sqrt{19} \rfloor = -5$,

---

## Parties entières

### **Propriétés**

1. Pour tout réel $x$, on a $x − 1 < \lfloor x \rfloor \le x$.
1. $\lfloor -x \rfloor = −\lfloor x \rfloor − 1$ sauf si $x$ est entier, auquel cas $\lfloor -x \rfloor = −\lfloor x \rfloor$.
1. Si $x$ et $y$ sont deux réels, $\lfloor x \rfloor + \lfloor y \rfloor \le \lfloor x + y\rfloor \le \lfloor x \rfloor + \lfloor y \rfloor + 1$.
1. Si $m > 0$ est un entier, alors il y a exactement $\lfloor \frac{x}{m} \rfloor$ multiples de $m$ compris entre 1 et $x$.

---

## Parties entières

### **Exercices**

**Exercice 1 :** Démontrez les propriétés (1) et (3).

<!-- (1) Montrons que $x − 1 < \lfloor x \rfloor \le x$ pour tout réel $x$.

D'une part, $\lfloor x \rfloor \le x$ est vraie par application immédiate de la définition.
D'autre part, on a (par définition) $x < \lfloor x \rfloor + 1 \Leftrightarrow x-1 < \lfloor x \rfloor$. -->

<!-- (3) Montrons que si $x$ et $y$ sont deux réels, alors $\lfloor x \rfloor + \lfloor y \rfloor \le \lfloor x + y\rfloor \le \lfloor x \rfloor + \lfloor y \rfloor + 1$. -->

</br>
</br>
</br>
</br>
</br>
</br>

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

<!-- _class: bg2 -->

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

## Algorithme d'Euclide

L'algorithme d'Euclide est une méthode pour trouver pratiquement le PGCD de deux nombres sans avoir besoin de faire leur décomposition en produit de facteurs premiers. Il est basé sur la propriété suivante.

<div class='block note'>
<div class='block-icon'>
<i class='fas fa-info' style='padding-right:1rem;'></i>
<b>Proposition</b>
</div>

Si $a$ et $b$ sont deux entiers naturels avec par exemple $a≥b$, si $r$ est le reste de $a$ par $b$, alors le PGCD de $a$ et $b$ vaut le PGCD de $b$ et $r$.

</div>

On fait donc des divisions euclidiennes, jusqu'à ce qu'on trouve un reste nul. Le dernier reste non nul est le pgcd de a et b.

<div class='flex-horizontal'><div class='flex'>

**Exemple :** On souhaite calculer le PGCD de 255 et 141. On effectue les divisions euclidiennes successives suivantes :

</div><div class='flex'>

$255 =1 \times 141 + 114$
$142 =1 \times 114 + 27$
$114 =4 \times 27 + 6$
$27 =4 \times 6 + 3$
$6 =2 \times 3 + 0$

</div></div>

Le pgcd de 255 et 141 est donc 3.

---

## Algorithme d'Euclide

---

<!-- PARTIE 02 : Nombres premiers -->

<div class='main'>

# 02

## Nombres premiers

</div>

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

**Propriété :** Il existe une infinité de nombres premiers.

---

## Décomposition en facteurs premiers

### **Théorème**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Théorème - Décomposition en facteurs premiers</b>
</div>

Tout entier $n \ge 1$ se décompose d'une seule et unique manière en un produit de nombres premiers.

Autrement dit, pour tout entier $n \ge 1$, il existe des nombres premiers deux à deux distincts $p_1, . . . , p_k$ et des entiers strictement positifs $\alpha_1, . . . , \alpha_k$, tels que :

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

<!-- _class: bg2 -->

<div class='block'>
<div class='block-icon'>
Proposition
</div>

Si la décomposition en facteurs premiers de l'entier $n \ge 1$ est $n=p_1^{\alpha_1}p_2^{\alpha_2}...p_k^{\alpha_k}$, alors les diviseurs positifs de $n$ sont les entiers de la forme $p_1^{\beta_1}p_2^{\beta_2}...p_k^{\beta_k}$, avec $0 \le \beta_i \le \alpha_i$ pour tout $1 \le i \le k$

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

## Décomposition en base _b_

</div>

---

## Décomposition en base **_b_**

<!-- _class: bg2 -->

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

<div class='block'>
<div class='block-icon'>
<i class='fas fa-edit' style='padding-right:1rem;'></i>
<b>Notation</b>
</div>

On notera $a = \overline{a_k a_{k−1} ... a_0}^b$, l'écriture en base _b_ de $a$

</div>

<div class='flex-horizontal'><div class='flex'>

**Exemples :**
$4 = \overline{100}^2$ car $4 = \textbf{1}\times 2^2 + \textbf{0}\times 2^1 +\textbf{0}\times 2^0$
$4 = \overline{11}^3$ car $4 = \textbf{1}\times 3^1 + \textbf{1}\times 3^0$
$4 = \overline{4}^5$ car $4 = \textbf{4}\times 5^0$

</div><div class='flex'>

</br>

$7 = \overline{111}^2$ car $7 = \textbf{1}\times 2^2 + \textbf{1}\times 2^1 +\textbf{1}\times 2^0$
$7 = \overline{21}^3$ car $7 = \textbf{2}\times 3^1 + \textbf{1}\times 3^0$
$7 = \overline{12}^5$ car $7 = \textbf{1}\times 5^1 + \textbf{2}\times 5^0$

</div></div>

---

## Tableau des bases classiques

<!-- _class: bg2 -->

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

<!-- _class: bg2 -->

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

<!-- PARTIE 04 : Congruences -->

<div class='main'>

# 04

## Congruences

</div>

---

<div style="position: absolute; right:3rem;top:3rem;">

![height:250px](assets/img/Congruences-Calendrier.jpg)

</div>

## Congruences

### **Avant propos**

<div class='flex-horizontal'><div class='flex' style='flex:0.65'>

Nous avons tous déjà utiliser les congruences sans le savoir.

Imaginons que l'on n'a pas de calendrier sous les yeux. **Sachant qu'aujourd'hui nous sommes mardi 5, comment savoir savoir quel jour seront nous le 28 ?**

</div><div class='flex' style='flex:0.35'>

</div></div>

Nous savons qu'une semaine est composée de 7 jours donc:

$Mardi\ 5 \xrightarrow[]{\ \ \ +7\ \ \ } Mardi\ 12 \xrightarrow[]{\ \ \ +7\ \ \ } Mardi\ 19 \xrightarrow[]{\ \ \ +7\ \ \ } Mardi\ 26 \xrightarrow[]{\ \ \ +1\ \ \ }Mercredi\ 27 \xrightarrow[]{\ \ \ +1\ \ \ }Jeudi\ 28$

En faisant cela, on fait des congruences.

<div class='block warning no-icon'>

On dira que **$5$ est congru à $26$ modulo $7$** et on notera $5 \equiv 26[7]$.

<i class='fas fa-warning'></i> $a \equiv b[7]$ signifie que $b = a + 7k$

</div>

---

## Congruences

### **Définitions**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Définition - Congruence</b>
</div>

Soient $n \in \mathbb{N}^*\text{ et }a,b \in \mathbb{Z}$.
On dit **$a$ et $b$ sont congrus modulo $n$** si et seulement si $\exists k \in \mathbb{N}$ tel que $a = b + nk$.
On notera $a \equiv b \left[n\right]$.

D'autre part,

$$
\begin{equation}
  \begin{split}
    a \equiv b\left[n\right] &\Longleftrightarrow \exists k \in \mathbb{N}; b = a + nk \\
    &\Longleftrightarrow n\text{ divise }a - b \\
    &\Longleftrightarrow  \text{a et b ont le meme reste dans la division euclidienne par n}
  \end{split}
\end{equation}
$$

</div>

---

## Congruences

### **Propriétés**

Soit $n \in \mathbb{N}^*$, $a,b \in \mathbb{Z}$

1. $a \equiv a\left[ n \right]$
1. $n \equiv 0\left[ n \right]$
1. $a \equiv b\left[ n \right] \Leftrightarrow b \equiv a\left[ n \right]$
1. $a \equiv 0\left[ n \right] \Leftrightarrow$ $n$ divise $a$
1. Si $a \equiv b\left[ n \right]$ et $b \equiv c\left[ n \right]$, alors $a \equiv c\left[ n \right]$
1. $r$ est le reste de la division euclidienne de $a$ par $b$ si et seulement si :

$$
\begin{equation}
  \begin{cases}
    a \equiv r\left[b\right]\\
    r < |b|
  \end{cases}
\end{equation}
$$

---

## Congruences

### **Opérations sur les congruences**

Soient $a,b,a',b' \in \mathbb{Z}$ tels que $a \equiv b\left[ n \right]$ et $a' \equiv b'\left[ n \right]$.

Alors :

1. $a+a' \equiv b + b' \left[ n \right]$
1. $a−a' \equiv b−b'\left[ n \right]$
1. $a \times a' \equiv b \times b'\left[ n \right]$
1. $a^{p} \equiv b^{p}\left[ n \right],\ \forall p \in \mathbb{N}$

Conséquences immédiates:

5. $a + k \equiv b + k\left[ n \right],\ \forall k \in \mathbb{Z}$
6. $a - k \equiv b - k\left[ n \right],\ \forall k \in \mathbb{Z}$
7. $a \times k \equiv b \times k\left[ n \right],\ \forall k \in \mathbb{Z}$

<i class='info'>(vous pouvez vous amuser à redémontrer toutes ces propriétés)</i>

---

## Congruences

<!-- _class: bg2 -->

### **Astuces de calcul**

</hr>

**Astuce 1 :** <i class='important'>Multiplier au fur et à mesure en simplifiant à chaque fois</i>

_Exemple :_ Soit $a \in \mathbb{Z},\ a \equiv 34\left[ 6\right]$. A quoi est congru $22a$ modulo $6$ ?

</br>
</br>
</hr>

**Astuce 2 :** <i class='important'>Aller dans les négatifs.</i>

_Exemple :_ Soit $a \in \mathbb{Z},\ a \equiv 10\left[ 11\right]$. A quoi est congru $a^{14}$ modulo $11$ ?

</br>
</br>
</hr>

**Astuce 3 :** : <i class='important'>Trouver une puissance congrue à $1$ ou $-1$</i>

_Exemple :_ On veut savoir le reste dans la division euclidienne de $2^{1495}$ par $15$.

---

## Congruences

<!-- _class: bg2 -->

### **Théorème des restes chinois**

<b>Théorème des restes chinois</b>
Soient $n_1, n_2, ... , n_k$ des entiers strictement positifs deux à deux premiers entre eux, et $a_1, a_2, ... , a_k$ des entiers quelconques. Le système d'équations :

$$
\begin{equation}
  \begin{cases}
    x \equiv a_1\left[n_1\right]\\
    \ \vdots\ \ \ \vdots\ \ \ \vdots \\
    x \equiv a_k\left[n_k\right]\\
  \end{cases}
\end{equation}
$$

admet une unique solution modulo $N = n_1 \times ... \times n_k$ donnée par la formule :

$$x= a_1N_1y_1 + ... + x= a_kN_ky_k$$
où $N_i = \frac{N}{n_i}$ et $y_i \equiv \frac{1}{N_i}\left[n_i\right]$ pour $i$ compris entre $1$ et $k$.

---

## Congruences

<!-- _class: bg2 -->

### **Théorème des restes chinois (exemple)**

<b>Problème :</b> Soient des objets en nombre inconnu. Si on les range par 3 il en reste 2. Si on les range par 5, il en reste 3 et si on les range par 7, il en reste 2. Combien a-t-on d'objets ?

<b>Solution</b>

Si $x$ désigne le nombre d'objets total, alors $x$ est le plus petit entier positif tel que :

$$
\begin{equation}
  \begin{cases}
    x \equiv 2\left[3\right]\\
    x \equiv 3\left[5\right]\\
    x \equiv 2\left[7\right]\\
  \end{cases}
\end{equation}
$$

On applique le théorème chinois : on a $N = 3 \times 5 \times 7 = 105$, $N_1 = \frac{105}{3}=35$, $N_2 = \frac{105}{5} = 21$ et $N_3 = \frac{105}{7} = 15$. L'inversion de chaque $N_i$ modulo $n_i$ (par l'algorithme d'Euclide) donne $y_1 =70$, $y_2=21$ et $y_3=15$

Donc, $x \equiv 2\times 70+3\times 21+2\times 15  [105] \equiv 233 [105] \equiv 23 [105]$

Ainsi, le nombre d'objets est de la forme $23 + 105k$ avec $k \in \mathbb{N}$.
