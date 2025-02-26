
def main():
    name = input("What's your name? ")
    hello(name) # call the function with the argument "name"

# Create the function using the def keyword: Custom Function
def hello(to = "world"): # give the default value to "to"
    print(f"Hello, {to}")

# Call the main function (inside which hello() function will be called. )
main()