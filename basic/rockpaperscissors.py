from random import choice

choices = ["rock", "paper", "scissors", "quit"]

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player = input("Player make your move: ").lower()

    if player in choices:
        if player == "quit":
            break

        computer = choice(choices)
        print(f"Computer choose {computer}")

        if player == computer:
            print("Tie")
        elif player == "rock" and computer == "scissors":
            print("You win")
            player_wins += 1
        elif player == "paper" and computer == "rock":
            print("You win")
            player_wins += 1
        elif player == "scissors" and computer == "paper":
            print("You win")
            player_wins += 1
        else:
            print("Computer wins")
            computer_wins += 1
    else:
        print("No valid option")

print(f"FINAL SCORES: Player Score: {player_wins} Computer Score: {computer_wins}")

if player_wins > computer_wins:
    print("Congrats! You Won!!!")
elif player_wins == computer_wins:
    print("It's a tie!")
else:
    print("Oh no! Computer Won")
