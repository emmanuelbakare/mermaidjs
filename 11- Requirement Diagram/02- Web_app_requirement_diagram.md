:::mermaid


requirementDiagram

    requirement Web_App {
    id: 1
    text: Sample web application
    risk: High
    verifymethod: Inspection
    }

    requirement Responsive {
    id: 1.1
    text: Application should support mobile and desktop screens
    risk: Medium
    verifymethod: Test
    }

    requirement User_Auth {
    id: 2
    text: Enable user signup and login
    risk: High
    verifymethod: Analysis
    }

    requirement DB_Access {
    id: 3
    text: Application requires access to a SQL database
    risk: Low
    verifymethod: Inspection
    }

    element Frontend {
    type: SPA
    docRef: specs/frontend.pdf
    } 

    element Backend {
    type: NodeJS REST API
    docRef: specs/backend.pdf
    }

    element DB {
    type: PostgreSQL 12
    docRef: admin/db_schema.sql
    }

    Frontend - satisfies -> Responsive
    Backend - satisfies -> User_Auth
    DB - satisfies -> DB_Access
    Web_App - contains -> Responsive
    Web_App - contains -> User_Auth
    Web_App - contains -> DB_Access