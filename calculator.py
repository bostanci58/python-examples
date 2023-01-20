number1 = float(input("Enter to number : "))
number2 = float(input("Enter to number two : "))
process = input("Addition : 1 \nextraction : 2 \nİmpact : 3 \nDivide : 4 \nEnter transaction : ")
if process == "1":
    Addition = number1 + number2
    print(Addition)
elif process == "2":
    extraction = number1 - number2
    print(extraction)
elif process == "3":
    İmpact = number1 * number2
    print(İmpact)
elif process == "4":
    Divide = number1 / number2
    print(Divide)
else:
    print("You entered the transaction incorrectly")