Fconclusion = 0
Cconclusion = 0

process = int(input("""Convert Fahrenheit to Celsius : 1
Convert Celsius to Fahrenheit : 2
Which one do you choose : """))
if process == 1:
    fahrenheitvalue = float(input("Enter the Fahrenheit value : "))
    Cconclusion = (fahrenheitvalue - 32) / 1.8
    Cconclusion = round(Cconclusion, 2)
    print(Cconclusion)
elif process == 2:
    celsiusvalue = float(input("Enter the Celsius value : "))
    Fconclusion = celsiusvalue * 1.8 + 32
    Fconclusion = round(Fconclusion, 2)
    print(Fconclusion)
else:
    print("You entered the transaction value incorrectly")