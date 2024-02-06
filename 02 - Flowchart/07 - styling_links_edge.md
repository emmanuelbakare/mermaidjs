%%{
    init:{
        'flowchart':{
            'curve': 'natural'
        }
    }

}%%
flowchart TB
   
    A([Start])-->B[/Input x/]
    B -->C{"x >5?"}
    C-..->|yes|D([stop])
    C-->|No|F[/print x /]:::bigger
    F-->G[x = x+ 1]:::nice 
    G:::bigger-->C 

    linkStyle 3,4,5 stroke-width:5px, stroke:#00ff00
    linkStyle 2 stroke:#ff0000

    style B color:#ffffff,font-size:18pt,fill:#00aaff

    classDef bigger font-size:15pt, stroke-width:3px
    classDef nice  font-size:17pt, stroke:red

    %% class A,C,D bigger
   
    


    
    
