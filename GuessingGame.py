import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 20. Can you guess it?")

number = random.randint(1, 20)
tries = 0

while tries < 5:
    guess = int(input("Enter your guess: "))
    tries += 1

    if guess == number:
        print("Congratulations! You guessed the number in", tries, "tries.")
        break
    elif guess < number:
        print("Sorry, your guess is too low. Try again.")
    else:
        print("Sorry, your guess is too high. Try again.")

if tries == 5:
    print("Sorry, you didn't guess the number in time. The number was", number, ".")
