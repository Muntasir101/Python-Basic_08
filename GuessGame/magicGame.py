"""
 1 - 5
 1 = You are lucky
 2 = Decent
 3 = Its rainy day
 4 = This is good
 5 = Nothing

"""
import random

secretNumber = random.randint(1, 5)


def game():
    print("Game Start.Take a Guess: ")
    guess = int(input())

    if guess == secretNumber:
        print("Success")

    else:
        print("Guess Wrong")

    if secretNumber == 1:
        print('1 You are lucky')

    elif secretNumber == 2:
        print('2 Decent')

    elif secretNumber == 3:
        print('3 Its rainy day')

    elif secretNumber == 4:
        print('4 This is good')

    else:
        print('5 Nothing')


game()
