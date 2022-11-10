# Copyright 2022 PI515

import random

keepAsking = True
while keepAsking:
    num = input('Type a number for an upper bound: ')
    if num.isdigit():
        print("Let's play!")
        num = int(num)
        keepAsking = False
    else:
        print("Invalid input. Try again.")
sec = num-1
secret = random.randint(2, sec)
guess = None
count = 1
print("Secret #", secret)

while guess != secret:
    guess = input("Type a number between 1 and " + str(num) + ": ")
    if guess.isdigit():
        guess = int(guess)
    if guess == secret:
        print("You got it!")
    else:
        print("Try again.")
        count += 1

if count == 1:
    print("It took you", count, "guess!")
else:
    print("It took you", count, "guesses!")
