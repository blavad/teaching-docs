---
marp: true
theme: dav-default
---

<style>
:root {
background-color:#FFF;
}
</style>

<div class='mermaid'>
%%{init: {'theme': 'base',
'themeVariables': {
'primaryColor': '#fff',
'primaryTextColor': '#1f1b30',
'primaryBorderColor': '#FF2453',
'lineColor': '#1f1b30',
'secondaryColor': '#006100',
'tertiaryColor': '#fff',
'fontFamily':'verdana',
'fontSize':'100%'
}, 
'flowchart' : { 'curve' : 'basis' } 
} }%%
classDiagram
    direction RL
    Class1 "1" -- "*" Class2

</div>
