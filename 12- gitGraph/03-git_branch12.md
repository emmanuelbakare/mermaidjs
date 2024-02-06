:::mermaid

gitGraph
    commit
    commit
    branch PIM
    commit
    commit
    commit tag:"v0.1"
    checkout main
    commit
    commit
    merge PIM
    commit
    branch Leave-Mgt
    commit
    commit tag:"v0.1"
    checkout main
    merge Leave-Mgt
    checkout Leave-Mgt
    commit


