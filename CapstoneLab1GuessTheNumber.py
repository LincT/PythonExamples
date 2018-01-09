# small number guessing game
import random


def chooseNumber():
    val = random.randint(1, 100)
    return val


def evaluateGuess(number, guess):
    if 1 <= guess <= 100:
        if number > guess:
            return "high"
        elif number < guess:
            return "low"
        elif number == guess:
            return "correct"
    else:
        print("invalid guess, must be between 1 and 100")


def main():
    chosen = chooseNumber()
    result = ""
    while result != "correct":
        guess = int(input("Guess a number between 1 and 100"))
        result = (evaluateGuess(chosen, guess))
        print(result)


main()
