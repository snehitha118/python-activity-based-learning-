categories = []
amounts = []

n = int(input("Enter the number of expenses: "))

for i in range(n):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))

    categories.append(category)
    amounts.append(amount)

print("\n===== PERSONAL EXPENSE DETAILS =====")

for i in range(n):
    print(categories[i], ":", amounts[i])

total = sum(amounts)
average = total / n

print("\n===== EXPENSE ANALYSIS =====")
print("Total expenses:", round(total, 2))
print("Average expense:", round(average, 2))

highest = max(amounts)
index = amounts.index(highest)

print("Highest expense category:", categories[index])
print("Highest expense amount:", round(highest, 2))

if total < 1000:
    print("Spending level: Low")
elif total < 5000:
    print("Spending level: Medium")
else:
    print("Spending level: High")

print("\nAnalysis completed successfully!")
