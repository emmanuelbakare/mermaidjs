:::mermaid
 
stateDiagram-v2
    state1: Design  state
    state2: Car Production
    [*] --> state1
    state1 --> state2: transport logistics
    state2 --> [*]

    note right of state1
        1. Prototype drawn on a sheet
        2. Design in a 3D software
        3. Approved by Manager
    end note

    note left of state2: Design schematic is fed into 3D printer.