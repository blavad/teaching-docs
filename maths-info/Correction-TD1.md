---
marp: true
paginate: true

theme: dav-maths-exos
title: Correction Démonstration de cours

footer: ""
_footer: ""
---

## Correction TD1

<div class='flex-horizontal'><div class='flex'>

<b class='important'>Note : Nous ferons le reste des exercices le 22 novembre</b>

**Exercice I.1:**
Définir l'ensemble des entiers naturels strictements inférieurs à $5$.

**Solution :** $A = \left\{ x \mid  x \in \mathbb{N}\text{ et } x < 5 \right\}$ ou $A = \left\{ x \in \mathbb{N} \mid x < 5 \right\}$

**Exercice I.2:**
Définir l'ensemble des entiers relatifs divisibles par $3$ de deux façons différentes.

**Solution :**

$A = \left\{ x \in \mathbb{Z} \mid \exists k \in \mathbb{Z},\ x = 3k\right\}$

ou

$A = \left\{ 3k \mid k \in \mathbb{Z}\right\}$

ou encore (en utilisant la fonction partie entière):

$A = \left\{ x \in \mathbb{Z} \mid \frac{x}{3} =  \lfloor \frac{x}{3} \rfloor  \right\}$

**Exercice I.3:**
Définir l'ensemble des nombres impaires strictements supérieurs à $3$.

$A = \left\{ 2k+1 \mid k \in \mathbb{N}\ et\ k>0 \right\}$

**Exercice II.1**
Soient $A = \left\{1,2,3\right\}$ et $𝐵 = \left\{0,1,2,3\right\}$. Décrire les ensembles $𝐴 \cap 𝐵$, $𝐴 ∪ 𝐵$ et $𝐴 × 𝐵$.

**Solution :**

$A \cap B = \{1,2,3\}$, $A \cup B = \{0, 1,2,3\}$

$A \times B = \{(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)\}$

**Exercice II.2**
Soient $A=\{0,2,4\}$ et $B = \{1,3,4,5 \}$ dans le référentiel $E=\{0,1,2,3,4,5\}$.
Déterminer les ensembles $\overline{A}$,$\overline{B}$,$A \cap B$, $A \cup B$, $A \setminus B$, $\mathcal{P}(A)$ et $A \times B$

</div><div class='flex'>

**Exercice II.3**
Soient $A = [1, 3]$ et $B=[2,4]$. Déterminer les ensembles $A \cap B$ et $A\cup B$.

**Solution :**
$A \cap B = [2,3]$
$A \cup B = [1,4]$

