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

## **Théorie des ensembles**

### Fiche d'exercices n°1

</br>

### _<u>Partie I : Définition d'ensembles (~20min)</u>_

**Exercice I.1**
Définir l'ensemble des entiers naturels divisibles par $5$.

**Exercice I.2**

**Exercice I.3**

**Exercice I.4**
Définir l'ensemble des points du cercle $\mathcal{C}$ de centre $(a,b) \in \mathbb{R}^2$ et de rayon $r$.

**Exercice I.5**
Définir l'ensemble des points de tous les cercles dont l'aire est égale à $1$.

**Exercice I.6**
Définir l'ensemble des points du disque ouvert $\mathcal{D}$ de centre $(a,b) \in \mathbb{R}^2$ et de rayon $2$.

</br>

### _<u>Partie II : Relations ensemblistes (~1h40)</u>_

**Exercice II.1**
Soient $A = \left\{1,2,3\right\}$ et $𝐵 = \left\{0,1,2,3\right\}$. Décrire les ensembles $𝐴 \cap 𝐵$, $𝐴 ∪ 𝐵$ et $𝐴 × 𝐵$.

**Exercice II.2**
Soient $A=\{0,2,4\}$ et $B = \{1,3,4,5 \}$ dans le référentiel $E=\{0,1,2,3,4,5\}$.
Déterminer les ensembles $\overline{A}$,$\overline{B}$,$A \cap B$, $A \cup B$, $A \setminus B$, $\mathcal{P}(A)$ et $A \times B$

**Exercice II.3**
Soient $A = [1, 3]$ et $B=[2,4]$. Déterminer les ensembles $A \cap B$ et $A\cup B$.

