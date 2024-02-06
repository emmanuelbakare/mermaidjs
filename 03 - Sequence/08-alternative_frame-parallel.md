:::mermaid

sequenceDiagram
    par Alice to Bob
        Alice->>Bob: Hello Guys!
    and Alice to John
        Alice->>John: Hello Guys!
        par John to Charlie
            John->>Charlie: Can we go?
        and John and Diana
            John->>Diana: Can we go?
        and John to Jane
            John->>Jane: Can we go?
        end
    end
    Bob--)Alice: Hi Alice!
    John--)Alice: Hi Alice!