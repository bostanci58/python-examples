conclusion = 0
def bodyMassIndex(kilo, size):
    conclusion = (kilo / (size * size))
    print(conclusion)
while True:
    bodyMassIndex(int(input("Enter the amount of weight in kilograms : ")), float(input("Enter your height in meters : ")))
