# Import datetime
from datetime import datetime

# Accept name as input for variable userName
userName = input("What is your name? ")

# Get the time
time = datetime.now()
hour = time.hour

# Print Greeting
print("Hello " + userName + ".")