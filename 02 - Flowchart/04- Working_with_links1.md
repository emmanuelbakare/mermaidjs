::: mermaid
flowchart TB
    %% A --> B
    %% C --- D
    %% E --text here--- F
    %% G --text here --> H
    %% I -->|text here| J
    %% K ---|text here| L
    %% A-.text here.->B
    %% C-.text here.-D
    %% A --> B
    %% C ==>|text here| D
    %% F == some text === G
    %% A
    %% B
    %% A ~~~|text here| B
    %% A((Juvenile))--> B((Adult))--> C((Eggs))-->D((tadpole))-->A
    %% a --> b & c--> d
    %% A & B--> C & D
    A --x C
    A --o D
    B <--> C
    B o--o D
    C-->F-->H
    A<---->G
    
    