**Exercice II.4**
Déterminer le complémentaire dans $\mathbb{R}$ des ensembles suivants $A_1 = ] −\infty, 0]$, $A_2 = ] −\infty, 0[$, $A_3 = ]0, +\infty[$, $A_4 = [0, +\infty[$, $A_5 =]1,2[$, $A_6 = [1,2[$

**Solution :**
$\overline{A_1} = ]0,+\infty[$
$\overline{A_2} = [0,+\infty[$
$\overline{A_3} = ]−\infty, 0]$
$\overline{A_4} = ]−\infty, 0[$
$\overline{A_5} = ]−\infty, 1] \cup [2, + \infty[$
$\overline{A_6} = ]−\infty, 1[ \cup [2, + \infty[$

**Exercice II.8 :**
Soit $C_{red} = [\![ 0; 2 ]\!],C_{green} = [\![ 0; 2 ]\!], C_{blue} = [\![ 0; 2 ]\!],$. Décrire $C_{red} \times C_{green} \times C_{blue}$.

**Solution :**
$C_{red} \times C_{green} \times C_{blue} = \left\{(0,0,0),(0,0,1),(0,0,2),(0,1,0),(0,1,1),(0,1,2),..., (2,2,0), (2,2,1), (2,2,2) \right\}$

**Exercice II.8 (complément):**
Donner l'ensemble des couleurs possibles en informatique.

**Note :** En informatique les couleurs sont codés sur 3 octets (1 octet = 8 bits = 256 valeurs possibles). Le premier octet pour le rouge, le deuxième pour le vert et le troisième pour le bleu. Chaque combinaison de 3 octets représente une couleur.

**Solution :**
Soient les ensembles $R=G=B = [\![0, 255]\!]$.

Les couleurs possibles sont :
$$R\times G\times B = \left\{(0,0,0), (0,0,1), (0,0,2), (0,0,3), ..., (255,255,254), (255,255,255)\right\}$$

## </div></div>

---

### Exercice II.9

<!-- ### **Démonstration de cours** -->

<div class='flex-horizontal'><div class='flex'>

<b class='important'>Rappel du cours</b>
Soit $E$ un ensemble, $A$ et $B$ deux parties de $E$.
**Egalité :** $A$ et $B$ sont égaux si et seulement si $A \subset B$ et $B \subset A$.
**Inclusion :** $A \subset B \Leftrightarrow \forall x\in A \Rightarrow x \in B$

<b class='important'>Démonstration 1)</b>
Soit $E$ un ensemble, $A$, $B$ et $C$ trois parties de $E$.
Montrons que $A \cup (B \cap C)= (A \cup B) \cap (A\cup C)$

Pour cela on montre qu'il y a double inclusion.

**_i)_ Montrons que $A \cup (B \cap C) \subset (A \cup B) \cap (A\cup C)$**

$x\in A \cup (B \cap C) \Rightarrow x \in A\text{ ou }(x \in B\text{ et }x \in C)$

On réalise une disjonction de cas (par rapport au **"ou"**).

<u>1er cas:</u> $x \in A \Rightarrow x \in A \cup B\text{ et }x \in A \cup C$
<u>2eme cas:</u> $x \in B  \text{ et } x \in C \Rightarrow x \in A \cup B\text{ et }x \in A\cup C$

Ainsi, $x \in A \cup (B \cap C) \Rightarrow x \in (A \cup B) \cap (A\cup C)$

On a vérifié la première inclusion $A \cup (B \cap C) \subset (A \cup B) \cap (A\cup C)$

**_ii)_ Montrons désormais que $(A \cup B) \cap (A\cup C) \subset A \cup (B \cap C)$**

$x\in (A \cup B) \cap (A\cup C) \Rightarrow (x \in A\text{ ou }x \in B)\text{ et }(x \in A\text{ ou }x \in C)$

On réalise une disjonction de cas (par rapport aux **"ou"**).

<u>1er cas:</u> $x \in A \text{ et }(x \in A\text{ ou }x \in C)$

- <u>1er sous cas:</u> $x \in A \text{ et }x \in A \Rightarrow x \in A \Rightarrow x \in A \cup (B \cap C)$
- <u>2eme sous cas:</u> $x \in A\text{ et }x \in C \Rightarrow x \in A \Rightarrow x \in A \cup (B \cap C)$

<u>2eme cas:</u> $x \in B \text{ et }(x \in A\text{ ou }x \in C)$

- <u>1er sous cas:</u> $x \in B \text{ et }x \in A \Rightarrow x \in A \Rightarrow x \in A \cup (B \cap C)$
- <u>2eme sous cas:</u> $x \in B \text{ et }x \in C \Rightarrow x \in B \cap C \Rightarrow x \in A \cup (B \cap C)$

Ainsi, $x \in (A \cup B) \cap (A\cup C) \Rightarrow x \in A \cup (B \cap C)$

On a vérifié la seconde inclusion $(A \cup B) \cap (A\cup C) \subset A \cup (B \cap C)$

La double inclusion est donc bien vérfiée et donc $A \cup (B \cap C)= (A \cup B) \cap (A\cup C)$.

</div><div class='flex'>

<b class='important'>Démonstration 2)</b>
Soit $E$ un ensemble, $A$, $B$ et $C$ trois parties de $E$.
Montrons que $A \cap (B \cup C)= (A \cap B) \cup (A\cap C)$

<b class='info'>(Démonstration que l'on réalisera au prochain cours)</b>

<!-- Pour cela on montre qu'il y a double inclusion.

**_i)_ Montrons que $A \cap (B \cup C) \subset (A \cap B) \cup (A\cap C)$**

$x\in A \cap (B \cup C) \Rightarrow x \in A\text{ et }(x \in B\text{ ou }x \in C)$

On réalise une disjonction de cas (par rapport au **"ou"**).

<u>1er cas:</u> $x \in B \Rightarrow x \in A \cap B\text{ et }x \in A \cap C$
<u>2eme cas:</u> $x \in C  \text{ et } x \in C \Rightarrow x \in A \cap B\text{ et }x \in A\cap C$

Ainsi, $x \in A \cap (B \cap C) \Rightarrow x \in (A \cap B) \cap (A\cap C)$

On a vérifié la première inclusion $A \cap (B \cap C) \subset (A \cap B) \cap (A\cap C)$

**_ii)_ Montrons désormais que $(A \cap B) \cap (A\cap C) \subset A \cap (B \cap C)$**

$x\in (A \cap B) \cap (A\cap C) \Rightarrow (x \in A\text{ ou }x \in B)\text{ et }(x \in A\text{ ou }x \in C)$

On réalise une disjonction de cas (par rapport aux **"ou"**).

<u>1er cas:</u> $x \in A \text{ et }(x \in A\text{ ou }x \in C)$

- <u>1er sous cas:</u> $x \in A \text{ et }x \in A \Rightarrow x \in A \Rightarrow x \in A \cap (B \cap C)$
- <u>2eme sous cas:</u> $x \in A\text{ et }x \in C \Rightarrow x \in A \Rightarrow x \in A \cap (B \cap C)$

<u>2eme cas:</u> $x \in B \text{ et }(x \in A\text{ ou }x \in C)$

- <u>1er sous cas:</u> $x \in B \text{ et }x \in A \Rightarrow x \in A \Rightarrow x \in A \cap (B \cap C)$
- <u>2eme sous cas:</u> $x \in B \text{ et }x \in C \Rightarrow x \in B \cap C \Rightarrow x \in A \cap (B \cap C)$

Ainsi, $x \in (A \cap B) \cap (A\cap C) \Rightarrow x \in A \cap (B \cap C)$

On a vérifié la seconde inclusion $(A \cap B) \cap (A\cap C) \subset A \cap (B \cap C)$

La double inclusion est donc bien vérfiée et donc $A \cap (B \cap C)= (A \cap B) \cap (A\cap C)$. -->

</div></div>

<script type='module'>
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });
window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>
