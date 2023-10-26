---
marp: true
theme: dav-default
---

<style>
:root {
    background-color:#FFF;
    font-size: 10px;
}
    </style>

<div class="mermaid">
%%{init: {'theme': 'base',
    'themeVariables': {
      'primaryColor': '#fff',
      'primaryTextColor': '#1f1b30',
      'primaryBorderColor': '#FF2453',
      'lineColor': '#1f1b30',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff',
      'fontFamily':'verdana',
      'fontSize':'300%'
    }, 
    "flowchart" : { "curve" : "basis" } 
} }%%
classDiagram
    class maVoiture["maVoiture : CitroenC3"] {
        id = 1
        maxSpeed = 220
        year = 2013
        currentSpeed = 0
    }

</div>
