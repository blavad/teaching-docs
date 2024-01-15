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

## **Probabilités & Statistiques**

### Fiche d'exercices n°1

</br>

### _<u>Partie I: Expériences alétoires</u>_

**Exercice I.1**
Pour les expériences aléatoires suivants, donner l'ensemble des résultats possibles (noté $\Omega$). <i class='important'><b>Note :</b> On appelle également cet ensemble l'<b>univers</b></i>

1. On lance une pièce et on regarde la face supérieure.

2. On lance deux dés (un rouge et un vert) et on regarde la face supérieure des deux dés.

3. La durée de vie d'une ampoule

4. On tire 3 cartes simultanément dans un jeu de 32 cartes.

<div class='block note'>
Evénement = une partie de l'univers

i.e $A \in \mathcal{P}(\Omega)$
i.e $A \subset \Omega$

</div>

**Exercice I.2**
En relation avec les expériences aléatoires précédentes, donner l'ensemble correspondant aux événements ci-dessous:

1. Soit $A_1 \subset \Omega_1$ tel que $A_1$ : "la face supérieure est pile"

2. Soit $A_2 \subset \Omega_2$ tel que $A_2$ : "les deux lancers ont un résultat pair"

3. Soit $A_3 \subset \Omega_3$ tel que $A_3$ : "la durée de vie de l'ampoule est inférieure ou égale à 2 ans"

4. Soit $A_4 \subset \Omega_4$ tel que $A_4$ : "obtenir 2 rois exactement"

</br>

</div><div class='flex'>

### Note de cours : Langage des événements

|    Ensemble     |                Evénements                 |
| :-------------: | :---------------------------------------: |
|    $\Omega$     |        Univers (Evénement certain)        |
|   $\emptyset$   |           événement impossible            |
|    $\bar{A}$    |         événement contraire de A          |
|     $\{a\}$     |           événement élémentaire           |
|   $A \cup B$    |    (A est réalisé) ou (B est réalisé)     |
|   $A \cap B$    |    (A est réalisé) et (B est réalisé)     |
| $A \setminus B$ | (A est réalisé) mais (B ne l'est réalisé) |

</br>

### _<u>Partie II: Dénombrement</u>_

<div class='block note'>

Soit $\mathbb{P}$ une loi de probabilité. Si $\mathbb{P}$ est uniforme sur $\Omega$ (i.e la probabilité de tous les événements élémentaires est la même) alors :
$$\mathbb{P}(A) = \frac{card\ A}{card\ \Omega} = \frac{\text{"nombre de cas favorables"}}{\text{"nombre de cas possibles"}}$$

</div>

**Exercice II.1**

1. Donner le cardinal des ensembles suivants : $A_1$, $\Omega_1$, $A_2$ et $\Omega_2$.
2. En déduire $\mathbb{P}(A_1)$ et $\mathbb{P}(A_2)$

**Exercice II.2 (Tirages successifs avec remise)**

1. Une urne contient 8 boules numérotées de 1 à 8. On en tire successivement 3, en notant après chaque tirage le numéro obtenu puis en remettant la boule tirée dans l’urne avant le tirage suivant. Combien existe-t-il d'issues possibles ?
1. Même question avec $n$ boules numérotées de $1$ à $n$ et un tirage successif de $p$ boules.

</div></div>

---

<div class='flex-horizontal'><div class='flex'>

**Exercice II.3 (Tirages successifs sans remise)**

1. Une urne contient 8 boules numérotées de 1 à 8. On en tire successivement 3, en notant après chaque tirage le numéro obtenu et sans remettre la boule tirée dans l’urne avant le tirage suivant. Combien existe-t-il d'issues possibles ?
1. Même question avec $n$ boules numérotées de $1$ à $n$ et un tirage successif de $p$ boules.

<i class='important'>**Note :** C'est le nombre d'**arrangements** de $p$ éléments choisis parmi $n$. On le note $A^n_p$.</i>

**Exercice II.4 (Tirages simultanés)**

1. Une urne contient 8 boules numérotées de 1 à 8. On en tire simultanément 3 et on note la liste des boules tirées indépendamment de l'ordre de tirage. Combien existe-t-il d'issues possibles ?
1. Même question avec $n$ boules numérotées de $1$ à $n$ et un tirage simultané de $p$ boules.

<i class='important'>**Note :** C'est le nombre de **combinaisons** à $p$ éléments choisis parmi $n$ éléments. On le note ${n \choose p}$.</i>

**Exercice II.5**
De combien de façons peut-on garer ...

1. ... 4 voitures différentes sur un parking de 6 places numérotées ?
1. ... 5 voitures différentes sur un parking de 5 places numérotées ?

**Exercice II.6**
Combien de mots peut-on former avec toutes les lettres de

1. NICOLAS
1. MARINA
1. ANASTASIA

<b class='important'>Note : Attention aux répétitions !</b>

</div><div class='flex'>

### _<u>Partie III : Probabilités</u>_

<div class='block note'>
<b>Propriétés de cours</b>

$a)\ \mathbb{P}(\bar{A}) = 1 - \mathbb{P}(A)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ b)\ \mathbb{P}(\emptyset) = 0$
$c)\ \mathbb{P}(A \setminus B) = \mathbb{P}(A \cap \bar{B}) = \mathbb{P}(A) - \mathbb{P}(A \cap B)$
$d)\ \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$

