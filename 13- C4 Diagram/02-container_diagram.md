:::mermaid 

C4Container
    title C4 Container diagram for Internet Banking System

    Person(customer, Customer,"A customer of the bank...", $tags="V1.0")
    System_Ext(email_system,"E-Mail System","A customer of the bank, with personal bank accounts",, $tags="V1.0")
    System_Ext(banking_system,"Mainframe Banking System","descr", , $tags="V1.0")

    Container_Boundary(C1, "Internet Banking System"){
        Container(web_app,"Web Application","Java, Spring MVC","Delivers the static content and the Internet banking SPA")
        Container(spa,"Single-Page App","JavaScript, Angular","Provides all the Internet banking functionality to cutomers via their web browser")
        Container_Ext(mobile_app, "Mobile App","C#, Xamarin","Provides a limited subset of the Internet banking functionality to customers via their mobile device")
        ContainerDb(database,"Database","SQL Database","Stores user registration information, hashed auth credentials, access logs, etc.")
        ContainerDb_Ext(backend_api, "API Application","Java, Docker Container", "Provides Internet banking functionality via API")
    }

    Rel(customer, web_app, "Uses","HTTPS")
    Rel(customer, spa, "Uses", "HTTPS")
    UpdateRelStyle(customer, spa, $offsetX="-170", $offsetY="-70")
    Rel(customer, mobile_app, "Uses")

    Rel(web_app, spa, "Delivers")
    Rel(spa, backend_api, "Uses", "async, JSON/HTTPS")
    Rel(mobile_app, backend_api, "Uses", "async, JSON/HTTPS")
    Rel_Back(database, backend_api, "Reads from and writes to", "sync, JDBC")

    Rel(email_system, customer, "Sends e-mails to")
    Rel(backend_api, email_system, "Sends e-mails using", "sync, SMTP")
    Rel(backend_api, banking_system, "Uses", "sync/async, XML/HTTPS")
    UpdateRelStyle(backend_api, banking_system,$offsetY="-170")
    
  
    