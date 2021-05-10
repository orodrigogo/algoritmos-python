option = 0

while True:
    print("""
            [1] - Sum
            [2] - Multiplication
            [3] - Subtraction
            [4] - Split 
            [5] - Exit Program        
        """)
    option = int(input("Chose the option:"))

    if option == 5:
        break

    numberA = int(input('Input the first number: '))
    numberB = int(input('Input the second number: '))

    if option == 1:
        print(f"Result the Sum is: { numberA + numberB }")
    elif option == 2:
        print(f"Result the Multiplication is: { numberA * numberB }")
    elif option == 3:
        print(f"Result the Subtraction is: { numberA - numberB }")
    elif option == 4:
        print(f"Result the Split is: { numberA / numberB }")
    elif option == 0 or option > 5:
        print("Invalid Option")

    input("Continue...")

print("Thanks for use my Program!")
