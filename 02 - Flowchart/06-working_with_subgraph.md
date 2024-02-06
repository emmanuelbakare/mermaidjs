::: mermaid

graph LR
    subgraph one[single]
        A1
    end

    subgraph multiple
        direction LR 
        subgraph two[double]
        B1-->B2 
        end

        subgraph three[triple]
            direction LR
            C1-->C2 & C3
        end
    end

    one-->multiple
    two-->three
    B2--> C1

