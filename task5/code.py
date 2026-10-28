employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic monthly salary: "))
performance_rating = int(input("Enter performance rating (1-5): "))

if basic_salary < 0 or performance_rating < 1 or performance_rating > 5:
    print("Invalid input. Check salary and performance rating.")

else:
    hra = basic_salary * 0.20
    travel_allowance = basic_salary * 0.10
    deductions = basic_salary * 0.05

    if performance_rating == 5:
        bonus = basic_salary * 0.15
    elif performance_rating == 4:
        bonus = basic_salary * 0.10
    elif performance_rating == 3:
        bonus = basic_salary * 0.05
    else:
        bonus = 0

    gross_salary = (
        basic_salary + hra + travel_allowance + bonus
    )
    final_salary = gross_salary - deductions

    print("\n----- Salary Summary -----")
    print("Employee Name:", employee_name)
    print("Basic Salary: Rs.", round(basic_salary, 2))
    print("HRA: Rs.", round(hra, 2))
    print("Travel Allowance: Rs.", round(travel_allowance, 2))
    print("Bonus: Rs.", round(bonus, 2))
    print("Deductions: Rs.", round(deductions, 2))
    print("Final Monthly Salary: Rs.", round(final_salary, 2))

