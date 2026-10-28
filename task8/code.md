TASK-8


MULTI-PRODUCT SHOPPING BUDGET CONSTRAINT

1. Problem Statement:

Develop a Python program to evaluate a shopping basket containing multiple products and quantities. Apply discount conditions, calculate the total shopping cost, compare it with a fixed budget, and determine which purchases must be reduced to remain within the budget


2.Algorithm:

1. Start the program.
2. Initialize the product names, prices, and quantities.
3. Enter the available shopping budget.
4. Calculate the cost of each product by multiplying its price by its quantity.
5. Calculate the total shopping cost.
6. Check the discount conditions and apply the appropriate discount.
7. Calculate the final cost after applying the discount.
8. Compare the final cost with the available budget.
9. If the final cost exceeds the budget, identify products whose quantities can be reduced.
10. Display the final shopping cost and budget status.
11. Stop the program.

    3.Flowchart:
    
    A([Start]) --> B[Initialize products, prices and quantities]
    
    B --> C[/Enter shopping budget/]
    
    C --> D[Set total_cost = 0]
    
    D --> E[Loop through all products]
    
    E --> F[Calculate cost = price x quantity]
    
    F --> G[Add cost to total_cost]
    
    G --> H{More products?}
    
    H -- Yes --> E
    
    H -- No --> I[Display total cost]
    
    I --> J{Total cost >= 500?}
    
    J -- Yes --> K[Calculate 10% discount]
    
    J -- No --> L[Set discount = 0]
    
    K --> M[Calculate final cost]
    
    L --> M
    
    M --> N{Final cost <= budget?}
    
    N -- Yes --> O[Display within budget]
    
    N -- No --> P[Display exceeds budget]
    
    P --> Q[Suggest reducing quantities]
    
    O --> R([End])
    
    Q --> R
    
4.Sample input:

    Enter your shopping budget: 1200

    5.Sample output:
    
    ----- SHOPPING BILL -----
    
Notebook - Cost: 200

Pen - Cost: 50

Bag - Cost: 500

Total cost: 750

Discount: 75.0

Final cost: 675.0

Shopping is within budget.




