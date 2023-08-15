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
    class Restaurant {
    }

    class Client
    class  Employee

    Restaurant *-- Service
    Restaurant *-- Employee

    Service o-- "0..20" Client
    Client <|-- FoodCritic
    Client -- "1..*" Bill : concerne
    Client o-- "1..*" Reservation
    Bill -- Payment

    Payment <|-- Cash
    Payment <|-- Check
    Payment <|-- Card


    Employee <|-- Waiter
    Employee <|-- Chef
    Waiter -- Client

</div>

