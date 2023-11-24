---
marp: true
paginate: false

theme: dav-maths-exos
title: Arithmétique

footer: ""
_footer: ""
math: mathjax
---

<div class='flex-horizontal'><div class='flex'>

## **Arithmétique modulaire**

### Fiche d'exercices n°1

</br>

### _<u>Partie I: Divisibilité (~30min)</u>_

**Exercice I.1**
Construire un nombre divisible par $2$,$3$,$4$,$5$,$9$ et $10$ en se basant uniquement sur les critère de divisibilité.

<!-- **Solution**

- 2 160 est divisible par 2, par 5, par 10. En effet, le chiffre des unités est 0.
- 2 160 est divisible par 4. En effet, 60 est divisible par 4.
- 2 160 est divisible par 3 et 9. En effet, $2 + 1 + 6 + 0 = 9$ et 9 est divisible par 3 et par 9 -->

**Exercice I.2** Soient $x$ et $y$ des entiers. Montrer que $2x + 3y$ est divisible par $7$ si et seulement si $5x + 4y$ l'est.

<!-- **Solution :** Supposons que 7 divise 2x + 3y, alors il divise 6 (2x + 3y) − 7 (x + 2y) = 5x + 4y.
Réciproquement si 7 divise 5x + 4y, il divise 6 (5x + 4y) − 7 (4x + 3y) = 2x + 3y. -->

<!-- **Exercice I.3 :** Pour quels entiers $n$ strictement positifs, le nombre $n^2 + 1$ divise-t-il $n + 1$ ?

**Solution :** Si $n^2 + 1$ divise $n + 1$, comme tout est positif, on doit avoir $n^2 + 1  \le n + 1$, ce qui n'est vérifié que pour $n = 1$. On vérifie ensuite que n = 1 est bien solution. -->
<!--
**Exercice I.3**
Déterminer les entiers relatifs $n$ tels que $n−4$ divise $3n−17$. -->

<!-- **Solution :** Puisque $n−4 | 3n−17$ et que $n−4 | n−4$ alors $n−4$ divise toute combinaison linéaire de $3n-17$ et $n-4$.

Notamment, $n-4$ divise $(3n−17)−3(n−4)=−5$.

Or les diviseurs dans $\mathbb{Z}$ de $−5$ sont $−5,−1,1,5$.
Les valeurs possibles de $n−4$ sont donc ces valeurs, et donc on a n∈{−1,3,5,9}.

Réciproquement, si $n=−1$, alors $n−4=−5$ divise $3n−17=−20$.
Si $n=3$, $n−4=−1$ divise $3n−17=−8$.
Si $n=5$, $n−4=1$ divise $3n−17=−2$.
Si $n=9$, $n−4=5$ divise $3n−17=10$.

En conclusion, les valeurs de $n$ qui conviennent sont $−1,3,5\ et\ 9$. -->

</br>

### _<u>Partie II: PGCD et nombres premiers (~2h30)</u>_

**Exercice II.1**
Donner la définition d'un nombre premier puis donner la liste des 20 premiers nombres premiers.

**Exercice II.2**
Les nombres suivants sont-ils premiers ? Justifier. $0, 1, 2, 3, 4, 91, 123$

**Exercice II.3**
Décomposer en produit de facteurs premiers les nombres suivants : $12, 17, 84,2520$

**Exercice II.4**
Trouver la fraction irréductible égale à $\frac{84}{30}$ et $\frac{2520}{77}$.

<!-- _Indice: on peut décomposer le numérateur et le dénominateur de la fraction en produit de facteurs premiers_ -->

**Exercice II.5**
Déterminer le PGCD de $4480$ et $400$ à l'aide de la décomposition en facteurs premiers.

**Exercice II.6**
Déterminer le PGCD de $3045$ et $300$ à l'aide de l'algorithme d'Euclide.

**Exercice II.7**
Déterminer tous les diviseurs communs à $60$ et $100$.
<i class='info'>Indice: On pourra utiliser la décomposition en facteurs premiers</i>

**Exercice II.7 (bis)**
Déterminer tous les diviseurs communs à $168$ et $204$.

</div><div class='flex'>

