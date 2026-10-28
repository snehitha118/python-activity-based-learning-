ATM TRANSACTION SEQUENCE SIMULATION


1. Problem Statement

Develop a Python program to process a sequence of deposits and withdrawals in a simulated bank account. The program should maintain the account balance, enforce withdrawal limits, reject invalid transactions, and generate a transaction summary.


2.Algorithm:

1. Start the program.
2. Input the initial account balance.
3. Input the withdrawal limit.
4. Input the sequence of deposit and withdrawal transactions.
5. Initialize the successful and rejected transaction counters to zero.
6. Process each transaction in the sequence.
7. If the transaction is a deposit, check whether the amount is greater than zero.
8. If the deposit amount is valid, add it to the account balance and increase the successful transaction counter. Otherwise, reject it and increase the rejected transaction counter.
9. If the transaction is a withdrawal, check whether the amount is positive, does not exceed the withdrawal limit, and is within the available balance.
10. If the withdrawal is valid, subtract the amount from the account balance and increase the successful transaction counter. Otherwise, reject it and increase the rejected transaction counter.
11. Repeat until all transactions have been processed.
12. Display the successful transactions, rejected transactions, and final account balance.
13. Stop the program.


3.Flowchart:
    A([Start]) --> B[/Enter initial balance and withdrawal limit/]
    
    B --> C[Set successful = 0 and rejected = 0]
    
    C --> D{More transactions?}

    D -- Yes --> E[/Read transaction type and amount/]
    
    E --> F{Amount <= 0?}

    F -- Yes --> G[Reject invalid amount]
    
    G --> H[Increase rejected counter]

    F -- No --> I{Transaction type?}

    I -- Deposit --> J[Add amount to balance]
    
    J --> K[Increase successful counter]

    I -- Withdrawal --> L{Amount <= balance AND amount <= limit?}
    
    L -- Yes --> M[Subtract amount from balance]
    
    M --> K
    
    L -- No --> N[Reject transaction]
    
    N --> H

    I -- Invalid type --> O[Reject invalid transaction type]
    
    O --> H

    K --> D
    
    H --> D

    D -- No --> P[/Display successful count, rejected count and final balance/]
    
    P --> Q([End])

    4.Sample input:

    Enter initial balance: 10000
    
Enter withdrawal limit: 3000

5.Sample output:

Transaction: deposit 2000

Deposit successful

Transaction: withdrawal 1000

Withdrawal successful

Transaction: withdrawal 5000

Transaction rejected: Limit or balance exceeded

Transaction: deposit 0

Transaction rejected: Invalid amount

Transaction: withdrawal 500

Withdrawal successful

----- TRANSACTION SUMMARY -----

Successful transactions: 3

Rejected transactions: 2

Final account balance: 10500.0

