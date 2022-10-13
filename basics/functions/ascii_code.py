print("Program Started!")
character = input("Please enter a standard character: ")

if len(character) ==1:
    print(f"The ASCII code for {character} is {ord(character)}")

else:
    print("Input needs to be a single character")

print("Program Ended")