**Exercice II.8**
Déterminer le PGCD de $621$ et $50$ à l'aide de l'algorithme d'Euclide.

**Exercice II.9**
Déterminer le PGCD de $1056$ et $140$ à l'aide de l'algorithme d'Euclide.

<!-- **Exercice II.8**
Soit $a, b \in \mathbb{Z^*}$. Montrez que $\forall n \in \mathbb{N^*}$, on a $PGCD(a^n, b^n) = PGCD(a, b)^n$

**Exercice II.9**
Soient $a$ et $b$ des nombres premiers entre eux. Montrer que $ab$ et $a + b$ sont aussi premiers entre eux. -->

<!-- **Solution**
Soit $d$ un diviseur commun de $ab$ et de $a+b$. Alors $d$ divise $a (a + b)−ab = a^2$. De même $d$ divise $b^2$. Or on a $PGCD(a^2, b^2) = PGCD(a, b)^n = 1^n = 1$ car $a$ et $b$ sont premiers entre eux. Donc $d = ±1$ et donc $ab$ et $a+b$ sont premiers entre eux. -->

<!-- **Exercice II.10**
Montrez que $PGCD(a,b) \times PPCM(a, b) = ab$.
<i class='info'>Indice: On pourra utiliser les réécritures du cours slide 20.</i> -->

</hr>

**Propriété très utile pour la suite :**

<div class='block note'>

$PGCD(a, b) = PGCD(a, b - ka)$

</div>

**Exercice II.11**
Soit $n$ un entier naturel.
Déterminer le PGCD de $9n + 4$ et de $2n+1$.

**Exercice II.12**
Soit $n$ un entier naturel.
Déterminer le PGCD de $n + 4$ et de $3n + 7$.

**Exercice II.13**
Déterminer l'ensemble des naturels $n$ tel que la fraction $\frac{3n + 2}{n+2}$ soit irréductible.

**Exercice II.14**
Trouvez les entiers naturels $a$ et $b$ avec $a < b$ tels que : $ab = 7776$ et $PGCD(a,b)=18$.

**Exercice II.15 (facultatif)**
Trouvez les entiers naturels $a$ et $b$ tels que : $ab - b^2 = 2028$ et $PGCD(a,b)=13$.

**Exercice II.16 (facultatif)**

1. Déterminer l'ensemble des entiers naturels $n$ tels que $PGCD(2n+3,n) = 3$.
2. En déduire l'ensemble des entiers naturels $n$ tels que $PGCD(2n+3,n)=1$

**Exercice II.17**
Si on divise $4294$ et $3521$ par un même entier naturel $n$, les restes respectifs sont $10$ et $11$. Quel est cet entier ?

**Exercice II.18**
Un boîte parallélépipédique rectangle de dimensions intérieures $31,2cm$, $13 cm$ et $7,8cm$ est entièrement remplie par des cubes à jouer dont l'arête est un nombre entier de millimètres. Quel est le nombre minimal de cubes que peut contenir cette boîte ?

</div></div>

---

<div class='flex-horizontal'><div class='flex'>

**Exercice II.19 (facultatif)**
On pose $a=588$ et $b=616$.

1. Décomposer $a$ et $b$ en produits de facteurs premiers.
2. En déduire $PGCD(a,b)$
3. Déduire également de la première question $PPCM(a,b)$

**Exercice II.20 - l'algorithme d'Euclide (facultatif)**
Soient $a$ et $b$ deux entiers naturels, on note $\mathcal{D}(a,b)$ l'ensemble des diviseurs communs à $a$ et $b$. Dans la suite, on considère que $a \ge b > 0$.

1. Donner $\mathcal{D}(120,24)$.
1. Montrer que $\mathcal{D}(a,b)=\mathcal{D}(a-b,b)$.
1. En déduire que $PGCD(a,b)=PGCD(a-b,b)$
1. Soit $r$ le reste dans la division euclidienne de $a$ par $b$. Montrer, en vous aidant de la question précédente, que $PGCD(a,b)=PGCD(r,b)$.
1. En vous aidant des divisions euclidiennes ci-dessous:  
   $$416 = 2 \times 182 + 52$$
   $$182 = 3 \times 52 + 26$$
   $$56 = 2 \times 26 + 0$$

   Déterminer $PGCD(416, 182)$

