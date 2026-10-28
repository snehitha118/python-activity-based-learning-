TASK-10
PROGRESSIVE ELECTRICITY BILLING

1. Problem Statement:

Develop a Python program to calculate household electricity bills based on the number of units consumed using progressive billing slabs. The program should include fixed charges, surcharges, and rebates where applicable. It should also compare electricity bills across multiple months and identify unusual increases in consumption charges.


2.Algorithm:

Step 1: Start the program.

Step 2: Define the electricity billing rates for each consumption slab:

- First 100 units: ₹1.50 per unit
- Next 100 units: ₹2.50 per unit
- Above 200 units: ₹4.00 per unit

Step 3: Set the fixed charge to ₹50.

Step 4: Ask the user to enter the number of months to be compared.

Step 5: For each month, enter the electricity units consumed.

Step 6: Calculate the energy charge using the progressive billing slabs.

Step 7: If consumption exceeds 300 units, add a 5% surcharge to the energy charge. If consumption is 100 units or less, apply a 5% rebate to the energy charge.

Step 8: Add the fixed charge and calculate the final electricity bill.

Step 9: Display the monthly consumption, energy charge, and final bill.

Step 10: Compare each month's bill with the previous month's bill. If the bill increases by more than 20%, display an unusual increase warning.

Step 11: Repeat the process for all the months entered.
Step 12: Stop the program.


3.Flowchart:

    A([Start]) --> B[/Enter number of months/]
    
    B --> C[Set month = 1 and previous bill = 0]
    
    C --> D{More months?}
    
    D -- Yes --> E[/Enter units consumed/]
    
    E --> F{Units < 0?}
    
    F -- Yes --> G[Display invalid units]
    
    G --> H[Skip to next month]
    
    F -- No --> I{Units <= 100?}
    
    I -- Yes --> J[Calculate energy charge at Rs. 1.50 per unit]
    
    I -- No --> K{Units <= 200?}
    
    K -- Yes --> L[Calculate first 100 units at 1.50 and remaining at 2.50]
    
    K -- No --> M[Calculate tiered charge up to 200 units and remaining at 4.00]
    
    J --> N{Units > 300?}
    
    L --> N
    
    M --> N
    
    N -- Yes --> O[Add 5 percent surcharge]
    
    N -- No --> P{Units <= 100?}
    
    P -- Yes --> Q[Apply 5 percent reduction]
    
    P -- No --> R[No energy charge adjustment]
    
    O --> S[Add fixed charge of Rs. 50]
    
    Q --> S
    
    R --> S
    
    S --> T[Display monthly bill]
    
    T --> U{Previous valid bill exists?}
    
    U -- Yes --> V[Calculate percentage increase]
    
    V --> W{Increase > 20 percent?}
    
    W -- Yes --> X[Display unusual increase warning]
    
    W -- No --> Y[Display no unusual increase]
    
    X --> Z[Update previous bill and month]
    
    Y --> Z
    
    U -- No --> Z
    
    H --> AA[Move to next month]
    
    Z --> AA
    
    AA --> D
    
    D -- No --> AB([End])

    4.Sample input:

    Enter number of months: 3

Month 1
Enter electricity units consumed: 80

Month 2
Enter electricity units consumed: 150

Month 3
Enter electricity units consumed: 320

5.Sample output:

Month 1
Units consumed: 80.0
Energy charge: Rs. 114.0
Fixed charge: Rs. 50
Total electricity bill: Rs. 164.0

Month 2
Units consumed: 150.0
Energy charge: Rs. 275.0
Fixed charge: Rs. 50
Total electricity bill: Rs. 325.0
Warning: Unusual increase in electricity bill!

Month 3
Units consumed: 320.0
Energy charge: Rs. 966.0
Fixed charge: Rs. 50
Total electricity bill: Rs. 1016.0
Warning: Unusual increase in electricity bill!
