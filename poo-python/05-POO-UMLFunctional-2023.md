---
marp: true
paginate: true

theme: dav-default
title: Cours POO - IA School

footer: "Programmation Orientée Objet 2023"
_footer: ""
---

<!-- PARTIE 0 : Présentation du cours -->

<!-- _paginate: skip -->
<!-- _class: cover -->

<div class="coverBlockCenter">
<div class="coverModuleName">Programmation Orientée Objet en Python</div>
<div class="coverCourseName"><span class="important">#5 </span>UML <span class="coverModuleName" style="font-size:40px;font-weight:bold">Functional Diagrams</span></div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/ia-school-logo.svg" />
<div class="coverYear coverFooterRight">2023</div>

<!-- TABLE DES MATIERES -->

---

## Table des matières

<b><span class="important">01 </span> Diagramme de séquences</b>
Syntaxe. Exemples.

<b><span class="important">02 </span> Synthèse COO</b>
Modélisation complète des interactions.

---

<!-- PARTIE 01 : Diagrammes de séquences -->

<div class='main'>

# 01

## Diagrammes de séquences

</div>

---

## **Diagrammes de séquences**

**Phase**
Fin de conception générale et pendant la conception détaillée.

**Objectifs**

- Représenter les interactions entre différents objets

![height:300](assets/img/seq-diag-seq-syntax.png)

---

## Diagrammes de séquences

![height:350](assets/img/seq-diag-seq-syntax.png)

---

## Diagrammes de séquences

![height:550](assets/img/seq-explained.png)

---

## Diagramme de séquences

### **Syntaxe**

<div class='flex-horizontal' style="height:70%"><div class='flex' style='flex:2'>

<div class='block'>

# Ligne de vie

<div class='flex-horizontal'><div class='flex'>

**Acteur**
Ligne de vie d'un acteur du système.

![](assets/img/seq-syntax-actor-line.png)

</div><div class='flex'>

**Objets**
Ligne de vie d'un objet du système.

![](assets/img/seq-syntax-obj-line.png)

</div></div>
</div>

</div><div class='flex'>

<div class='block' style="height:110%">

# Messages

**Envoi de message**
<u>_Exemples :_</u>
appeler("Mozart", 510)
afficher(x,y)
initialiser(x=100)

![](assets/img/seq-syntax-envoi-msg.png)

**Retour de message**
<u>_Exemples :_</u>
age
name="Mark"
"Summer"

![](assets/img/seq-syntax-retour-msg.png)

</div></div>

---

## Diagramme de séquences

### **Syntaxe**

<div class='flex-horizontal'><div class='flex'>

<div class='block' style="height:90%">

# opt

Contient une séquence qui peut ou non se produire.

![](assets/img/seq-syntax-opt.png)

</div>

</div>
<div class='flex'>

<div class='block' style="height:90%">

# alt

Contient des alternatives à une séquence de messages.

![](assets/img/seq-syntax-alt.png)

</div>

</div><div class='flex'>

<div class='block' style="height:90%">

# loop

Le fragment est répété un certain nombre de fois.

![](assets/img/seq-syntax-loop.png)

</div>

</div>

</div>

---

## Diagramme de séquences

**Exemple**
![height:500](./assets/img/seq-resto-ex.png)

---

<!-- PARTIE 02 : Synthèse COO -->

<div class='main'>

# 02

## Synthèse COO

</div>

---

## Synthèse conception orientée objet

Les **diagrammes de cas d’utilisation** modélisent à **QUOI** sert le système, en organisant les interactions possibles avec les acteurs.

Les **diagrammes de classes** permettent de spécifier la structure et les liens entre les objets dont le système est composé : ils spécifient **QUI** sera à l’oeuvre dans le système pour réaliser les fonctionnalités décrites par les diagrammes de cas d’utilisation.

Les **diagrammes de séquences** permettent de décrire **COMMENT** les éléments du système interagissent entre eux et avec les acteurs :

- Les objets au coeur d’un système interagissent en s’échangent des messages.
- Les acteurs interagissent avec le système au moyen d’IHM (Interfaces Homme-Machine).

---

## Synthèse conception orientée objet

Pour être complètement spécifiée, une interaction doit être décrite dans plusieurs diagrammes UML:

<div class='flex-horizontal'><div class='flex'>

- Cas d’utilisation
  ![](./assets/img/synthese-coo-usecase.png)

- Classes pour spécifier les opérations nécessaires

</div><div class='flex'>

- Séquences
  ![](./assets/img/synthese-coo-seq.png)

</div></div>

![](./assets/img/synthese-coo-class.png)
