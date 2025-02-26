def main():
    x = get_int("What's value of x? ")
    print(f"X is {x}")
          
# Exception with numbers
def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) 
        except ValueError: 
            # print("X is not an Integer.")
            pass # silently ignore the current iteration

# calling the main function
main()

# This is not going to be the reason of ValueError.
# when you input "string" in x. the valueError can be applied. 

# This code snippets that try to handle any error occurring when taking the input 
# from the user. If any occurs, then handle the error with printing X is not an integer.
