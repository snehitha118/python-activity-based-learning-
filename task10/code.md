PROGRESSIVE ELECTRICITY BILLING

1. Problem Statement

Develop a Python program to calculate household electricity bills based on the number of units consumed using progressive billing slabs. The program should include fixed charges, surcharges, and rebates where applicable. It should also compare electricity bills across multiple months and identify unusual increases in consumption charges.


Algorithm

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

