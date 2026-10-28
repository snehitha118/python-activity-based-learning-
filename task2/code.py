units = []

for month in range(1, 4):
    usage = float(input("Enter electricity units for month " + str(month) + ": "))
    units.append(usage)

print("\n===== MONTHLY ELECTRICITY USAGE =====")

for month in range(3):
    print("Month", month + 1, ":", units[month], "units")

total = sum(units)
average = total / len(units)

print("\n===== USAGE ANALYSIS =====")
print("Total usage:", total, "units")
print("Average usage:", round(average, 2), "units")

if average < 100:
    print("Usage level: Low")
elif average < 300:
    print("Usage level: Medium")
else:
    print("Usage level: High")

highest_usage = max(units)
highest_month = units.index(highest_usage) + 1

print("Highest usage:", highest_usage, "units")
print("Month with highest usage: Month", highest_month)

print("\nAnalysis completed successfully!")
