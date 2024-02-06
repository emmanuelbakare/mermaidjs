:::mermaid

stateDiagram

    classDef notMoving fill:white
    classDef movement font-style:italic
    classDef badBadEvent fill:#f00,color:white,font-weight:bold,stroke-width:2px,stroke:yellow
    classDef run fill:green,color:white
    [*]--> Still
    Still --> [*]
    Still --> Moving
    Moving --> Still
    Moving --> Running:::run
    Running --> Crash
    Crash --> [*]

    class Still notMoving
    class Moving movement
    class Crash badBadEvent
    %%class Running run
    direction LR
   
     