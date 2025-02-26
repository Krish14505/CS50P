name = input("What's your name? ")

match name: 
    case "harry" | "Harmione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # default
        print(f"who is {name}?")