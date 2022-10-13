print("Program Started!")

asc = int(input("Please enter an ASCII code: "))

if asc >= 32 and asc <= 126:
    print(f"The character represented by the ASCII value {asc} is: {chr(asc)}")
else:
    print("cannot represent value")

print("program ended")

