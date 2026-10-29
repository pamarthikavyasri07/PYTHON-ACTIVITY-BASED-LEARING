
months = int(input("Enter number of months: "))
bills = []

for month in range(1, months + 1):
    units = float(input(f"Enter units for month {month}: "))

    # Calculate progressive slab charges
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = (100 * 2) + (units - 100) * 3
    else:
        energy = (100 * 2) + (100 * 3) + (units - 200) * 5

    fixed = 50
    surcharge = energy * 0.05

    # Rebate for low consumption
    rebate = energy * 0.10 if units < 100 else 0

    bill = energy + fixed + surcharge - rebate
    bills.append(bill)

    print(f"Month {month} Bill: Rs. {bill:.2f}")

# Compare monthly bills
print("\nMonthly Bill Comparison")

for i in range(1, months):
    increase = bills[i] - bills[i - 1]

    if bills[i - 1] > 0:
        percent = (increase / bills[i - 1]) * 100
    else:
        percent = 0

    print(f"Month {i} to Month {i + 1}: "
          f"{percent:.2f}% change")

    if percent > 30:
        print("Warning: Unusual bill increase!")

print("Billing completed.")
