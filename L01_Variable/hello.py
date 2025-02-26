name = input("What's your name? ") # waiting for the user to type something in.

# Remove the whitespace from str
name = name.strip().title() # = refers to assignment adn capitalize every starting letter

# split user's name into first name and last name 
first, last = name.split(" ")
print(f"Hello, {first} | {last}") # This is how you print the value of a variable inside the double quotes.

