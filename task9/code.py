total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
required_percentage = float(input("Enter required attendance percentage: "))

current_percentage = (attended_classes / total_classes) * 100

print("Current Attendance:", round(current_percentage, 2), "%")

if current_percentage >= required_percentage:
    print("Attendance requirement met")
    print("Additional classes required: 0")
else:
    additional_classes = 0

    while current_percentage < required_percentage:
        additional_classes += 1
        total_classes += 1
        attended_classes += 1

        current_percentage = (attended_classes / total_classes) * 100

    print("Attendance requirement can be met")
    print("Additional classes required:", additional_classes)
    print("Updated Attendance:", round(current_percentage, 2), "%")
