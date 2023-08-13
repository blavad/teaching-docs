---
marp: true
paginate: true

theme: dav-default
title: Cours POO - IA School

footer: 'Programmation Orientée Objet 2023'
_footer: ''

---

<!-- PARTIE 0 : Présentation du cours -->

<!-- _paginate: skip -->
<!-- _class: cover -->

<div class="coverBlockCenter">
<div class="coverModuleName">Programmation Orientée Objet en Python</div>
<div class="coverCourseName"><span class="important">#5 </span>UML (class diagram)</div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/ia-school-logo.svg" />
<div class="coverYear coverFooterRight">2023</div>


--- 
<!-- TABLE DES MATIERES -->

## Table des matières 

<b><span class="important">01 </span> Introduction à UML</b>
Motivations. UML. Cycle de développement. Diagrammes. 

<b><span class="important">02 </span> Diagramme de cas d'utilisation</b>
Quelques exemples.

<b><span class="important">03 </span> Diagramme de classes</b>
Typing. Documentation. Gestion des erreurs. Tests unitaires.


---

<!-- _class: bg2 -->

## Cycle en V

Besoin de conception pour réaliser une architecture complexe.

![height:480](assets/img/cycleV.png)


---

## **U**nified **M**odeling **L**anguage 

<b class='important'>UML</b> c'est quoi ?
- un langage de modélisation de systèmes informatiques
- modèle graphique (à base de pictogrammes)
- indépendant du langage de programmation
- intervient dans la phase de conception (générale et détaillée)

---

<!-- _class: bg2 -->

<div class='block note'>

<i class='block-icon fas fa-info'></i>

**Fun fact** : UML est décrit en UML. 

![height:450px](assets/img/UML-taxonomy.png)

</div>


---

<!-- _class: bg2 -->

## Quelques diagrammes 

<div class='flex-horizontal' style="height:60%;"><div class='flex'>

<div class='block'  style="height:100%;">

# Diagrammes structurels

<b class='important'>Diagramme de classes</b>
Définit l’ensemble des classes et de leurs relations

**Diagramme de composants**
Liste les composants logiciels

**Diagramme de déploiement**
Définit la répartition des composants sur une
architecture matérielle

</div>

</div><div class='flex'>


<div class='block' style="height:100%;">

# Diagrammes de comportement

<b class='important'>Diagramme des cas d'utilisation</b>
Définit les scénarios d’interaction entre les utilisateurs et le système

**Diagramme d'activité**
Représente les états du système et leurs transitions par événements

<b class='important'>Diagramme de séquence</b>
Représente les scénarios d’interactions entre entités du système


</div>

</div></div>

<br/>
<br/>

<span style="font-size:20px">

Référence: [Laurent Vercouter, Cours UML, Insa Rouen](https://pagesperso.litislab.fr/lvercouter/teaching/)

</span>

---

## Chaîne de conception

Différents diagrammes arrivent à différents moments dans la chaîne de conception.

<div class='flex-horizontal'><div class='flex' style='flex:0.7'>

![height:500px](assets/img/UML-roadmap.png)


</div><div class='flex' style='flex:0.3;'>

<div style="height:80%"></div>

<span style="font-size:20px">

Référence: 
[Laurent Audibert](https://laurent-audibert.developpez.com/Cours-UML/?page=mise-en-oeuvre-uml)

</span>

</div></div>



---

<!-- PARTIE 02 : Cas d'utilisation -->

<div class='main'>

# 02

## Cas d'utilisation

</div>

---

<!-- _class: bg1 -->

## Diagramme de cas d'utilisation 

<b class='important'>Objectifs</b>





<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });

window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>