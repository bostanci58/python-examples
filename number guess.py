import random

randomNumber = random.randint(1,100)
numberGuesses = 0
while True:
    guess = int(input("Guess numbers from 1 to 100 : "))
    numberGuesses += 1
    if guess < randomNumber:
        print("Please enter a larger number")
        continue
    elif guess > randomNumber:
        print("Please enter a smaller number")
        continue
    else:
        print(f"Congratulations, you got the number on the {numberGuesses}th try.")
        break