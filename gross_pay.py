# Prompt the user for weekly hours worked and hourly rate
weeklyHours = float(input("Weekly hours worked? "))
hourlyRate = float(input("Hourly pay rate? "))

# Calculate gross pay
grossPay = weeklyHours * hourlyRate
grossPay = round(grossPay, 2)

# If user worked more than 40 hours in the week, calculate overtime pay
if weeklyHours > 40:
    grossPay = hourlyRate * 40
    overHours = weeklyHours - 40
    overPay = overHours * (hourlyRate * 1.5)
    grossPay += overPay
    overPay = str(overPay)

# Stringify gross pay
grossPay = str(grossPay)


# Print gross pay
if weeklyHours > 40:
    print("Your gross pay is: $" + grossPay + ". This includes $" + overPay + " of overtime pay.")
else:
    print("Your gross pay is: $" + grossPay)