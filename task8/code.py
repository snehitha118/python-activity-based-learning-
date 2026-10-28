products = ["Notebook", "Pen", "Bag"]
prices = [50, 10, 500]
quantities = [4, 5, 1]

budget = float(input("Enter your shopping budget: "))
total_cost = 0

print("\n----- SHOPPING BILL -----")

for i in range(len(products)):
    cost = prices[i] * quantities[i]
    total_cost += cost
    print(products[i], "- Cost:", cost)

print("\nTotal cost:", total_cost)

if total_cost >= 500:
    discount = total_cost * 0.10
else:
    discount = 0

final_cost = total_cost - discount

print("Discount:", round(discount, 2))
print("Final cost:", round(final_cost, 2))

if final_cost <= budget:
    print("Shopping is within budget.")
else:
    print("Shopping exceeds budget.")
    print("Reduce the quantity of some products.")
