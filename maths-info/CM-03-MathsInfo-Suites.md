---
marp: true
paginate: true

theme: dav-maths
title: Suites

footer: "Suites"
_footer: ""
math: mathjax
---

<!-- PAGE DE COUVERTURE -->
<!-- _paginate: skip -->
<!-- _class: cover -->
<div class='coverBlockCenter'><div class='coverModuleName'>Mathématiques pour l'informatique</div><div class='coverCourseName'><span class='important'>#3 </span>Suites</div><div class='coverAuthor'>par <span class='important'>David Albert</span></div></div><img style="background-color:#ffffff" class='coverFooterLeft' height='60px' src='./assets/img/logo-gema.png' /><div class='coverYear coverFooterRight'>2023</div>

---

<!-- TABLE DES MATIERES -->

## Table des matières

<b><span class='important'>00 </span>Notations</b>

<b><span class='important'>01 </span>Suites numériques</b>
Suites numérique. Définition par récurrence.

<b><span class='important'>02 </span>Suites arithmétiques</b>
Suites arithmétiques.

<b><span class='important'>03 </span>Suites géométriques</b>
Suites géométriques.

<b><span class='important'>04 </span> Démonstration par récurrence</b>
Méthode et exemples.

<!-- FIN TABLE DES MATIERES -->

---

## **00** Notations

<span style="display: inline-block; width:4rem;">$u_n$ </span>notation utilisée pour les suites

<span style="display: inline-block; width:4rem;">$\sum$ </span>symbole de sommation

<span style="display: inline-block; width:4rem;">$\prod$ </span>symbole de produit

---

<!-- PARTIE 04 : Suites -->

<div class='main'>

# 01

## Suites numériques

</div>

---

## Suites numériques

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Definition - Suite numérique</b>
</div>

Une suite numérique est une fonction définie sur $\mathbb{N}$, à valeurs dans $\mathbb{R}$ :

$u : \mathbb{N} \rightarrow \mathbb{R}$
$\ \ \ \ \ \ n \rightarrow u(n)$, aussi noté $u_n$

</div>

**Exemple :**

La liste 5; 10; 12; 20; 21; ... correspond à la suite $(u_n)$ telle que :
$u_0=5;\ u_1=10;\ u_2=12;\ u_3=20;\ u_4=21;\ ...$

On dit que $5$ est le terme initial ou terme de rang $0$.
$10$ est le terme de rang $1$.
$12$ est le terme de rang $2$.

---

## Suites numériques

### **définie par une formule explicite $u_n = f(n)$**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Definition - Suite définie par une formule explicite</b>
</div>

Une suite est définie par une **formule explicite** lorsque $u_n$ s'exprime directement en fonction de $n$
Dans ce cas, on peut calculer chaque terme à partir de son indice.

</div>

**Exemple :**

Pour tout entier naturel $n$, on a $u_n=\sqrt{2n+1}=f(n)$.

Alors:

$u_0=\sqrt{2\times 0+1}=\sqrt{1}$
$u_1=\sqrt{2\times 1+1}=\sqrt{3}$
$u_2=\sqrt{2\times 2+1}=\sqrt{5}$
...
...
$u_{32}=\sqrt{2\times 32+1}=\sqrt{65}$

---

## Suites numériques

### **définie par une relation de récurrence $u_{n+1} = f(u_n)$**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Definition - Suite définie par une relation de récurrence</b>
</div>

Une suite est définie par une **relation de récurrence** quand elle est définie par la donnée de :

- son **premier terme**
- une relation qui permet de calculer chaque terme à partir du précédent

</div>

**Exemple :** Soit $u_0 = 2$ et $u_{n+1}=u_n^2 -1$

$u_0 = 2$
$u_1 = 2^2 -1 = 3$
$u_2 = 3^2 -1 = 8$
$u_3 = 8^2 -1 = 63$
...

<div class='block warning'>
Contrairement à une suite définie grâce à sa forme explicite, une relation de récurrence ne permet pas de calculer un terme de rang donné sans avoir calculé tous les termes précédents.

</div>

---

## Suites numériques

### **Exercices**

1. Soit $(u_n)_{n \in \mathbb{N}}$ définit par $u_n = 3n+21$. Donner $u_0, u_1, u_2, u_5, u_{10}\ et\ u_{100}$.

</br>
</br>
</br>
</br>
</br>

2. Soit $(u_n)_{n \in \mathbb{N}}$ définit par $u_0=3$ et $u_{n+1} = 2u_n + 2$. Donnez $u_0, u_1, u_2, u_5\ et\ u_{10}$.

---

<!-- PARTIE 04 : Suites -->

<div class='main'>

# 02

## Suites arithmétiques

</div>

---

## Suites arithmétiques

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Definition - Suite arithmétique</b>
</div>

Une suite $(u_n)$ est une **suite arithmétique** s'il existe un nombre $r$ tel que pour tout entier $n$, on a : $u_{n+1} = u_n + r$

Le nombre $r$ est appelé **raison** de la suite.

</div>

**Exemple :** Soit la suite $(u_n)$ définit par :

<div class='flex-horizontal'><div class='flex' style="flex:0.2">

$$

\begin{equation}
\begin{cases}
u_0 = 3\\
u_{n+1} = u_n + 5
\end{cases}
\end{equation}


$$

</div><div class='flex'>

</div></div>

Une telle suite est appelée une suite arithmétique de raison $5$ et de premier terme $3$.

---

## Suites arithmétiques

### **Propriétés**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Propriété</b>
</div>

$(u_n)$ est une suite arithmétique de raison $r$ et de premier terme $u_0$.

Pour tout entier naturel $n$, on a : $u_n = u_0 + n \times r$

</div>

