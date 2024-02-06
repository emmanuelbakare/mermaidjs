:::mermaid

sequenceDiagram
    Alice->>Bob: Hello Bob, how are you?
    alt is sick?
        Bob->>Alice: Not so good 
    else Not sick
        Bob->>Alice: Feeling Like a Daisy
    end

    opt Other response
        Bob->>Alice: Thanks for asking
    end