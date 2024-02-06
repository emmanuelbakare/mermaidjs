:::mermaid

gitGraph
    commit
    commit
    branch PIM
    commit
    commit
    commit tag:"v0.1"
    checkout main
    merge PIM
    commit
    commit
    branch Leave-Mgt
    commit
    commit
    commit tag:"v0.1"
    checkout main
    merge Leave-Mgt
    checkout Leave-Mgt
    commit
    commit
    checkout PIM
    commit id: "cherry1"
    commit
    checkout main
    cherry-pick id:"cherry1"
     

    

    