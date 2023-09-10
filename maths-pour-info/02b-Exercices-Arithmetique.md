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

**Exercice I.2**
...
...

**Exercice I.3** Soient $x$ et $y$ des entiers. Montrer que $2x + 3y$ est divisible par $7$ si et seulement si $5x + 4y$ l'est.

<!-- **Solution :** Supposons que 7 divise 2x + 3y, alors il divise 6 (2x + 3y) − 7 (x + 2y) = 5x + 4y.
Réciproquement si 7 divise 5x + 4y, il divise 6 (5x + 4y) − 7 (4x + 3y) = 2x + 3y. -->

**Exercice I.4 :** Pour quels entiers $n$ strictement positifs, le nombre $n^2 + 1$ divise-t-il $n + 1$ ?

<!-- **Solution :** Si $n^2 + 1$ divise $n + 1$, comme tout est positif, on doit avoir $n^2 + 1  \le n + 1$, ce qui n'est vérifié que pour $n = 1$. On vérifie ensuite que n = 1 est bien solution. -->

</br>

### _<u>Partie II: PGCD et nombres premiers (~2h00)</u>_

**Exercice II.1**
Donner la définition d'un nombre premier puis donner la liste des 20 premiers nombres premiers.

**Exercice II.2**
Les nombres suivants sont-ils premiers ? Justifier. $0, 1, 2, 3, 4, 91, 123$

**Exercice II.3**
Décomposer en produit de facteurs premiers les nombres suivants : $12, 17, 84,2520$

**Exercice II.4**
...

**Exercice II.5**
Trouver la fraction irréductible égale à $\frac{84}{30}$ et $\frac{2520}{77}$.

<!-- _Indice: on peut décomposer le numérateur et le dénominateur de la fraction en produit de facteurs premiers_ -->

**Exercice II.6**
Déterminer le PGCD de 4480 et 400 à l'aide de la décomposition en facteurs premiers.

</div><div class='flex'>

**Exercice II.7**
Déterminer le PGCD de 3045 et 300 à l'aide de l'algorithme d'Euclide.

**Exercice II.8**
Déterminer tous les diviseurs communs à $60$ et $100$.

**Exercice II.9**
Déterminer tous les diviseurs communs à $168$ et $204$.

**Exercice II.10**
Soient $a$ et $b$ des nombres premiers entre eux. Montrer que $ab$ et $a + b$ sont aussi premiers entre eux.

<!-- **Solution**
Soit $d$ un diviseur commun de $ab$ et de $a+b$. Alors $d$ divise $a (a + b)−ab = a^2$. De même $d$ divise $b^2$. Or on a $PGCD(a^2, b^2) = PGCD(a, b)^n = 1^n = 1$ car $a$ et $b$ sont premiers entre eux. Donc $d = ±1$ et donc $ab$ et $a+b$ sont premiers entre eux. -->

**Exercice II.11**
Déterminer l'ensemble des naturels $n$ tel que la fraction $\frac{3n + 2}{n+2}$ soit irréductible.

**Exercice II.12**
Soit $n$ un entier naturel.
Déterminer le PGCD de $9n + 4$ et de $2n+1$ par deux méthodes.

**Exercice II.13**
Soit $n$ un entier naturel.
Déterminer le PGCD de $n + 4$ et de $3n + 7$ par deux méthodes.

**Exercice II.14**
Trouvez les entiers naturels $a$ et $b$ avec $a < b$ tels que : $ab = 7776$ et $PGCD(a,b)=18$.

**Exercice II.15**
Trouvez les entiers naturels $a$ et $b$ tels que : $ab - b^2 = 2028$ et $PGCD(a,b)=13$.

**Exercice II.16**

1. Déterminer l'ensemble des entiers naturels $n$ tels que $PGCD(2n+3,n) = 3$.
2. En déduire l'ensemble des entiers naturels $n$ tels que $PGCD(2n+3,n)=1$

**Exercice II.17**
Si on divise $4294$ et $3521$ par un même entier naturel $n$, les restes respectifs sont $10$ et $11$. Quel est cet entier ?

**Exercice II.18**
Un boîte parallélépipédique rectangle de dimensions intérieures $31,2cm$, $13 cm$ et $7,8cm$ est entièrement remplie par des cubes à jouer dont l'arête est un nombre entier de millimètres. Quel est le nombre maximal de cubes que peut contenir cette boîte ?

</div></div>

---

<div class='flex-horizontal'><div class='flex'>

**Exercice II.19**
On pose $a=588$ et $b=616$.

1. Décomposer $a$ et $b$ en produits de facteurs premiers.
2. En déduire $PGCD(a,b)$
3. Déduire également de la première question $PPCM(a,b)$

**Exercice II.20 (l'algorithme d'Euclide)**
Soient $a$ et $b$ deux entiers naturels, on note $\mathcal{D}(a,b)$ l'ensemble des diviseurs communs à $a$ et $b$. Dans la suite, on considère que $a \ge b > 0$.

