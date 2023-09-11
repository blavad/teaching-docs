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

<b><span class='important'>01 </span>Suites</b>
Suites arithmétiques.

<b><span class='important'>02 </span>Suites</b>
Suites arithmético-géométrique.

<b><span class='important'>03 </span> Démonstration par récurrence</b>
Définition et exemples.

<!-- FIN TABLE DES MATIERES -->

---

## **00** Notations

<span style="display: inline-block; width:4rem;">$u_n$ </span>notation utilisé pour les suites

<span style="display: inline-block; width:4rem;">$\sum$ </span>symbole de sommation

<span style="display: inline-block; width:4rem;">$\prod$ </span>symbole de produit

---

<!-- PARTIE 04 : Suites -->

<div class='main'>

# 01

## Suites

</div>

---

## Démonstration par récurrence

**Exemple**
Montrer que pour tout $n \in \mathbb{N}^*$, on a :

$$(i)\ \ \ \ \sum_{i=1}^{n}i = \frac{n(n+1)}{2}$$

$$(ii)\ \ \ \ \sum_{i=1}^{n}i^2 = \frac{n(n+1)(2n+1)}{6}$$

<script type='module'>
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });
window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>
