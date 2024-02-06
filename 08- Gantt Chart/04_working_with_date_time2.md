:::mermaid

gantt
    title sample Gantt Chart
    dateFormat YY-MM-DD
    axisFormat %y/%m/%d
    tickInterval 1day
    weekday  Monday 
    todayMarker off
    excludes Monday, Tuesday

    section One
        Task 11: done, a11, 24-01-01,3d
        Task 12: a12, after a11,3d
    section Two
        Task 21: crit,done,a21, 24-01-02, 2d
        Task 22: crit, 24-01-04, 2d
        Task 23: done, 2d
        Task 24: active, after a12, 4d
        
 
   

    