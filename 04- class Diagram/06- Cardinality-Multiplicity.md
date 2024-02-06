:::mermaid


classDiagram
   
    class Animal{
        - age: int
        + makeSound() void
    }

    class Mammal {
        # furColor string
        - giveBirth() void
    }

    class Reptile {
        # scaleType string
        + layEggs() void
    }

    class Dog {
        # breed string
        + bark() void
    }

    class Dolphin {
        + swim() void
    }

    class Platypus {
    # poisonous: boolean
    + swim() void
    }


   
    Animal <|-- Mammal : Inheritance 
    Animal <|-- Reptile : Inheritance
    Mammal "0" o-- "*"  Dog : aggregation
    Mammal "1" *-- "*" Dolphin  :Composition 
    Reptile"1" *-- "n" Platypus :Composition 