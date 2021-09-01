hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))

if minute > 44:
    print(hour, minute-45)
elif minute <= 44 and hour >= 1:
    print(hour-1, minute+15)
else:
    print(23, minute+15)
    