:::mermaid

erDiagram
   Person [Customer] {
        int PID PK "Person Identification"
        string Name "Name of Person"
        int Age
        string Address
   }    

   Person ||--|{ Address: contains

   Address ["Home Address"] {
        string Street
        string City
        string State
        int zipcode
        int owner PK,FK
   }
   
    