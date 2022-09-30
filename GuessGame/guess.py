import random

secretNumber = random.randint(1, 5)
print('I am thinking of a number between 1 and 5')

# ask player to guess
for guessesTaken in range(1, 2):
    print("Game Start.Take a Guess: ")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low")

    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break

if guess == secretNumber:
    print("You are The ultimate Winner !!!!")
    print("Good Job! you guessed secret number in " + str(guessesTaken) + ' Guesses!')

else:
    print("Nope!! The computer generated random number was " + str(secretNumber))

print("Game End")