1. Ecrire en langage naturel un algorithme permettant de déterminer le $PGCD$ de $a$ et $b$.

</div><div class='flex'>

### _<u>Partie III : Décomposition en base b (~30min)</u>_

**Exercice III.1**
Calculez les 10 premières puissances de 2.

**Exercice III.2**
Donnez les écritures des nombres entiers suivants dans la base binaire (_b=2_) : 5, 54, 127, 256, 501, 1010

**Exercice III.3**
Calculez les 5 premières puissances de 3.

**Exercice III.4**
Donnez les écritures des nombres entiers suivants dans la base ternaire (_b=3_): 54, 127, 256, 501, 1010

**Exercice III.5**
Calculez les 3 premières puissances de 16.

**Exercice III.6**
Donnez les écritures des nombres entiers suivants dans la base hexadécimale (_b=16_): 54, 127, 256, 501, 1010

</div></div>

---

<div class='flex-horizontal'><div class='flex'>

### _<u>Partie IV : Congruences (~2h30)</u>_

<!--
[ici](http://www.jaicompris.com/lycee/math/arithmetique/congruence-Z.php) -->

**Exercice IV.1**
Les propositions suivantes sont-elles vraies ?
$(a)\ 37≡4 [3]\ \ \ \ (b)\ 101≡1 [5]\ \ \ \ (c)\ −16≡0 [6]\ \ \ \ (d)\ −15≡6 [7]$

<!-- **Solution**
Vrai, Vrai, Faux, Vrai -->

**Exercice IV.2**
Simplifier les congruences suivantes:

1. $22 \equiv ? [2]$, $83 \equiv ? [2]$, $3125 \equiv ? [2]$
1. $33 \equiv ? [5]$, $3132 \equiv ? [5]$, $4729 \equiv ? [5]$
1. En déduire, $3132 + 4729 \equiv ? [5]$
1. $7^4 \equiv ? [10]$
1. En déduire le chiffre des unités (dans l'écriture décimale) de $7^{98}$ ?

**Exercice IV.3**
Trouvez les valeurs de $x$ tels que $x−4 \equiv 3[5]$.

**Exercice IV.4 (Pièges et erreurs classiques sur les congruences) :**
Indiquer si les affirmations suivantes sont vraies ou fausses, en justifiant:

1. $Si\ a \times b \equiv 0[6]\ alors\ a\ \equiv 0[6]\ ou\ b \equiv 0[6]$
1. $Si\ 2x \equiv 4[12]\ alors\ x \equiv 2[12]$
1. $Si\ 2x \equiv 4[12]\ alors\ x \equiv 2[6]$
1. $Si\ 7-x \equiv 5[3]\ alors\ x \equiv 2[3]$
1. $Pour\ tout\ entier\ x,\ x^5 \equiv x[4]$

**Exercice IV.5 (facultatif)**

1. Démontrer que $115 \equiv 27 [11]$ et que $-39 \equiv 27[11]$
2. Trouver un entier naturel $n$ inférieur à 100 qui vérifie :

$$

\begin{equation}
\begin{cases}
n \equiv 27[11]\\
n \equiv 4[7]
\end{cases}
\end{equation}


$$

3. Combien d'entiers naturels inférieurs à $1000$ sont congrus à $27$ modulo 11 ?

**Exercice IV.6 (facultatif)**
A l'aide des congruences, quel est le dernier chiffre dans l'écriture décimale de $3^{2023}$?

**Exercice IV.7**
Déterminer le reste de la division euclidienne de $2024^{2024}$ par $5$.

<!-- **Solution :**
$2024 \equiv -1[5]$ car $2024 - (-1) = 2025$ est divisible par $5$.
Donc $2024^{2024} \equiv (-1)^{2024}[5] \equiv 1[5]$
Or $−1 \equiv 4[5]$ donc $2024^{2024} \equiv 4[5]$
Comme $0 \le 4 < 5$, le reste de la division euclidienne de $2024^{2024}$ par 5 est 4. -->

</div><div class='flex'>

**Exercice IV.8 (facultatif)**
Démontrer les propriétés de cours suivantes.

1. Démontrer que $a \equiv b \left[ n \right] \Leftrightarrow n\text{ divise }a-b$
2. Démontrer la propriété de cours (1) (i.e. $a+a' \equiv b + b' \left[ n \right]$)

3. Démontrer la propriété de cours (3) (i.e. $a \times a' \equiv b \times b' \left[ n \right]$)

**Exercice IV.9**

1. Compléter la table des restes dans la congruence modulo 9 :
   | $x \equiv$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
   | :---------: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
   | $4x \equiv$ | | | | | | | | | |

1. Résoudre alors l'équation $4x \equiv 5[9]$

1. En remarquant que $4 \times 7 \equiv 1[9]$, résoudre sans utiliser de table des restes l'équation :
   $$7x \equiv 8[9]$$

1. Résoudre enfin l'équation $3x \equiv 6[9]$

**Exercice IV.10**
Démontrer les propositions suivantes:
a. $\forall n \in \mathbb{N},\ n\left(n^2 + 11 \right)\text{ est divisible par }3$
b. $\forall n \in \mathbb{N},\ n^3 + 5n\text{ est divisible par }6$
c. $\forall n \in \mathbb{N},\ n^3-n\text{ est divisible par 2 et par 3}$
d. $\forall n \in \mathbb{N},\ n(n+1)(2n+1)\text{ est divisible par 6}$

<!-- **Solution**
a) On sait que $a\mid b  \Leftrightarrow b \equiv 0[a]$

Donc $3 \mid n(n^2+11) \Leftrightarrow n(n^2 +11) \equiv 0[3]$

Soit $n \in \mathbb{Z}$, $11\equiv 2[3]$ donc $n(n^2 +11) \equiv n(n^2 +2)[3]$

On établit la table de congruences suivante:

|     $n[3]$     | $0$ |     $1$      |     $2$      |
| :------------: | :-: | :----------: | :----------: |
|   $n^2+2[3]$   | $2$ | $3 \equiv 0$ | $6 \equiv 0$ |
| $n(n^2 +2)[3]$ | $0$ |     $0$      |     $0$      |

Ainsi, $\forall n\in \mathbb{Z}\text{, on a } 3 \mid n(n^2+11)$. -->

**Exercice IV.11 (facultatif)**
Démontrer que pour tout entier naturel $n$ impair, $n^2−1$ est divisible par $8$

**Exercice IV.12**
On considère un entier naturel $a$ défini par son écriture décimale $a = \overline{a_na_{n-1}...a_1a_0}$ avec $a_n \neq 0$.
On a donc : $a = a_n \times 10^n + a_{n-1} \times 10^{n-1}+ ...+ a_1 \times 10 + a_0$

1. Montrer que l'entier a est divisible par 3 si et seulement si la somme de ses chiffres est divisible par 3.
1. Montrer que l'entier a est divisible par 9 si et seulement si la somme de ses chiffres est divisible par 9.
1. $8176312459102535214621$ est-il divisible par $3$ ? Par $9$ ?

</div></div>

---

<div class='flex-horizontal'><div class='flex'>

**Exercice IV.13**
Résoudre le système suivant, d'inconnue $x\in \mathbb{Z}$ :

<div style="width:100px">

$$

\begin{equation}
\begin{cases}
x \equiv 1[5]\\
x \equiv 2[11]
\end{cases}
\end{equation}


$$

</div>

**Exercice IV.14 (facultatif)**

Une bande de 17 pirates possède un trésor constitué de pièces d'or d'égale valeur. Ils projettent de se les partager également, et de donner le reste au cuisinier chinois. Celui-ci recevrait alors 3 pièces. Mais les pirates se querellent, et six d'entre eux sont tués. Un nouveau partage donnerait au cuisinier 4 pièces. Dans un naufrage ultérieur, seuls le trésor, six pirates et le cuisinier sont sauvés, et le partage donnerait alors 5 pièces d'or à ce dernier. Quelle est la fortune minimale que peut espérer le cuisinier s'il décide d'empoisonner le reste des pirates ?

**_Indice :_** Pour cet exercice, on se basera sur le théorème ci-dessous.

<div class='block note'>
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

</div>

</div><div class='flex'>

</div></div>