**Exercice II.4**
Déterminer le complémentaire dans $\mathbb{R}$ des ensembles suivants $A_1 = ] −\infty, 0]$, $A_2 = ] −\infty, 0[$, $A_3 = ]0, +\infty[$, $A_4 = [0, +\infty[$, $A_5 =]1,2[$, $A_6 = [1,2[$

**Exercice II.5** Soient $A = ] − \infty, 1[ \cup ]2, +\infty[$, $B =] − \infty, 1[$ et $B = [2, +\infty[$. Comparer les ensembles $\bar{A}$ et $\bar{B} \cap \bar{C}$

</div><div class='flex'>

**Exercice II.6**
Soient $𝐴 =] −\infty, 3]$, $𝐵 =] − 2,7]$ et $𝐶 =] − 5, +\infty[$ trois parties de $\mathbb{R}$.
Déterminer $𝐴 ∩ 𝐵$, $𝐴 ∪ 𝐵$, $𝐵 ∩ 𝐶$, $𝐵 ∪ 𝐶$, $ℝ ∖ 𝐴$, $𝐴 ∖ 𝐵$, $(ℝ ∖ 𝐴) ∩ (ℝ ∖ 𝐵)$, $(ℝ ∖ (𝐴 ∪ 𝐵)$, $(𝐴 ∩ 𝐵) ∪
(𝐴 ∩ 𝐶)$ et $𝐴 ∩ (𝐵 ∪ 𝐶)$

**Exercice II.7**
Soit $A = \left\{1,8,10\right\}$. Décrire $\mathcal{P}(A)$, l'ensemble des parties de $A$.

**Exercice II.8**
Soit $C_{red} = [\![ 0; 2 ]\!],C_{green} = [\![ 0; 2 ]\!], C_{blue} = [\![ 0; 2 ]\!],$. Décrire $C_{red} \times C_{green} \times C_{blue}$.

**Exercice II.9 (démo de cours)**
Soient $A$, $B$ et $C$ trois parties d’un ensemble $E$. Montrer que

1. $𝐴 ∪ (𝐵 ∩ 𝐶) = (𝐴 ∪ 𝐵) ∩ (𝐴 ∪ 𝐶)$
2. $𝐴 ∩ (𝐵 ∪ 𝐶) = (𝐴 ∩ 𝐵) ∪ (𝐴 ∩ 𝐶)$

**Exercice II.10**

1. Montrer que $(𝐴 ∖ 𝐵) ∖ 𝐶 = 𝐴 ∖ (𝐵 ∪ 𝐶)$
2. Montrer que $(𝐴 ∖ 𝐵) ∩ (𝐶 ∖ 𝐷) = (𝐴 ∩ 𝐶) ∖ (𝐵 ∪ 𝐷)$

**Exercice II.11**
On donne la définition suivante $𝐴Δ𝐵 = (𝐴 ∖ 𝐵) ∪ (𝐵 ∖ 𝐴)$

1. Montrer que
   $(𝐴 ∩ 𝐵) ∩ (\overline{𝐴 ∩ 𝐶}) = 𝐴 ∩ 𝐵 ∩ \overline{𝐶}$
   $(𝐴 ∩ 𝐶) ∩ (\overline{𝐴 ∩ 𝐵}) = 𝐴 ∩ 𝐶 ∩ \overline{𝐵}$
2. En déduire que
   $(𝐴 ∩ 𝐵)Δ(𝐴 ∩ 𝐶) = 𝐴 ∩ (𝐵Δ𝐶)$

</div></div>

<!-- --- -->
<!--  -->
<!-- ### _<u> Partie III : Pour aller plus loin (~1h00)</u>_ -->
<!--  -->
<!-- <div class='flex-horizontal'><div class='flex'> -->
<!--  -->
<!-- **Exercice III.1** -->
<!-- Soit $E$ un ensemble et soit $\mathcal{P}(E)$ l’ensemble des parties de $E$. -->
<!-- Pour $A$ et $B$ dans $\mathcal{P}(E)$, on appelle différence symétrique de $A$ par $B$ l’ensemble, noté $𝐴Δ𝐵$ défini par : $𝐴Δ𝐵 = (𝐴 ∪ 𝐵) ∖ (𝐴 ∩ 𝐵)$ -->
<!--  -->
<!-- 1. Montrer que $𝐴Δ𝐵 = (𝐴 ∩ \overline{𝐵}) ∪ (𝐵 ∩ \overline{A}) = (𝐴 ∖ 𝐵) ∪ (𝐵 ∖ 𝐴)$. -->
<!-- 2. Calculer $𝐴Δ𝐴$, $𝐴Δ∅$ et $𝐴Δ𝐸$. -->
<!-- 3. Montrer que pour tous $A$, $B$ et $C$ dans $\mathcal{P}(E)$, on a : -->
   <!-- a) Montrer que : $\overline{\left(𝐴 \cap \overline{𝐵}\right) \cup \left(𝐵 \cap \overline{𝐴}\right)} = \left(\overline{𝐴} \cap \overline{𝐵}\right) \cup \left(𝐵 \cap 𝐴\right)$ -->
   <!-- b) Montrer que : $(𝐴Δ𝐵)Δ𝐶 = (𝐴 ∩ \overline{𝐵} ∩ \overline{𝐶}) ∪ (𝐵 ∩ \overline{𝐴} ∩ \overline{𝐶}) ∪ (𝐶 ∩ \overline{𝐴} ∩ \overline{𝐵}) ∪ (𝐶 ∩ 𝐵 ∩ 𝐴)$ -->
   <!-- c) Montrer que $𝐴Δ(𝐵Δ𝐶) = (𝐶𝛥𝐵)𝛥𝐴$ -->
   <!-- d) A l’aide du b), montrer que $(𝐴𝛥𝐵)𝛥𝐶 = (𝐶𝛥𝐵)𝛥𝐴$ -->
   <!-- e) En déduire que : $(𝐴Δ𝐵)Δ𝐶 = 𝐴Δ(𝐵Δ𝐶)$ -->
<!--  -->
<!-- **Exercice III.2 (démo de cours)** -->
<!-- Soit $E$ un ensemble et $F$ et $G$ deux parties de $E$. Démontrer que : -->
<!--  -->
<!-- 1. $(\overline{𝐴 \cap 𝐵}) = \overline{𝐴} \cup \overline{𝐵}$ -->
<!-- 1. $(\overline{𝐴 \cup 𝐵}) = \overline{𝐴} \cap \overline{𝐵}$ -->
<!-- <!-- 1. $E \setminus (A \cap B) = (E \setminus A) \cup (E \setminus B)$ -->
<!-- 1. $E \setminus (A \cup B) = (E \setminus A) \cap (E \setminus B)$ --> -->
<!--  -->
<!-- **Exercice III.3** -->
<!-- Soit $E$ un ensemble et $F$ et $G$ deux parties de $E$. Démontrer que : -->
<!--  -->
<!-- 1. $F \subset G \Leftrightarrow F ∪ G = G$ -->
<!-- 2. $F \subset G \Leftrightarrow F ∩ \overline{G} = ∅$ -->
<!--  -->
<!-- </div><div class='flex'> -->
<!--  -->
<!-- </div></div> -->
<!--  -->
