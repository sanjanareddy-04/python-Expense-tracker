total = 0

while True:
    expense = float(input("Enter expense (or 0 to finish): "))

    if expense == 0:
        break

    total = total + expense

print("Total Spent:", total)