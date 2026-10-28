print("MULTI-DAY WATER TANK SIMULATION")

capacity = int(input("Enter tank capacity in litres: "))
water_level = int(input("Enter initial water level: "))
target = int(input("Enter target water level: "))
days = int(input("Enter number of days: "))

target_day = 0

if capacity <= 0 or water_level < 0 or water_level > capacity:
    print("Invalid tank capacity or initial water level")

elif target < 0 or target > capacity or days <= 0:
    print("Invalid target level or number of days")

else:
    for day in range(1, days + 1):
        inflow = int(input("Enter water inflow: "))
        outflow = int(input("Enter water outflow: "))

        if inflow < 0 or outflow < 0:
            print("Invalid water quantity")
            break

        water_level = water_level + inflow - outflow

        if water_level > capacity:
            overflow = water_level - capacity
            print("Overflow:", overflow, "litres")
            water_level = capacity

        if water_level < 0:
            print("Water shortage:", abs(water_level), "litres")
            water_level = 0

        print("Day", day, "water level:", water_level, "litres")

        if water_level >= target and target_day == 0:
            target_day = day

    if target_day > 0:
        print("Target first reached on day:", target_day)
    else:
        print("Target threshold was not reached")
