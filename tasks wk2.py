
direction = input("what direction should i paint (up, down, left or right)? ")

if direction == "up":
    print("I am painting up")
elif direction == "down":
    print("I am painting down")
elif direction == "left":
    print("I am painting left")
elif direction == "right":
    print("I am painting right")
else:
    print("enter a valid answer")

number = int(input("Please enter a whole number"))

if number % 2 == 0:
    print("even")
else:
    print("odd")


number_1 = int(input("Enter first number: "))

number_2 = int(input("Enter second number: "))

if number_1 < number_2:
    print("The first number is smallest")
elif number_2 < number_1:
    print("The second number is the smallest")
else:
    print("Both are equal")


