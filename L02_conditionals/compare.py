# Conditional statement
# Here is the simple syntax of how to use the conditional statment

# Ask the user about their age
age = int(input("What's your age? "))

if age > 18: 
    print("You are eligible to drive a car")
elif age < 18:
    print("You are NOT eligible to drive a car")
else: 
    print("I think you should appear in the G1 exam.")
