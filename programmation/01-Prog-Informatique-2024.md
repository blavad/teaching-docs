---
marp: true
paginate: true

theme: dav-maths
title: Cours POO - IA School

footer: "Programmation Orientée Objet 2023"
_footer: ""
---

<!-- PARTIE 0 : Présentation du cours -->

<!-- _paginate: skip -->
<!-- _class: cover -->

<div class="coverBlockCenter">
<div class="coverModuleName">Informatique & Programmation</div>
<div class="coverCourseName"><span class="important">#1 </span>Intro à l'informatique</div>
<div class="coverAuthor">par <span class="important">David Albert</span></div>
</div>

<img class="coverFooterLeft" style="background-color:#fff" height="60px" src="assets/img/logo-gema.png" />
<div class="coverYear coverFooterRight">2024</div>

<!-- TABLE DES MATIERES -->

---

## Table des matières

<b><span class="important">01 </span> Ordinateur</b>
Périphériques. Processeur. RAM. Disque dure.

<b><span class="important">02 </span>Système d'exploitation</b>
Pourquoi ? Comment ?

<b><span class="important">03 </span>Représentation de l'information </b>
Représentation des nombres, des caractères et des images.

<b><span class="important">04 </span> Système de fichiers </b>
Arborescence Linux. Chemin absolu. Chemin relatif.

<b><span class="important">05 </span> Interpréteur de commandes</b>
Utiliser un interpréteur de commandes.

---

## **01** Ordinateur

L'ordinateur est une machine de prédilection en informatique.

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Vous allez utiliser un ordinateur pendant de longues heures. Cela vaut donc le coup de savoir, au moins sommairement, de quoi est fait un ordinateur.

</div>

</br>
</hr>
</br>

**Visualisons le démontage d'un ordinateur**
https://www.lemonde.fr/blog/binaire/2017/05/31/podcast-le-ventre-de-mon-ordi/

---

## **02** Système d'exploitation

**C'est quoi ?**
Le système d’exploitation se situe à l'interface entre deux mondes : le logiciel et le matériel

<div class='flex-horizontal'><div class='flex'>

<div class='block'>
<div class='block-icon'>
<b>Le logiciel</b>
</div>

Des applications tels que :

- Chrome, Word, GTA 4, Discord
- Des utilitaires Linux tels que **cd**, **ls**, **ip**

</div>

</div><div class='flex'>

<div class='block'>
<div class='block-icon'>
<b>Le matériel</b>
</div>

Des composants matériel tels que :

- mémoire vive, processeur, disque dur
- carte graphique, carte réseau, clavier

</div>

</div></div>

<b class='important'><i class='fas fa-warning'></i> Le rôle du système d'exploitation est d'assurer que les éléments matériels, requis par les logiciels en cours d'exécution, soient utilisés de manière partagée, équilibrée et sûre.</b>

</hr>

**Visualisons la vidéo suivante qui explique :**

- la gestion virtualisée de la mémoire
- le contrôle de l'exécution via l'ordonnanceur

https://www.lemonde.fr/blog/binaire/2017/06/14/podcast-systeme-dexploitation/

---

## **03** Représentation de l'information

Toutes les informations que l'ordinateur manipule sont codées en binaire (une suite de 0 et 1) :

- les entiers naturels et relatifs
- les nombres décimaux dits à virgule flottante,
- les caractères (ASCII, unicode)
- les données multimédias (son, image, vidéo, page web...)
- les programmes...

</br>
</hr>
</br>

**Lisons le billet ci-dessous sur le codage binaire**
https://interstices.info/nom-de-code-binaire/

---

## **04** Système de fichiers

**Définition**
Un **système de fichiers** est une structure utilisée par un système d'exploitation pour organiser et gérer les fichiers sur un appareil de stockage tel qu'un disque dur, un SSD ou une clé USB.

**Explications**
Le terme système de fichiers désigne à la fois l'organisation des informations mémorisées sur les périphériques de stockage de l'ordinateur et la vue logique hiérarchique présentée à l'utilisateur. Les informations sont stockées dans des paquets appelées fichiers, écrits dans un certain format, c'est-à-dire selon une certaine manière d'encoder les informations en binaire. Ces fichiers peuvent être aussi bien du texte, une page web, un morceau de musique, une photo de vacance, un script, un logiciel, etc. Un répertoire regroupe des fichiers ou d'autres répertoires, ce qui aboutit à une hiérarchie de fichiers. C'est le chemin d'accès qui permet de localiser un fichier de la hiérarchie.

Vous maîtrisez ce qu'est un fichier, un répertoire (= dossier), un chemin d'accès, un lien symbolique, le répertoire courant ? Si oui, passez à la suite. Si non, jouez à Find your path pour vous familiariser avec la représentation des chemins dans les environnements de type unix. Si vous avez joué déjà 20 minutes et que vous ne voyez pas le rapport avec ce qui précède, contactez l'enseignant.

---

## **05** Interpréteur de commandes

La **console** est une interface textuelle qui permet à un utilisateur de demander à l'ordinateur de réaliser certaines tâches, uniquement à l'aide d'un écran et d'un clavier.

<div class='flex-horizontal'><div class='flex'>

**Sur un serveur sans interface graphique**
La console est généralement directement accessible au démarrage.

</div><div class='flex'>

**Sur une machine grand public**
On utilise un émulateur de terminal

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Dans Windows, l'émulateur de terminal s'appelle **Powershell** et est disponible sur toutes les machines.

</div>

</div></div>

---

## **05** Interpréteur de commandes

Une fois dans le terminal, l'utilisateur n'a qu'à écrire au clavier la commande qu'il souhaite que le système d'exploitation exécute.

Quelques commandes UNIX utiles

- **cd** (change directory) : changer d'emplacement dans le système de fichier
- **ls** (list) : affiche les éléments d'un dossier
- **cp** (copy) : copie un fichier
- **rm** (remove) : supprimer un fichier ou un dossier

<div class='block note'>

<i class='block-icon fas fa-info'></i>

Une commande n'est autre qu'un fichier exécutable. Sous Linux, les commandes les plus courantes sont placés dans le dossier `/bin`

</div>
