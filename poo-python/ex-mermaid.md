---
marp: true
theme: custom
---

<pre class="mermaid">
%%{init: {'theme': 'base',
    'themeVariables': {
      'primaryColor': '#fff',
      'primaryTextColor': '#1f1b30',
      'primaryBorderColor': '#FF2453',
      'lineColor': '#1f1b30',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff',
      'fontFamily':'verdana'
    }, "flowchart" : { "curve" : "basis" } } }%%
classDiagram
    class CitroenC3 {
        -id: int
        -maxSpeed: int 
        -year: int
        -currentSpeed: int 
        +accelerate(): void
        +turnLeft(deg: int): void
        +turnRight(deg: int): void
    }
</pre>


<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });

window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>