**Démonstration :**
D'après la définition, une suite arithmétique $(u_n)$ de raison $r$ et de premier terme $u_0$ vérifie la relation $u_{n+1} = u_n + r$. En calculant les premiers termes :
$u_1 = u_0 + r$
$u_2 = u_1 + r = (u_0 + r) + r = u_0 + 2r$
$u_3 = u_2 + r = (u_0 + 2r) + r = u_0 + 3r$
...
$u_{n} = u_{n-1} + r = (u_0 + (n-1)r) + r = u_0 + nr$

---

## Suites arithmétiques

### **Propriétés**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Propriété</b>
</div>

$(u_n)$ est une suite arithmétique de raison $r$.

- si $r>0$ alors $u_{n+1} - u_n > 0$ et la suite est croissante.

- si $r<0$ alors $u_{n+1} - u_n > 0$ et la suite est décroissante.

</div>

---

## Suites arithmétiques

### **Exercices**

1. La suite $(u_n)$ définie par $u_n= 7-9n$ est-elle arithmétique ?

</br>
</br>
</br>
</br>
</br>

2. La suite $(v_n)$ définie par $v_n= n^2 + 3$ est-elle arithmétique ?

---

<!-- PARTIE 03 : Suites géométriques -->

<div class='main'>

# 03

## Suites géométriques

</div>

---

## Suites géométriques

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Definition - Suites géométriques</b>
</div>

Une suite $(u_n)$ est une **suite géométrique** s'il existe un nombre $q$ tel que pour tout entier $n$, on a : $u_{n+1} = q \times u_n$

Le nombre $q$ est appelé **raison** de la suite.

</div>

**Exemple :**
Soit la suite $(u_n)$ définit par :

<div class='flex-horizontal'><div class='flex' style="flex:0.2">

$$

\begin{equation}
\begin{cases}
u_0 = 3\\
u_{n+1} = 2 \times u_n
\end{cases}
\end{equation}


$$

</div><div class='flex'>

</div></div>

Une telle suite est appelée une suite géométrique de raison $2$ et de premier terme $3$.

---

## Suties géométriques

### **Propriétés**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Propriété</b>
</div>

$(u_n)$ est une suite géométrique de raison $q$ et de premier terme $u_0$.

Pour tout entier naturel $n$, on a : $u_n=u_0\times q^n$.

</div>

**Démonstration :**
D'après la définition, la suite géométrique $(u_n)$ de raison $q$ et de premier terme $u_0$ vérifie la relation $u_{n+1} = q \times u_n$.

En calculant les premiers termes :
$u_1 = q \times u_0$
$u_2 = q \times u_1 = q \times (q \times u_0) = q^2 \times u_0$
$u_3 = q \times u_2 = q \times (q^2 \times u_0) = q^3 \times u_0$
...
$u_n = q \times u_{n-1} = q \times (q^{n-1} \times u_0) = q^n \times u_0$

---

## Suites géométriques

### **Propriétés**

<div class='block note'>
<div class='block-icon'>
<i class='far fa-heart' style='padding-right:1rem;'></i>
<b>Propriétés</b>
</div>

$(u_n)$ est une suite géométrique de raison $q$ et de premier terme non nul $u_0$.

Pour :

- Si $q > 1$ alors la suite $(u_n)$ est croissante.
- Si $0 < q < 1$ alors la suite $(u_n)$ est décroissante.

Pour :

- Si $q > 1$ alors la suite $(u_n)$ est décroissante.
- Si $0 < q < 1$ alors la suite $(u_n)$ est croissante.

</div>

---

## Suites géométriques

### **Exercices**

1. La suite $(u_n)$ définie par $u_n=3 \times 5^n$ est-elle géométrique ?

---

<!-- PARTIE 04 : Démonstration par récurrence -->

<div class='main'>

# 04

## Démonstration par récurrence

</div>

---

## Démonstration par récurrence

### **Méthode**

Pour démontrer par récurrence une propriété $P(n)$ on procède en 2 étapes:

1. <b class='important'>Initialisation :</b> On vérifie que $P(n)$ est vraie pour une certaine valeur de $n$. Notons cette valeur $n_0$. On choisit pour $n_0$, la plus petite valeur de $n$ possible.
<div class='block note'>

<i class='block-icon fas fa-info'></i>

La plupart du temps, on vérifie que $P(0)$, $P(1)$ ou $P(2)$ est vraie.

</div>

1. <b class='important'>Hérédité :</b> On suppose que $P(n)$ est vraie pour **UN** entier $n \ge n_0$

   On rédige toujours de la façon suivante:
   <b class='info'>Soit un entier $n \ge n_0$. Supposons $P(n)$ vraie et montrons que cela entraine que $P(n+1)$ est vraie.</b>

1. <b class='important'>Conclusion :</b> On rédige la conclusion toujours de la même façon:
   <b class='info'>Comme $P(n_0)$ est vraie et $P(n)$ est héréditaire pour tout entier $n \ge n_0$, donc par récurrence $P(n)$ est vraie pour tout entier $n \ge n0$.</b>

---

## Démonstration par récurrence

### **Exercices**

Montrer que si $(u_n)$ est une suite arithmétique de raison $r$ alors pour tout $n \in \mathbb{N}^*$, on a $u_n = u_0 + n \times r$

---

## Démonstration par récurrence

### **Exercices (suite)**

Montrer que pour tout $n \in \mathbb{N}^*$, on a :

<div class='flex-horizontal'><div class='flex' style="flex:0.5">

$$(i)\ \ \ \ \sum_{i=1}^{n}i = \frac{n(n+1)}{2}$$

$$(ii)\ \ \ \ \sum_{i=1}^{n}i^2 = \frac{n(n+1)(2n+1)}{6}$$

</div><div class='flex'>

</div></div>

<script type='module'>
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });
window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>
