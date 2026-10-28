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

... 
   flowchart:

   
    A([START]) --> B[Initialize empty list: units = []]
    
    B --> C[/Input electricity units for 3 months/]
    
    C --> D[Display monthly electricity usage]
    
    D --> E[Calculate total and average usage]
    
    E --> F{Check average usage}
    
    F -->|Average < 100| G[Usage Level: Low]
    
    F -->|Average < 300| H[Usage Level: Medium]
    
    F -->|Average >= 300| I[Usage Level: High]
    
    G --> J[Find highest usage and month]
    
    H --> J
    
    I --> J
    
    J --> K[Display analysis report]
    
    K --> L([STOP])
    
    ...

    
Sample input:

  Enter electricity units for month 1: 120
  
Enter electricity units for month 2: 250

Enter electricity units for month 3: 180

sample output:

===== MONTHLY ELECTRICITY USAGE =====


Month 1 : 120.0 units

Month 2 : 250.0 units

Month 3 : 180.0 units

===== USAGE ANALYSIS =====

Total usage: 550.0 units
Average usage: 183.33 units
Usage level: Medium
Highest usage: 250.0 units
Month with highest usage: Month 2

Analysis completed successfully!
