
MULTI-DAY WATER TANK SIMULATION

1. Problem Statement

Develop a Python program to simulate water levels in a tank over multiple days. The program should update the water level based on the quantity of water entering and leaving the tank, detect overflow and water shortages, and identify the first interval in which the water level reaches a specified threshold.

2.Algorithm:

1. Start the program.
2. Enter the tank capacity.
3. Enter the initial water level.
4. Enter the target water-level threshold.
5. Enter the number of days for simulation.
6. For each day, enter the water inflow and outflow quantities.
7. Calculate the new water level by adding inflow and subtracting outflow.
8. If the water level exceeds the tank capacity, calculate the overflow and set the water level to the tank capacity.
9. If the water level becomes negative, display a water shortage and set the water level to zero.
10. Display the water level after each day.
11. Check whether the water level has reached the target threshold for the first time.
12. Display the first day on which the target is reached, or display a message if it is never reached.

 3.Flowchart:

    A([START]) --> B[/Input capacity, initial water level, target and days/]
    
    B --> C{Valid capacity and initial level?}
    
    C -->|No| D[Display invalid tank message]
    
    C -->|Yes| E{Valid target and days?}
    
    E -->|No| F[Display invalid target or days message]
    
    E -->|Yes| G[Set target_day = 0]
    
    G --> H[Start day loop]
    
    H --> I[/Input inflow and outflow/]
    
    I --> J{Are inflow and outflow non-negative?}
    
    J -->|No| K[Display invalid water quantity]
    
    K --> Z([STOP])
    
    J -->|Yes| L[Update water level]
    
    L --> M{Water level greater than capacity?}
    
    M -->|Yes| N[Calculate and display overflow]
    
    N --> O[Set water level to capacity]
    
    M -->|No| P{Water level below zero?}
    
    O --> P
    
    P -->|Yes| Q[Display water shortage and set level to zero]
    
    P -->|No| R[Display daily water level]
    
    Q --> R
    
    R --> S{Target reached for first time?}
    
    S -->|Yes| T[Record target day if not already recorded]
    
    S -->|No| U{More days remaining?}
    
    T --> U

    U -->|Yes| H
    
    U -->|No| V{target_day greater than zero?}
    
    V -->|Yes| W[Display first target day]
    
    V -->|No| X[Display target not reached]
    
    W --> Z
    
    X --> Z
    
    D --> Z
    
    F --> Z
    
4.Sample input:

    Enter tank capacity in litres: 1000
    
Enter initial water level: 400

Enter target water level: 700

Enter number of days: 3

Enter water inflow: 200

Enter water outflow: 50

Enter water inflow: 300

Enter water outflow: 100

Enter water inflow: 100

Enter water outflow: 150

5.Sample output:

MULTI-DAY WATER TANK SIMULATION

Enter tank capacity in litres: 1000

Enter initial water level: 400

Enter target water level: 700

Enter number of days: 3

Enter water inflow: 200

Enter water outflow: 50

Day 1 water level: 550 litres

Enter water inflow: 300

Enter water outflow: 100

Day 2 water level: 750 litres

Enter water inflow: 100

Enter water outflow: 150

Day 3 water level: 700 litres

Target first reached on day: 2






