import random

print("Number Guessing Game ")
print("Guess a number between 1 to 9 ")
guess=input("Enter your guess:" )

chances=5
number=random.randint(0, 10)
while (chances>=5):
    chances=chances-1
    print(guess)
if guess == number:
    print("CONGRATS you won!!!!") 
if not chances < 5:
    print("YOU LOSE!!! the number is"+number)   
    








