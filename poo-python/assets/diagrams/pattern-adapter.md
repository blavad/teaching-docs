---
marp: true
theme: dav-default
---

<style>
:root {
background-color:#FFF;
font-size:10px;
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
      'fontSize':'200%'
    }, 
    "flowchart" : { "curve" : "basis" } 
} }%%
classDiagram
    class Target {
        + request()
    }

    class Adaptee {
        + special_request()
    }

    class Adapter {
        + request()
    }

    Client --> Target
    direction TB
    Target <|-- Adapter
    Adapter --> Adaptee
</div>

