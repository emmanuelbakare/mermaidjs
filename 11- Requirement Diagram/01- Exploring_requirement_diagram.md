:::mermaid

requirementDiagram
    %% requirements, elements, relationship
    %% requirements can be 
        %%requirement, functionalRequirement, 
        %%interfaceRequirement, performanceRequirement, 
        %%physicalRequirement, designConstraint
    %% Risk options: Low, Medium, High
    %%verificationmethod: Analysis, Inspection, Test, Demonstration
    %% Relationship: contains, copies, derives, satisfies, verifies, refines, or traces.
    requirement req1 {
        id: 1
        text: user text
        risk: Low
        verifymethod: Analysis

    }

    element elem1 {
        type: simulation
        docref: github.com/all_the_tests
    }

    req1 -satisfies-> elem1

