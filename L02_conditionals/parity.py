# In this small project we will make the 
# logic program that will find whether the number is even or odd.

# Ask number to the user: 
num = int(input("What's a number? "))

# condition
# In notes, we have multiple arithmatic symbols for number, here we use % modulo operators to find the remainder of devision. 
# Even number always have the remainder of 0 when they are divided by 2. 

if num%2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is odd")   


# Here is the another way logic to implement the solution
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else: 
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()