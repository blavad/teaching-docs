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
Définition et explications.

<b><span class="important">02 </span> Diagramme de cas d'utilisation</b>
Quelques exemples.

<b><span class="important">03 </span> Diagramme de classes</b>
Typing. Documentation. Gestion des erreurs. Tests unitaires.


---





<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });

window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>