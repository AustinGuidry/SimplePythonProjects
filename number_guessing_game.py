#RNG Guessing Game

import random

print("Hello, there!")
print("")
name = input("What's your name? ")
print("")
print(f"Hello, {name}!")
print("")
input("Would you like to play a game? ")
print("")
print("I'm thinking of a number.")
print("...")
print("...")
print("...")
print("It's between 1-100")
print("")
random_number = random.randint(1, 100)

guess = int(input("Have a guess! "))
while guess != random_number:
  if guess < random_number:
    guess = int(input("Too low! Try again! "))
  else:
    guess = int(input("Oooh, too high! Try again! "))
print(f"BOOM!! Nailed it! It was {random_number}!!")
print("")
print("Thanks for playing!")
print("Austin")
