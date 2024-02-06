:::mermaid

    %%state "Car Design" as Design
    Design: Car Design
    %%direction LR
    [*] --> Design 
    Design --> Produce: activate design
    Produce --> [*]