print("SMART PARKING FEE MANAGEMENT")

vehicle = input("Enter vehicle category (bike/car): ").lower()

entry = int(input("Enter entry hour (0-23): "))
exit_time = int(input("Enter exit hour (0-23): "))

if entry < 0 or entry > 23 or exit_time < 0 or exit_time > 23:
    print("Invalid time input")

elif exit_time == entry:
    print("Parking duration cannot be zero")

else:
    if exit_time < entry:
        duration = (24 - entry) + exit_time
    else:
        duration = exit_time - entry

    if vehicle == "bike":
        rate = 10
    elif vehicle == "car":
        rate = 20
    else:
        rate = 0

    if rate == 0:
        print("Invalid vehicle category")
    else:
        fee = duration * rate

        if duration > 24:
            fee = 500

        if exit_time < entry:
            fee = fee + 50

        print("Parking duration:", duration, "hours")
        print("Parking fee: Rs.", fee)


