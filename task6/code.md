SMART PARKING FEE MANAGEMENT

1. Problem Statement:

Develop a Python program to calculate parking charges based on vehicle entry and exit times, vehicle categories, overnight parking, daily parking limits, and penalty conditions. The program should also validate time inputs and display the final parking fee.


2.Algorithm:

1. Start the program.
2. Enter the vehicle category.
3. Enter the vehicle entry time and exit time.
4. Validate the entered time values.
5. If the time values are invalid, display an error message.
6. Calculate the total parking duration.
7. Select the parking rate based on the vehicle category.
8. Calculate the parking fee based on the parking duration.
9. Check whether overnight charges are applicable.
10. Apply the daily parking limit.
11. Check whether any penalty conditions apply.
12. Calculate and display the final parking fee.
13. Stop the program.

3.Flowchart:

    A([START]) --> B[/Input vehicle category, entry hour and exit hour/]
    
    B --> C{Are entry and exit hours valid?}
    
    C -->|No| D[Display Invalid time input]
    
    D --> Z([STOP])
    
    C -->|Yes| E{Is exit hour equal to entry hour?}
    
    E -->|Yes| F[Display duration cannot be zero]
    
    F --> Z
    
    E -->|No| G{Is exit hour less than entry hour?}
    
    G -->|Yes| H[Calculate duration across midnight]
    
    G -->|No| I[Calculate duration = exit - entry]
    
    H --> J[Set vehicle rate]
    
    I --> J
    
    J --> K{Bike or car?}
    
    K -->|Bike| L[Rate = Rs. 10 per hour]
    
    K -->|Car| M[Rate = Rs. 20 per hour]
    
    K -->|Invalid| N[Display invalid vehicle category]
    
    N --> Z
    
    L --> O[Calculate parking fee]
    
    M --> O
    
    O --> P{Duration greater than 24 hours?}
    
    P -->|Yes| Q[Set fee = Rs. 500]
    
    P -->|No| R{Did parking cross midnight?}
    
    Q --> R
    
    R -->|Yes| S[Add Rs. 50 extra charge]
    
    R -->|No| T[Display duration and fee]
    
    S --> T
    
    T --> Z

    4.Sample input:

    SMART PARKING FEE MANAGEMENT
    
Enter vehicle category (bike/car): car

Enter entry hour (0-23): 10

Enter exit hour (0-23): 15

5.Sample output:

SMART PARKING FEE MANAGEMENT

Enter vehicle category (bike/car): car

Enter entry hour (0-23): 10

Enter exit hour (0-23): 15

Parking duration: 5 hours

Parking fee: Rs. 100

