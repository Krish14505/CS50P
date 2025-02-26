# Lecture 01: Variables & Functions
How to print something to the console.
- print("Hello, World")

Functions and Arguments
- functions: Ready made things that a developer can use to do something
Arguments: A value or values that being passed inside the function.

Bug
- It is a mistake/ mistakes in the program.
Don't get discouraged when things won't work.

Comments: 
- A notes that viewer(developer) can understand what the lines of code is doing. comments are ignored by the compiler. Sign(#)

Pseudocode: 
- A human language that explain the code. 
- Beofre writing the code, it is a better practice to use pseudocode for thinking about the logic

documentation: docs.python.org

Investigation of print():
docs.python.org/3/library/functions.html#print
- print(*objects, sep=' ', end = '\n', file=sys.stdout, flush= flase)

escape character: \
- print("hello, \"friend\""): It reminds the compiler not to get confused with the double quotes placing. 

Parameters & Named Parameters: 

Format string: f
- print(f"Hello, {firstName} {lastName}")
- This is how we can format the string where the value comes from the variable(firstName,lastName)

String Methods:
docs.python.org/3/library/stdtypes.html#string-methods
1. strip(): removes the whitespace from str
2. capitalize(): capitalize the first letter of  a string into uppercase
3. title(): capitalize the first letter of all strings into uppercase

int: 
- It's just a number
- Arithmatic Expression: + , - , * , / , %

Project Alert: 
Calculator

float: 
- Its number with decimal number.
- float also allows to contain the integers.
l
int functions: 
- docs.python.ord/3/library/functions.html#round : It returns the nearest integers to its input.

Function:
- Invent own function along with using the built-in functions.
- Keyword that is used to create the function: def
- parameterized functions
    Give the default value to the parameters.

Note: Function must be declared before its been called. However, The only way to solve this problem is to define everything in the main function and then call the main() function at the very end of the code. 


Scope: 
- The existance of a variable is only valid when we use the variable in the scope. For example, if we use python
