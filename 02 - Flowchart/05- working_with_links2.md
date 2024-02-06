::: mermaid

flowchart TB
    A([Start])-->B[/Input x/]
    B-->C{"x >5?"}
    C-..->|yes|D([stop])
    C-->|No|F[/print x /]
    F-->G[x = x+ 1]
    G-->C