</div>

**Exercice III.1**
Un commerçant propose des boissons sur un marché. Son réfrigérateur contient 30 bouteilles de thé glacé, 32 de jus d’ananas, 18 de soda et 40 d’eau gazeuse. Ces bouteilles sont de même forme. Le commerçant prélève au hasard une bouteille dans son réfrigérateur.

1. Déterminer la probabilité que cette bouteille soit une bouteille de soda.
1. Déterminer de deux façons différentes la probabilité que cette bouteille ne soit pas une bouteille de soda.

**Exercice III.2**
Un sac contient des papiers sur lesquels sont inscrits 1, 2, 3, 4, 5, 6. On tire au hasard un papier du sac et on note le nombre obtenu. Voici les probabilités de certaines issues:

|   Nombres    |  1   |  2  |  3  |  4  |  5   |  6  |
| :----------: | :--: | :-: | :-: | :-: | :--: | :-: |
| Probabilités | 0,05 | 0,1 |     | 0,2 | 0,25 | 0,3 |

1. Quelle est la probabilité manquante d'obtenir 3 ?
1. Donner la probabilité de chacun des événements:

   - $A_1$: "Obtenir un nombre multiple de 3"
   - $A_2$: "Obtenir 4 ou plus"
   - $A_3$: "Obtenir un nombre entier n tel que n⩽2 ou n⩾5"

**Exercice III.3**
Cécile a un jeu de 32 cartes. Elle dit à Mike de tirer 5 cartes au hasard et lui dit que si parmis ces cartes il y a exactement un as, elle lui laissera la part de gâteau.

1. Quelles sont les chances de Mike d'avoir la part de gâteau ?

2. Quelles auraient été les chances pour Mike de manger la dernière part de gâteau si la condition était de tirer au moins un as parmis les 5 cartes ?

</div></div>

---

<div class='flex-horizontal'><div class='flex'>

<div class='block note'>
<b>Rappel : Probabilités conditionnelles</b>

Soit $\Omega$ l'univers, $A \subset \Omega$ avec $\mathbb{P}(A) > 0$. On appelle **probabilité sachant $A$**, et on note $\mathbb{P}_A$, l'application :

$$
\begin{align}
\mathbb{P}_A :&\ \mathcal{P}(\Omega) \rightarrow [0, 1]\\
&\ B\ \ \ \longmapsto \ \mathbb{P}_A(B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(A)}
\end{align}
$$

</div>

**Exercice III.4**
Une société comprend 40% de cadres, 20% d'entre eux parlent anglais. Quelle est la probabilité qu'un employé au hasard soit un cadre qui parle anglais ?

**Exercice III.5**
En France, la proportion de gauchers est de 16%. On compte 3 gauchers hommes pour 2 gauchères. Quelle est la probabilité qu'un français choisi au hasard soit une gauchère?

**Exercice III.6**
Un joueur de tennis réussit sa première balle de service avec une probabilité de 0,7. S'il ne réussit pas sa première balle de service, il réussit sa seconde balle de service avec une probabilité de 0,9. On note les événements:

- $R_1$ : "Il réussit sa première balle de service. "
- $R_2$ : "Il réussit sa deuxième balle de service."

Représenter la situation par un arbre de probabilités.
Quelle est la probabilité qu'il commette une double faute?

**Exercice III.7**
$A$ et $B$ sont deux évènements tels que $\mathbb{P}(A)=0,4$ et $\mathbb{P}_A(B)=0,9$.
Déterminer $\mathbb{P}(A \setminus B)$.

**Exercice III.8**
$A$ et $B$ sont deux évènements tels que $\mathbb{P}(A)=0,4$, $\mathbb{P}_B(A)=0,2$ et $\mathbb{P}(A∪B)=0.8$.
Déterminer $\mathbb{P}(A∩B)$.

**Exercice III.9 (complémentaire)**
Une entreprise organise un dîner pour ceux de ses employés qui ont deux enfants dont au moins une fille. Chaque emplyé invité se présente au repas avec son ainé(e). M. Dupont a deux enfants. Quelle est la probabilité qu'il vienne avec son fils ?

</div><div class='flex'>

**Exercice III.10**
Une urne contient 12 boules numérotées de 1 à 12. On en tire une hasard, et on considère les événements

A="tirage d'un nombre pair"
B="tirage d'un multiple de 3"

