:::mermaid

    erDiagram

    CUSTOMER ||--o{ ORDER :places
    CUSTOMER {
        int id
        string name
        string email
    }

    ORDER ||--|{ LINE-ITEM : contains

    ORDER {
        int orderId
        date datePlaced
    }

    LINE-ITEM {
        int quantity
        float price 
    }
    
    CUSTOMER }|--|| PRODUCT:purchases
    PRODUCT {
        string name
        float cost
    }

    CUSTOMER ||--|{ ADDRESS: uses
    ADDRESS {
        string street
        string city
    }


   