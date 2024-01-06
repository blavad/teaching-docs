---
marp: true
paginate: true

theme: dav-default
title: POO

footer: "POO Avancée"
_footer: ""
---

<!-- PAGE DE COUVERTURE -->
<!-- _paginate: skip -->
<!-- _class: cover -->
<div class='coverBlockCenter'><div class='coverModuleName'>Nom du cours</div><div class='coverCourseName'><span class='important'>#1 </span>Nom de la leçon</div><div class='coverAuthor'>par <span class='important'>Prénom Nom</span></div></div><img class='coverFooterLeft' height='60px' src='' /><div class='coverYear coverFooterRight'>Date</div>

---

<!-- TABLE DES MATIERES -->

## Table des matières

<b><span class='important'>01 </span>Section 1</b>
Explications

<b><span class='important'>02 </span> Section 2</b>
Explications

<b><span class='important'>03 </span> Section 3</b>
Explications

## <!-- FIN TABLE DES MATIERES -->

<!-- PARTIE 01 : Section 1 -->

<div class='main'>

# 01

## Section 1

</div>

---

## Slides come here

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. .

<div class='flex-horizontal'><div class='flex'>

<b class='important'>Definition</b>
Excepteur sint occaecat cupidatat non proident, **sunt in** culpa qui officia deserunt mollit anim id est laborum.

<div class='block note'>

<i class='block-icon fas fa-info'></i>

# Note

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

</div>

</div><div class='flex'>

<b class='important'>Example</b>

```python
class MyClass:
    def __init__():
        # Init a class

    def method():
        # method implementation
```

<div class='block warning'>

<i class='block-icon fas fa-exclamation'></i>

Duis aute irure dolor in reprehenderit.

</div>

</div></div>

---

<!-- PARTIE 02 : Section 2 -->

<div class='main'>

# 02

## Section 2

</div>

---

## Slides come here

### **subtitle**

---

<!-- PARTIE 03 : Section 3 -->

<div class='main'>

# 03

## Snippets

</div>

---

## Snippets

- **emph** et **emphi** : Texte en couleur (bold ou italic)
- **binfo** : block d'information
- **bwarn** : block de warning
- **bstd** : block standard
- **bdef-title** : block de définition
- **slide** : nouvelle slide vierge
- **section** : nouvelle section
- **cover** : nouvelle page de couverture
- **table-of-content** : table des matières
- **lay-h2** : 2 colonnes
- **lay-h2-custom** : 2 colonnes de taille inégales
- **lay-h3** : 3 colonnes
- **lay-h4** : 4 colonnes

<script type='module'>
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });
window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>
