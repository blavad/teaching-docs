---
marp: true
paginate: true

theme: dav-maths
title: Cours POO - IA School

footer: "Programmation Orientée Objet 2024"
_footer: ""
---

<!-- PARTIE 0 : Présentation du cours -->

<!-- _paginate: skip -->
<!-- _class: cover -->

<div class="coverBlockCenter">
<div class="coverModuleName">Introduction à l'apprentissage par renforcement</div>
<div class="coverCourseName"><span class="important">#3 </span>Dynamic Programming</div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/logo-gema.png" />
<div class="coverYear coverFooterRight">2024</div>

<!-- TABLE DES MATIERES -->

---

## Table des matières

<b><span class="important">01 </span> Policy Evaluation</b>

<b><span class="important">02 </span> Policy Iteration</b>
Introduction. Exemples.

<b><span class="important">03 </span> Value Iteration</b>
Introduction. Exemples.

---

## Planification

Dans le cas où le modèle de l’environnement est parfaitement connu, Bellman introduit dans ses travaux
des méthodes de planification directe, aussi connu sous le nom de programmation dynamique. Cepen-
dant, le modèle de l’environnement n’est pas toujours connu. Une seconde méthode consiste donc à
estimer un modèle de l’environnement si cela est possible. Il faut ensuite appliquer les méthodes de
programmation dynamique classiques sur l’estimation du modèle de l’environnement.
