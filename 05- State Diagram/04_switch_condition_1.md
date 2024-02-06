:::mermaid

stateDiagram-v2
    state condition <<choice>>
     
    [*] --> input
    input--> condition
    condition --> Yes:  x >5 
    condition --> No:  x < 5
   