1. Montrer que $\mathcal{D}(a,b)=\mathcal{D}(a-b,b)$.
2. En déduire que $PGCD(a,b)=PGCD(a-b,b)$
3. Soit $r$ le reste dans la division euclidienne de $a$ par $b$. Montrer, en vous aidant de la question précédente, que $PGCD(a,b)=PGCD(r,b)$.
4. En vous aidant des divisions euclidiennes ci-dessous:  
   $$416 = 2 \times 182 + 52$$
   $$182 = 3 \times 52 + 26$$
   $$56 = 2 \times 26 + 0$$

   Déterminer $PGCD(416, 182)$

5. Ecrire en langage naturel un algorithme permettant de déterminer le $PGCD$ de $a$ et $b$.

**Exercice II.21 (Nombres de Fermat et infinitude des nombres premiers)**

On définit les **nombres de Fermat** comme étant les entiers $F_n = 2^{2^n}+1$ avec $n$ un entier naturel.

1. Etablir que pour tous entiers naturels $n$ et $k$, on a: $F_{n+k} = (F_n -1)^{2^k}$
2. En déduire que si $k$ est un entier naturel non nul alors pour tout entier naturel $n$, on a : $F_{n+k} \equiv 2 [F_n]$
3. En déduire que deux nombres de Fermat distincts sont premiers entre eux.
4. Retrouver alors qu'il existe une infinité de nombres premiers.

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

### _<u>Partie IV : Congruences (~1h30)</u>_

[ici](http://www.jaicompris.com/lycee/math/arithmetique/congruence-Z.php)

**Exercice IV.1**
Les propositions suivantes sont-elles vraies ?
$(a)\ 37≡4 [3]\ \ \ \ (b)\ 101≡1 [5]\ \ \ \ (c)\ −16≡0 [6]\ \ \ \ (d)\ −15≡6 [7]$

**Exercice IV.2**
Démontrer les propriétés de cours suivantes.

1. Démontrer que $a \equiv b \left[ n \right] \Leftrightarrow n\text{ divise }a-b$
2. Démontrer que (1) si dessus. (i.e. $a+a' \equiv b + b' \left[ n \right]$)

<!-- **Solution :**
$2024 \equiv -1[5]$ car $2024 - (-1) = 2025$ est divisible par $5$.
Donc $2024^{2024} \equiv (-1)^{2024}[5] \equiv 1[5]$
Or $−1 \equiv 4[5]$ donc $2009^{2009} \equiv 4[5]$
Comme $0 \le 4 < 5$, le reste de la division euclidienne de $2009^{2009}$ par 5 est 4. -->

**Exercice IV.3**
...
...

**Exercice IV.4**
Démontrer les propositions suivantes:
a. $\forall n \in \mathbb{N},\ n\left(n^2 + 11 \right)\text{ est divisible par }3$
b. $\forall n \in \mathbb{N},\ n^3 + 5n\text{ est divisible par }6$

**Exercice IV.5**
Déterminer le reste de la division euclidienne de $2024^{2024}$ par $5$.

**Exercice IV.7 :**
Démontrer que $a \equiv b \left[ n \right] \Leftrightarrow \text{a et b ont le meme reste dans la division euclidienne par n}$

**Exercice IV.8**
Démontrer que tout entier naturel $n$, $n(n+1)(2n+1)$ est divisible par $6$

**Exercice IV.9**
Démontrer que pour tout entier naturel $n$, $n^3-n$ est divisible par $2$ et par $3$

**Exercice IV.10**
Démontrer que pour tout entier naturel $n$ impair, $n^2−1$ est divisible par $8$

**Exercice IV.11**
Déterminer les entiers relatifs $n$ tels que $n−4$ divise $3n−17$.

</div><div class='flex'>

**Exercice IV.12**
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

**Exercice IV.13**

1. Montrer que tout entier naturel est congru modulo $9$ à la somme des chiffres de son écriture décimale.

2. En déduire que, quels que soient les entiers naturels $x= \overline{a_n...a_0}$, $y= \overline{b_m...b_0}$ et $z=\overline{c_p...c_0}$, si $xy=z$, alors $\left(\sum_{i=0}^{n}a_i\right)\left(\sum_{i=0}^{m}b_i\right) \equiv \left(\sum_{i=0}^{p}c_i\right) \left[9\right]$

**Exercice IV.14**
Une bande de 17 pirates possède un trésor constitué de pièces d'or d'égale valeur. Ils projettent de se les partager également, et de donner le reste au cuisinier chinois. Celui-ci recevrait alors 3 pièces. Mais les pirates se querellent, et six d'entre eux sont tués. Un nouveau partage donnerait au cuisinier 4 pièces. Dans un naufrage ultérieur, seuls le trésor, six pirates et le cuisinier sont sauvés, et le partage donnerait alors 5 pièces d'or à ce dernier. Quelle est la fortune minimale que peut espérer le cuisinier s'il décide d'empoisonner le reste des pirates ?

</div></div>
