number_of_months = int(input("Enter number of months: "))

previous_bill = 0

for month in range(1, number_of_months + 1):
    print("\nMonth", month)

    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units. Enter a non-negative value.")
        continue

    
    if units <= 100:
        energy_charge = units * 1.50
    elif units <= 200:
        energy_charge = (100 * 1.50) + ((units - 100) * 2.50)
    else:
        energy_charge = (
            (100 * 1.50)
            + (100 * 2.50)
            + ((units - 200) * 4.00)
        )

   
    if units > 300:
        energy_charge += energy_charge * 0.05
    elif units <= 100:
        energy_charge -= energy_charge * 0.05

    fixed_charge = 50
    total_bill = energy_charge + fixed_charge

    print("Units consumed:", units)
    print("Energy charge: Rs.", round(energy_charge, 2))
    print("Fixed charge: Rs.", fixed_charge)
    print("Total electricity bill: Rs.", round(total_bill, 2))

    
    if month > 1 and previous_bill > 0:
        increase = ((total_bill - previous_bill) / previous_bill) * 100

        if increase > 20:
            print("Warning: Unusual increase in electricity bill!")
        else:
            print("No unusual increase in electricity bill.")

    previous_bill = total_bill
