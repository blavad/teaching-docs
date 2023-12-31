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
    class User {
      - username: string
      - avatar: string
      - email: string
    }

    class Screen {
      - id: string
      - name: string
      - isActive: boolean
    }

    class Site

    class Client

    class PaymentMethod


    class PaymentManager {
      + payBill(method:PaymentMethod, bill: Bill)
    }


    User o-- Site

    Client <|-- Aeroport
    Client <|-- Cinema

    PaymentMethod <|-- CreditCard

</div>

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
    direction TB
    class Client
    class Staff
    class Service

    Team o-- Staff
    Person <|-- Staff
    Person <|-- Client

    Team -- Manager
    Staff <|-- Manager
    Staff <|-- Dresser

    Service *-- "*" Reservation
    Client o-- Reservation
    Client <|-- FoodCritic
    Client -- Bill
    Service "0..1" -- "0.1" Service : précède >

</div>
