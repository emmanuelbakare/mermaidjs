:::mermaid

sequenceDiagram
    box rgb(15,200,50) Frontend Interface
        participant User as "User"
        participant App as "Shopping App"
    end

    box orange Backend Interface
        participant Gateway as "Payment Gateway"
        participant Bank as "Bank"
    end

    User->>+App: Select Item and Checkout
    rect rgb(200,0,0,0.7)
    App->>+Gateway: Initiate Payment Request
    Gateway->>+Bank: Process Payment
    end
    Bank-->>-Gateway: Payment Approved
    Gateway-->>-App: Payment Success
    App-->>-User: Order Confirmed
