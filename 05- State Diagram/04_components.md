:::mermaid 

stateDiagram-v2
    [*]--> state1
    state1 --> state2
    state1 --> state3

    state state1{
        [*]--> state11
    }

    state state2{
        [*]--> state21
    }

    state state3{
        [*]--> state31
    }

    state2 --> [*]
    state3 --> [*]
     