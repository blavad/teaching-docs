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
<div class="coverCourseName"><span class="important">#4 </span>UML  
<span class="coverModuleName" style="font-size:40px;font-weight:bold">Structural Diagrams</span></div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<!-- <img  height="60px" src="assets/img/logoUnboared.png" /> -->
<div class="coverFooterLeft">
<img  style="background-color:#fff" height="60px" src="assets/img/ia-school-logo.svg" />
</div>
<div class="coverYear coverFooterRight">2023</div>

---

<!-- TABLE DES MATIERES -->

## Table des matières

<b><span class="important">01 </span> Cycles de développement</b>
Cycle en V et méthodes AGILE.

<b><span class="important">02 </span> Introduction à UML</b>
Motivations. Diagrammes. Chaîne de conception.

<b><span class="important">03 </span> Diagramme de cas d'utilisation</b>
Quelques exemples.

<b><span class="important">04 </span> Maquettes</b>
Logiciels pour créer des maquettes.

<b><span class="important">05 </span> Diagramme de classes</b>
Syntaxe. Modèle du domaine. Diagramme de classes participantes.

---

<!-- PARTIE 01 : Cycles de développement -->

<div class='main'>

# 01

## Cycles de développement

</div>

---

<!-- _class: bg2 -->

## Cycle en V

![height:540](assets/img/poo-python-CycleV.png)

---

## Vers une méthodologie **AGILE**

<div class='block warning'>

<i class='block-icon fas fa-exclamation'></i>

Le **cycle en V** a un **inconvénient majeur**. La vérification de la conformité aux besoins client attend la fin du développement du produit. S'il y a un soucis, on s'en rend compte **très tardivement**.

</div>

**Méthologie AGILE**
Pour pallier à cela, les entreprises privilégient de plus en plus des **cycles courts** et successifs. On répètera successivement les étapes de _spécifications, conception, développement, test et validation_.
![height:270](assets/img/cycle-agile.png)

---

<!-- PARTIE 02 : Introduction à UML -->

<div class='main'>

# 02

## Introduction à UML

</div>

---

## **U**nified **M**odeling **L**anguage

**Motivations**

- Besoin de se comprendre
- Besoin de conception pour réaliser une architecture complexe.

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

<!-- PARTIE 03 : Cas d'utilisation -->

<div class='main'>

# 03

## Diagramme de cas d'utilisation

</div>

---

## Etude de cas

### **Gestion d'un restaurant**

On souhaite réaliser une application pour un restaurant qui lui permettra de gérer les réservations et les commandes de ses clients.

<div class='block warning'>

<i class='block-icon fas fa-info'></i>

# On utilisera cet exemple comme fil rouge tout au long de ce cours.

</div>

**Enoncé détaillé**
Le restaurant accueille des clients qui sont identifiés par leur nom, leur email et leur numéro de téléphone. Le restaurant est ouvert tous les jours de 19h et 23h30. Il réalise chaque soir 3 services de 1h30 et et jusqu'à 20 clients par service. Les clients peuvent réserver une table sur ces créneaux. S'il n'y a plus de place, ils peuvent également commander leur repas en ligne, payer via l'application et venir le récupérer dans la foulée. Sur place, les serveurs s'occupent des commandes des et du paiement des clients.

---

<!-- _class: bg1 -->

## Diagramme de cas d'utilisation

### **Résumé**

<div class='flex-horizontal'><div class='flex'>

**Objectifs**

- Premier diagramme réalisé pour définir les scénarios d’usage
- A réaliser avec le client
- À utiliser tout au long du développement

</div><div class='flex'>

**Exemple**

![height:430](assets/diagrams/usecase-ex-full.png)

</div></div>

---

## Diagramme de cas d'utilisation

### **Syntaxe**

<div class='flex-horizontal'><div class='flex'>

<div class='block'>

<i class='block-icon fas fa-hand'></i>

# Déclenchement

![width:450](assets/diagrams/usecase-declenche.png)

</div>

<div class='block'>

<i class='block-icon fas fa-arrow-right'></i>

# Prolongement

