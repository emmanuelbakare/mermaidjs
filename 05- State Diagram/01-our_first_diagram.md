:::mermaid

---
title: Car Design States
---
stateDiagram
    direction LR
    [*] --> Design 
    Design --> Produce
    Produce --> Assemble 
    Assemble --> Test
    Test --> Deliver
    Deliver --> [*]
