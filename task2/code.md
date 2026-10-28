TASK-2


ELECTRICITY USAGE ANALYSIS


Subject: Python Programming

Programming language: Python

1. Problem Statement:
Electricity consumption varies from month to month. Monitoring electricity usage helps users understand their consumption patterns and avoid unnecessary usage. The aim of this project is to develop a Python program that records electricity usage for three months, calculates the total and average consumption, classifies usage as Low, Medium, or High, and identifies the month with the highest electricity consumption.

2.Alogorithm:

1. Start the program.
2. Create an empty list to store electricity usage.
3. Enter electricity consumption for three months.
4. Store each month's usage in the list.
5. Display the monthly electricity usage.
6. Calculate the total electricity consumption.
7. Calculate the average electricity consumption.
8. Classify average usage as Low, Medium, or High.
9. Identify the highest electricity usage and its corresponding month.
10. Display the analysis results.

11. 3.flowchart:
12. 
    A([START]) --> B[/Input Customer Name and Units Consumed/]
    B --> C{Are Units Less Than or Equal to 100?}

    C -- Yes --> D[Calculate Bill Using First Slab Rate]
    C -- No --> E{Are Units Less Than or Equal to 200?}

    E -- Yes --> F[Calculate Bill Using Second Slab Rate]
    E -- No --> G[Calculate Bill Using Higher Slab Rates]

    D --> H[Calculate Total Electricity Bill]
    F --> H
    G --> H

    H --> I[/Display Customer Name, Units and Total Bill/]
    I --> J([STOP])

    4.Sample input:
    Enter Customer Name: Snehitha
Enter Units Consumed: 150

5.sample output:
Electricity Bill Analysis

Customer Name: Snehitha
Units Consumed: 150
Total Electricity Bill: ₹450

    
14. Stop the program.

