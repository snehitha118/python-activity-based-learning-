TASK-5


EMPLOYEE SALARY AND BONUS CALCULATION

1. Problem Statement:

Develop a Python program to calculate an employee's monthly salary by considering basic salary, allowances, deductions, and performance-based bonuses. The program should calculate the final salary and display a clear salary summary.


2. Algorithm:

Step 1: Start the program.

Step 2: Input the employee's name, basic monthly salary, and performance rating.

Step 3: Check whether the basic salary is non-negative and the performance rating is between 1 and 5.

Step 4: Calculate House Rent Allowance (HRA) as 20% of the basic salary.

Step 5: Calculate Travel Allowance as 10% of the basic salary.

Step 6: Calculate deductions as 5% of the basic salary.

Step 7: Calculate the bonus based on the performance rating:

- Rating 5: 15% bonus
- Rating 4: 10% bonus
- Rating 3: 5% bonus
- Rating below 3: No bonus

Step 8: Calculate gross salary by adding the basic salary, HRA, travel allowance, and bonus.

Step 9: Calculate the final salary by subtracting deductions from the gross salary.

Step 10: Display the employee's name, allowances, bonus, deductions, and final monthly salary.

Step 11: Stop the program.

3.Flowchart:

    A([START]) --> B[/Input employee name, basic salary and performance rating/]
    
    B --> C{Salary >= 0 and rating between 1 and 5?}
    
    C -->|No| D[Display invalid input message]
    
    D --> Z([STOP])
    
    C -->|Yes| E[Calculate HRA, travel allowance and deductions]
    
    E --> F{Performance rating?}
    
    F -->|5| G[Bonus = 15% of basic salary]
    
    F -->|4| H[Bonus = 10% of basic salary]
    
    F -->|3| I[Bonus = 5% of basic salary]
    
    F -->|1 or 2| J[Bonus = 0]
    
    G --> K[Calculate gross salary]
    
    H --> K
    
    I --> K
    
    J --> K
    
    K --> L[Calculate final salary after deductions]
    
    L --> M[Display salary summary]
    
    M --> Z
    
4.Sample input:

    Enter employee name: Ravi
    
Enter basic monthly salary: 30000

Enter performance rating (1-5): 5

5.Sample output:

----- Salary Summary -----

Employee Name: Ravi

Basic Salary: Rs. 30000.0

HRA: Rs. 6000.0

Travel Allowance: Rs. 3000.0

Bonus: Rs. 4500.0

Deductions: Rs. 1500.0

Final Monthly Salary: Rs. 42000.0