Les événements A et B sont-ils indépendants?
Reprendre la question avec une urne contenant 13 boules.
<i class='important'>**Note :** Deux événements $A$ et $B$ sont indépendants $\Leftrightarrow \mathbb{P}(A \cap B) = \mathbb{P}(A) \times \mathbb{P}(B)$ </i>

**Exercice III.11**
Une population possède une proportion $p \in ]0,1[$ de tricheurs. On fait tirer une carte d'un jeu de 32 à un individu. On admet que si cet individu est un tricheur, il est sure de retourner un as.

1. Quelle est la probabilité qu'un individu choisi au hasard soit un tricheur sachant qu'il a retourné un as ?
1. Quel doit être la proportion minimale $p$ de tricheurs pour que la probabilité de l'événement précédent soit supérieur strictement à $\frac{8}{9}$ ?

<i class='info'>**Indice :** On pourra chercher $\mathbb{P}_A(T)$ avec $A$ et $T$ tels que suit :

- $A$ : "l'individu retourne un as"
- $T$ : "l'individu est un tricheur"

</i>

</div></div>

---

<div class='flex-horizontal'><div class='flex'>

### _<u>Partie IV : Variables aléatoires</u>_

**Exercice IV.1**
Un joueur lance successivement deux fois une pièce de monnaie. Soit $X$ la variable aléatoire égale au nombre de fois où la pièce est retombée sur face. Déterminer la loi de $X$, son espérance $E(X)$ et sa variance $V(X)$.

**Exercice IV.2**
Soit $X$ une variable aléatoire telle que $X(\Omega) = \{3,4,5,6\}$. On sait que $\mathbb{P}(X < 5) = \frac{1}{3}$, $\mathbb{P}(X > 5) = \frac{1}{2}$, $\mathbb{P}(X = 3) =\mathbb{P}(X = 4)$. Calculez $E(X)$ et $V(X)$.

**Exercice IV.3**
Une famille de dauphins comprend 5 femelles et 4 mâles. On choisit au hasard dans cette famille un groupe de 4 dauphins. Soit X la variable aléatoire représentant le nombre de femelles du groupe. Déterminer la loi de X puis son espérance.

**Exercice IV.4**
Un joueur lance successivement deux fois un dé équilibré. Soit $X$ la variable aléatoire égale à la différence entre les résultats du premier lancer et du deuxième lancer. Déterminer la loi de $X$, de $|X|$ et de $X^2$. Déterminer l'espérance de ces lois.

**Exercice IV.5**
On suppose que la V.A. $X$ vérifie :
$\forall n \in \mathbb{N}^*,\ \ \mathbb{P}(X \leq n) = 1 - (1 - p)^n$ où $p$ est un réel de $]0,1[$
Déterminer la loi de X.

**Exercice IV.6 (loi de Bernouilli)**
Soit une expérience aléatoire comportant deux issues, le succès ou l'échec. On note alors $p$ la probabilité du succès (par exemple obtenir pile avec une pièce truquée) et $1-p$ de l'échec.

Soit $\Omega = \{ succes, echec \}$, on peut définir une variable aléatoire $X$ prenant la valeur $1$ en cas de succès et $0$ en cas d'échec.

Calculez la loi de cette variable aléatoire, son espérance et sa variance.

<div class='block note'>
On dira que X suit une loi de Bernouilli de paramètre $p$ et on notera :

$X \sim Bernouilli(p)$

</div>

</div><div class='flex'>

**Exercice IV.7 (loi binomiale)**
Soit une expérience aléatoire comportant deux issues, le succès ou l'échec. On note alors $p$ la probabilité du succès et $1-p$ de l'échec et on répète $n$ fois cette expérience aléatoire.

On définit la variable aléatoire $X$ comme le nombre de succès obtenus.

Donnez la loi de cette variable aléatoire.

<div class='block note'>
On dira que X suit une loi de binomiale de paramètre $n$ et $p$ et on notera :

$X \sim B(n, p)$

</div>

<br/>

### _<u>Partie V : Statistiques</u>_

**Exercice V.1**
Donnez les formules de la moyenne, la variance et de l'écart-type.

**Exercice V.2**
Voici les notes de 15 étudiants : 1, 4, 5, 5, 6, 8, 10, 11, 11, 11, 12, 13, 15, 16, 19.

Donnez la moyenne, la médiane, la variance, l'écart-type ainsi que les 1er et 3ème quartiles de cette série de notes.

**Exercice V.3**
On a interrogé 21 élèves en leur demandant leur pointure. On a trié les résultats dans le tableau suivant :

| pointure | 35  | 36  | 38  | 39  | 40  |
| :------: | :-: | :-: | :-: | :-: | :-: |
| pointure |  1  |  5  | 10  |  3  |  2  |

On considère la série des pointures du groupe d'élèves interrogés.

Calculez la moyennne, la médiane et les 1er et 3ème quartiles de cette série de données.

</div></div>
