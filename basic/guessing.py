from random import randint

number = randint(1, 10)

while True:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess < number:
        print("TOO LOW!")
    elif guess > number:
        print("TOO HIGH!")
    else:
        print("YOU WON!!!")
        play_again = input("Do you wan to play again? (y/n)")
        if play_again == "y":
            number = randint(1, 10)
            guess = None
        else:
            print("Thank you for playing")
            break