![width:450](assets/diagrams/usecase-extends.png)

</div>

</div><div class='flex'>

<div class='block'>

<i class='block-icon fas fa-check'></i>

# Pré-requis

![width:450](assets/diagrams/usecase-include.png)

</div>

<div class='block'>

<i class='block-icon fas fa-child'></i>

# Héritage

![width:180](assets/diagrams/usecase-heritage.png)

</div>
</div></div>

---

<!-- PARTIE 04 : Maquettes -->

<div class='main'>

# 04

## Maquettes

</div>

---

## Réaliser les premières maquettes

Rien de tel que quelques maquettes pour mettre tout le monde d'accord sur l'interface homme-machine et ses interactions.

**Outils:** [drawio](https://app.diagrams.net/) et [Figma](https://www.figma.com/)

![height:380](assets/img/maquettes-drawio.png)

<!-- ![height:380](assets/img/maquettes-figma.png) -->

---

<!-- PARTIE 05 : Diagramme de classes -->

<div class='main'>

# 05

## Diagrammes de classes

</div>

---

## Diagramme de classes

### **Syntaxe 1**

<div class='flex-horizontal'><div class='flex' style="flex:0.5">

<div class='block'>

<!-- <i class='block-icon fas fa-'></i> -->

# Classe

**Attributs**
_[+/#/-] attr : Type_

**Méthodes**
_[+/#/-] method(param: Type): ReturnType_

<div class='flex-horizontal'><div class='flex' style='flex:0.3'>

![height:140](assets/diagrams/class-class.png)

</div><div class='flex' style='flex:0.7'>

<b class='important'>+</b> attributs **publics**
<b class='important'>#</b> attributs **protégés**
<b class='important'>-</b> attributs **privés**

</div></div></div></div>

<div class='flex'  style="flex:0.5">

<div class='block'>

# Interface et classes abstraites

![height:120](assets/diagrams/class-interface.png)

Méthodes abstraites en _italic_ (ou <u>soulignée</u>)

</div>
<div class='block'>

# Héritage

![height:100](assets/diagrams/class-heritage.png)

</div>

</div></div>

---

## Diagramme de classes

### **Syntaxe 2**

<div class='flex-horizontal' style="height:70%"><div class='flex'>

<div class='block'  style="height:100%">

# Association

Si deux classes sont en intéractions dans le système on les associent.

</br>

<img src="assets/diagrams/class-association.png"/>

On peut préciser la multiplicité.

</div>

</div><div class='flex' style="flex:1.5">

<div class='block' style="height:100%">

# Aggrégation / Composition

- associations particulières
- On peut dire: "objet de la classe 1 <u>contient</u> objet(s) de la classe 2"

<div class='flex-horizontal'><div class='flex' style="padding:0;">

**Composition**
![height:110](assets/diagrams/class-composition.png)

</div><div class='flex' style="padding:0;">

</br>

Contient physiquement
_Class1_ détruite <i class='fas fa-arrow-right'></i> _Class2_ détruite

</div></div>

<div class='flex-horizontal'><div class='flex' style="padding:0;">

**Aggrégation**
![height:100](assets/diagrams/class-aggregation.png)

</div><div class='flex' style='padding:0;'>

</br>

_Class1_ détruite <i class='fas fa-arrow-right'></i> _Class2_ persiste

</div></div>

</br>

</div>

</div></div>

---

## **Modèle du domaine**

<div class='flex-horizontal'><div class='flex' style='flex:1.5'>

**Phase**
Début de conception générale. Intervient juste après les premières maquettes et cas d'utilisation.

**Objectifs**

- Premier diagramme de classes à réaliser
- Indépendant des fonctionnels de l’application
- Représente le domaine métier

</div><div class='flex'>

![height:500px](assets/diagrams/class-domain-example.png)

</div></div>

---

## **Diagramme de classes participantes**

**Phase**
Fin de conception générale. Intervient dans la dernière phase de la conception générale en même temps que les diagrammes de séquence et d'activité.

**Objectifs**

- Enrichissement du modèle de domaine
- Modélisation guidée par les besoins
