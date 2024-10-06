import random

jackpot = random.randint(1,100)

guess = int(input("Guess the number: "))
Counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess lower")

    guess = int(input("Guess again: "))
    Counter += 1


print("Correct Guess")
print("You took", Counter, "attempts")