:::mermaid

%%{
    init:{
        "theme":"default",
        "themeVariables": {
            "xyChart":{
                "titleColor": "#ff0000"
            }
            
        }
    }
}%%
xychart-beta
    title "Sales Revenue"

    x-axis "Months of the Year" [jan, feb, mar, apr]
    y-axis "Revenue (in $)" 4000 --> 11000

    line [5600, 7000, 9000, 6800]
    bar [5600, 7000, 9000, 6800]