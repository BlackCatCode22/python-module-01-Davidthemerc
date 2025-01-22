# Prompt the user for weekly hours worked and hourly rate
weeklyHours = float(input("Weekly hours worked? "))
hourlyRate = float(input("Hourly pay rate? "))

# Calculate gross pay
grossPay = weeklyHours * hourlyRate
grossPay = round(grossPay, 2)
grossPay = str(grossPay)

# Print gross pay
print("Your gross pay is: $" + grossPay)