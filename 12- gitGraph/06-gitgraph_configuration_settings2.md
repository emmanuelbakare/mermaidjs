:::mermaid

%%{
    init:{
        "theme":"default",
        "gitGraph":{
            "showBranches":true,
            "showCommitLabel":true,
            "rotateCommitLabel":true,
            "mainBranchName":"Default"
        }
    }

}%%
gitGraph LR:
    commit type:HIGHLIGHT
    commit tag: "v1.0"
    branch One
    branch Two
    commit
    commit tag: "v2.0"
    branch Three
    commit
    checkout Two
    commit
    checkout Default
    commit
    commit tag: "v2.1"
    checkout One
    commit
    checkout Three
    commit tag: "v3.0"
    



